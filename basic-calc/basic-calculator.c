/**
 * Basic Calculator
 * 
 * David Yue
 */

#include <stdarg.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// terminal macro color codes
#define RED    "\033[31m"
#define GREEN  "\033[32m"
#define YELLOW "\033[33m"
#define RESET  "\033[0m"

static long parse_sums ();

typedef enum { PLUS, MINUS, MULT, DIV, LPAREN, RPAREN, NUMBER, END } TokenType;

typedef struct {
        TokenType type;
        long value;
        size_t col_no;
} Token;

// buffer to store user input
char *buf = NULL;

size_t buf_size = 0;
size_t buf_count = 0;

// column number of current symbol
size_t col_no = 0;

// pointer to current symbol
char *current = NULL;

// current token
Token current_token = { 0 };

bool has_error = false;

static void error (size_t start, size_t end, char *title, char *message, ...)
{
        // minimize cascading errors
        if (has_error)
                return;

        va_list args;

        va_start (args, message);

        has_error = true;

        // prints out a nice looking error message and can underline a part of
        // the expression
        fprintf (stderr, YELLOW);
        vfprintf (stderr, title, args);
        fprintf (stderr, RESET);

        putc ('\n', stderr);

        // highlight the relevant part of the expression in red
        for (size_t i = 0; buf[i] != '\0'; i++) {
                if (i >= start && i <= end) {
                        fprintf (stderr, RED);
                        putc (buf[i], stderr);
                        fprintf (stderr, RESET);
                } else {
                        putc (buf[i], stderr);
                }
        }

        putc ('\n', stderr);
        fprintf (stderr, YELLOW);
        // underline the expression
        for (size_t i = 0; i < strlen (buf) + 10; i++) {
                if (i >= start && i <= end) {
                        putc ('^', stderr);
                } else if (i > end) {
                        putc ('~', stderr);
                } else {
                        putc (' ', stderr);
                }
        }

        fprintf (stderr, GREEN);
        putc (' ', stderr);
        vfprintf (stderr, message, args);
        putc ('\n', stderr);
        fprintf (stderr, RESET);

        va_end (args);
}

static char advance ()
{
        // in the beginning, current is NULL, update it to point to buffer
        // instead.
        if (!current) {
                col_no = 0;
                current = buf;
                return '\0';
        }

        // save old current char
        char old = *current;

        // advance to next symbol, provided we haven't reached the end
        if (*current != '\0') {
                current++;
                col_no++;
        }
        return old;
}

static bool match (char c)
{
        // safe guard, this should never be true
        if (!current)
                return false;

        // only advance if character matches what we expect
        if (*current == c) {
                advance ();
                return true;
        }
        return false;
}

static char peek ()
{
        return *current;
}

static bool is_number (char c)
{
        // this does ASCII value comparison, making sure c is a numeric
        // character
        return ('0' <= c && c <= '9');
}

static long number (char first)
{
        // converts a base-10 integer string to an actual integer
        long n = first - '0';
        while (is_number (peek ())) {
                n *= 10;
                n += advance () - '0';
        }
        return n;
}

static Token create_token (TokenType type, long value)
{
        Token t = { .type = type, .value = value, .col_no = col_no - 1 };

        return t;
}

static Token next_token ()
{
        for (;;) {
                char c = peek ();

                if (c == '\0')
                        return create_token (END, 0);

                advance ();

                switch (c) {
                case '+': return create_token (PLUS, 0);
                case '-': return create_token (MINUS, 0);
                case '*': return create_token (MULT, 0);
                case '/': return create_token (DIV, 0);
                case ')': return create_token (RPAREN, 0);
                case '(': return create_token (LPAREN, 0);

                // filter out all the crap we don't need
                case ' ':
                case '\t':
                case '\n':
                case '\r': continue;

                // should be number if above don't match
                default:
                        if (is_number (c))
                                return create_token (NUMBER, number (c));
                        else {
                                error (col_no - 1,
                                       col_no - 1,
                                       "error: unexpected character %c",
                                       "symbol unrecognized",
                                       c);
                                continue;
                        }
                }
        }
}

static Token peek_token ()
{
        return current_token;
}

static Token advance_token ()
{
        Token old = current_token;

        if (old.type != END)
                current_token = next_token ();

        return old;
}

static bool match_token (TokenType type)
{
        if (current_token.type == type) {
                advance_token ();
                return true;
        }

        return false;
}

static long parse_primary ()
{
        Token t = peek_token ();

        // parenthesized expression
        if (match_token (LPAREN)) {
                // parse the same way as original
                long ans = parse_sums ();
                size_t rparen_col = peek_token ().col_no;
                if (!match_token (RPAREN)) {
                        error (t.col_no,
                               t.col_no,
                               "error: unmatched opening parentheses",
                               "possibly missing closing parentheses ')'");
                }
                return ans;
        } else if (match_token (NUMBER)) {
                // numeric value
                return t.value;
        } else if (match_token (END)) {
                error (t.col_no, t.col_no, "", "unexpected EOF");
                return 0;
        } else {
                // some shit went wrong
                error (t.col_no,
                       t.col_no,
                       "error: unexpected token",
                       "expected parenthesized expression or numeric value");
                return 0;
        }
}

static long parse_unary ()
{
        // allows for negative numbers essentially, -5 + 4 etc.
        // also chained negatives like --5 etc.

        return match_token (MINUS) ? -parse_unary () : parse_primary ();
}

static long parse_products ()
{
        // logic is the same as parse_sums()
        long left = parse_unary ();

        while (1) {
                if (match_token (MULT)) {
                        left *= parse_unary ();

                } else if (match_token (DIV)) {
                        Token start = peek_token ();

                        long ans = parse_unary ();

                        Token end = peek_token ();

                        // if right side is 0, error
                        if (ans == 0) {
                                error (start.col_no,
                                       end.col_no,
                                       "error: cannot divide by 0",
                                       "the following divisor evaluates to 0");
                                return 0;
                        }

                        left /= ans;

                } else {
                        break;
                }
        }
        return left;
}

static long parse_sums ()
{
        // parse left side of +/- op. we always call one precedence level up,
        // this ensures we follow the order of operations correctly

        long left = parse_products ();

        // while there is a op, parse the right side. this allows for chained
        // expressions: 1 + 4 + 5 etc.
        while (1)
                if (match_token (PLUS))
                        left += parse_products ();
                else if (match_token (MINUS))
                        left -= parse_products ();
                else
                        break;

        return left;
}

static long parse_expression ()
{
        // make sure globals are initialized
        advance ();
        current_token.type = -1;
        advance_token ();

        // parse from lowest precedence to highest
        return parse_sums ();
}

static void buffer_write_char (char c)
{
        if (buf_count + 1 >= buf_size) {
                // update size, start with 8, increase by factor
                // of 2 each time we run out of space
                if (buf_size == 0)
                        buf_size = 8;
                else
                        buf_size *= 2;

                buf = realloc (buf, buf_size);

                // we must error check realloc
                if (!buf) {
                        perror ("realloc");
                        exit (EXIT_FAILURE);
                }
        }

        buf[buf_count++] = c;
        buf[buf_count] = '\0';
}

static void buffer_reset ()
{
        buf_size = buf_count = 0;
        current = NULL;

        if (buf) {
                free (buf);
                buf = NULL;
        }
}

int main (int argc, char **argv)
{
        printf ("Basic Calculator\n"
                "Ctrl-C/D to exit\n");

        /**
         * We wish to save the user's entire input expression in a buffer in
         * order to output friendly error messages.
         *
         * If we can accept unhelpful errors than this step is not neccessary,
         * we can read char by char and "forget" whatever was read in the past.
         *
         * i.e we just use fgetc(stdin) each time in advance()
         *
         * This is because our parser only ever needs to read the next symbol in
         * the expression and never needs to look backwards to successfully
         * compute the expression.
         *
         * This is obvious when we look at the input handling methods which all
         * our other functions are built upon:
         *
         * advance() only ever advances to the next symbol
         * match() advances if current symbol matches what we expect
         * peek() returns the current symbol
         *
         * There is no method to go backwards
         */

        while (1) {
                printf ("Enter an expresssion: ");

                int c;

                while ((c = fgetc (stdin)) != EOF) {
                        if (c == '\n')
                                break;

                        buffer_write_char (c);
                }

                if (c == EOF || buf_size == 0)
                        exit (EXIT_SUCCESS);

                // parse expression
                long ans = parse_expression ();

                // ensure no junk at the end of the expression
                if (!match_token (END)) {
                        error (peek_token ().col_no,
                               strlen (buf) + 1,
                               "error: incomplete expression",
                               "unused");
                } else {
                        if (!has_error)
                                printf ("%ld\n", ans);
                }

                buffer_reset ();
                has_error = false;
        }
}