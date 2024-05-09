#include <cs50.h>
#include <errno.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

// each of our text files contains 1000 words
#define LISTSIZE 1000

// values for colors and score (EXACT == right letter, right place; CLOSE == right letter, wrong place; WRONG == wrong
// letter)
#define EXACT 2
#define CLOSE 1
#define WRONG 0

// ANSI color codes for boxed in letters
#define GREEN  "\e[38;2;255;255;255;1m\e[48;2;106;170;100;1m"
#define YELLOW "\e[38;2;255;255;255;1m\e[48;2;201;180;88;1m"
#define RED    "\e[38;2;255;255;255;1m\e[48;2;220;20;60;1m"
#define RESET  "\e[0;39m"

void strip (char *s)
{
        char *p = strchr (s, '\n');

        if (p)
                *p = '\0';

        p = strchr (s, '\r');
        if (p)
                *p = '\0';
}

char *read_line ()
{
        char *buffer = malloc (8 * sizeof (char));

        if (!buffer) {
                perror ("malloc");
                exit (EXIT_FAILURE);
        }

        size_t buffer_size = 8;
        size_t buffer_count = 0;
        char c;

        while ((c = fgetc (stdin)) != EOF) {
                buffer[buffer_count++] = c;

                if (c == '\n') {
                        break;
                }

                if (buffer_count + 1 == buffer_size) {
                        buffer = realloc (buffer, 2 * buffer_size);
                        buffer_size *= 2;
                }
        }

        buffer[buffer_count] = '\0';

        return buffer;
}

char *prompt_word (int word_size)
{
        for (;;) {
                printf ("Input a %d-letter word: ", word_size);

                char *word = read_line ();
                if (strlen (word) - 1 != word_size) {
                        free (word);
                        continue;
                }

                strip (word);

                return word;
        }
}

int guess_status (char *expected_word, char *word)
{
        char *curr = expected_word;
        int correct = 0;
        for (int i = 0; i < strlen (expected_word); i++) {
                if (expected_word[i] == word[i]) {
                        printf (GREEN "%c" RESET, word[i]);
                        correct++;
                } else if (strchr (expected_word, word[i])) {
                        printf (YELLOW "%c" RESET, word[i]);
                } else {
                        printf (RED "%c" RESET, word[i]);
                }
        }

        putchar ('\n');

        return correct == strlen (expected_word);
}

void find_random_word (char *word_buffer, int buffer_size, int word_size)
{
        if (word_size < 5 || word_size > 8) {
                fprintf (stderr, "error: find_random_word: received invalid word size");
                exit (EXIT_FAILURE);
        }

        char filename[12];
        sprintf (filename, "words/%d.txt", word_size);

        FILE *word_list = fopen (filename, "r");

        if (!word_list) {
                perror ("fopen");
                exit (EXIT_FAILURE);
        }

        int word_index = rand () % LISTSIZE;

        int word_count = 0;

        while (fgets (word_buffer, buffer_size, word_list) != NULL) {
                if (word_count++ == word_index)
                        break;
        }
        strip (word_buffer);
        fclose (word_list);
}

int main (int argc, char **argv)
{
        srand (time (NULL));

        if (argc != 2) {
                fprintf (stderr, "usage: %s wordsize", argv[0]);
                exit (EXIT_FAILURE);
        }

        char *end_ptr = NULL;
        int word_size = strtol (argv[1], &end_ptr, 10);

        if (end_ptr == argv[1]) {
                fprintf (stderr, "error: not a valid word size!");
                exit (EXIT_FAILURE);
        }

        if (errno != 0) {
                perror ("strtol");
                exit (EXIT_FAILURE);
        }

        int tries = 6;

        char expected_word[word_size + 2];

        find_random_word (expected_word, word_size + 2, word_size);
        printf ("%s\n", expected_word);
        while (tries > 0) {
                char *word = prompt_word (word_size);

                if (guess_status (expected_word, word)) {
                        break;
                }
        }
}