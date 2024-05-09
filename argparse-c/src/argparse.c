/**
 * argparse: A Python argparse inspired C command line parsing library
 *
 * Author: David Yue
 */
#include "argparse.h"
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/**
 * Initializes a ArgumentParser structure
 *
 * argc: argument count
 * argv: argument vector
 */
void argparse_init (struct ArgumentParser *parser, int argc, char **argv)
{
        parser->argc = argc;
        parser->argv = argv;
        parser->n_flags = 0;
}

static char *get_usable_flag_name (struct ArgumentParserFlag *flag)
{
        if (flag->long_flag[0] != '\0') {
                return flag->long_flag;
        } else if (flag->short_flag[0] != '\0') {
                return flag->short_flag;
        } else {
                fprintf (stderr, "FATAL error: no valid flag name!\n");
                exit (EXIT_FAILURE);
        }
}

/**
 * Frees all allocated memory related to ArgumentParser structure
 */
void argparse_free (struct ArgumentParser *parser)
{
        for (int i = 0; i < parser->n_flags; i++) {
                struct ArgumentParserFlag *flag = &(parser->flags[i]);

                if (flag->arguments)
                        free (flag->arguments);
        }
}

/**
 * Finds flag structure in ArgumentParser structure
 */
static struct ArgumentParserFlag *find_flag (struct ArgumentParser *parser, const char *flag)
{
        for (int i = 0; i < parser->n_flags; i++) {
                struct ArgumentParserFlag *current_flag = (parser->flags + i);
                if (strcmp (current_flag->short_flag, flag) == 0)
                        return current_flag;
                if (strcmp (current_flag->long_flag, flag) == 0)
                        return current_flag;
        }

        return NULL;
}

static int add_flag (struct ArgumentParser *parser, struct ArgumentParserFlag new_flag)
{
        if (parser->n_flags == MAX_FLAGS)
                return 0;

        parser->flags[parser->n_flags++] = new_flag;

        return 1;
}

static void update_flag_arguments_array (struct ArgumentParserFlag *flag)
{
        if (!flag->arguments) {
                flag->argument_size = 8;
                flag->argument_count = 0;
                flag->arguments = malloc (flag->argument_size * sizeof (struct ArgumentParserArg));

                if (!flag->arguments) {
                        perror ("malloc");
                        exit (EXIT_FAILURE);
                }
        }

        if (flag->argument_count == flag->argument_size) {
                flag->argument_size *= 2;
                flag->arguments = realloc (flag->arguments, flag->argument_size * sizeof (struct ArgumentParserArg));

                if (!flag->arguments) {
                        perror ("realloc");
                        exit (EXIT_FAILURE);
                }
        }
}

static void add_flag_str_argument (struct ArgumentParserFlag *flag, char *value)
{
        update_flag_arguments_array (flag);

        flag->arguments[flag->argument_count++] = (struct ArgumentParserArg){ .str_value = value };
}

static void add_flag_int_argument (struct ArgumentParserFlag *flag, int64_t value)
{
        update_flag_arguments_array (flag);

        flag->arguments[flag->argument_count++] = (struct ArgumentParserArg){ .int_value = value };
}
static void add_flag_dbl_argument (struct ArgumentParserFlag *flag, double value)
{
        update_flag_arguments_array (flag);

        flag->arguments[flag->argument_count++] = (struct ArgumentParserArg){ .dbl_value = value };
}

static int validate_long_flag_format (const char *flag)
{
        if (flag[0] != '-' || flag[1] != '-')
                return 0;

        for (int i = 0; flag[i] != '\0'; i++) {
                switch (flag[i]) {
                case ' ':
                case '\t':
                case '\n': return 0;
                case '-':
                case '_': continue;
                default:
                        if (('a' <= flag[i] && flag[i] <= 'z') || ('A' <= flag[i] && flag[i] <= 'Z') ||
                            ('0' < flag[i] && flag[i] < '9')) {
                                continue;
                        }
                        return 0;
                }
        }

        if (strlen (flag) > MAX_LONG_FLAG_LENGTH)
                return 0;

        return 1;
}

static int validate_short_flag_format (const char *flag)
{
        if (strlen (flag) != MAX_SHORT_FLAG_LENGTH)
                return 0;

        if (flag[0] != '-')
                return 0;

        char c = flag[1];
        switch (c) {
        case ' ':
        case '\t':
        case '\n':
        case '-':
        case '_': return 0;
        default: break;
        };

        return (('a' <= c && c <= 'z') || ('A' <= c && c <= 'Z') || ('0' < c && c < '9'));
}

int argparse_add_argument (struct ArgumentParser *parser,
                           const char *short_name,
                           const char *long_name,
                           int nargs,
                           enum ArgumentParserOptions action,
                           enum ArgumentParserOptions type,
                           char *help_text)
{
        if (short_name && !validate_short_flag_format (short_name))
                return 0;

        if (long_name && !validate_long_flag_format (long_name))
                return 0;

        struct ArgumentParserFlag flag = { 0 };

        flag.action = action;
        flag.nargs = nargs;
        flag.type = type;
        flag.help_text = help_text;

        switch (flag.action) {
        case ARGPARSE_ACTION_STORE_FALSE: flag.exists = 1; break;
        default: break;
        }

        if (long_name)
                strcpy (flag.long_flag, long_name);
        if (short_name)
                strcpy (flag.short_flag, short_name);

        if (flag.long_flag[0] == '\0' && flag.short_flag[0] == '\0') {
                fprintf (stderr, "error: must specify either flag long name or flag short, cannot both be NULL\n");
                exit (EXIT_FAILURE);
        }

        return add_flag (parser, flag);
}

static void output_help_text (struct ArgumentParser *parser)
{
        printf ("usage: %s ", parser->argv[0]);

        for (int i = 0; i < parser->n_flags; i++) {
                struct ArgumentParserFlag *f = &(parser->flags[i]);

                if (f->long_flag[0] == '\0' || f->short_flag[0] == '\0') {
                        printf ("[%s] ", get_usable_flag_name (f));
                } else {
                        printf ("[%s | %s] ", f->long_flag, f->short_flag);
                }
        }

        putchar ('\n');
        for (int i = 0; i < parser->n_flags; i++) {
                struct ArgumentParserFlag *f = &(parser->flags[i]);

                if (f->long_flag[0] == '\0' || f->short_flag[0] == '\0') {
                        printf ("%s : %s\n", get_usable_flag_name (f), f->help_text);
                } else {
                        printf ("%s | %s : %s\n", f->long_flag, f->short_flag, f->help_text);
                }
        }
}

struct ArgumentParserFlag *argparse_get_flag (struct ArgumentParser *parser, char *flag)
{
        return find_flag (parser, flag);
}

int verify_flag_arguments_complete (struct ArgumentParserFlag *flag)
{
        return flag->argument_count == flag->nargs;
}

int apply_no_argument_flag_action (struct ArgumentParserFlag *flag)
{
        switch (flag->action) {
        case ARGPARSE_ACTION_COUNT: flag->occurence_count++; break;
        case ARGPARSE_ACTION_STORE_TRUE: {
                flag->exists = 1;
                break;
        }
        case ARGPARSE_ACTION_STORE_FALSE: {
                flag->exists = 0;
                break;
        }
        default: {
                return 0;
        }
        }

        return 1;
}

int argparse_parse_args (struct ArgumentParser *parser)
{
        enum State { PARSE_FLAG, PARSE_FLAG_ARG };

        enum State current_state = PARSE_FLAG;

        struct ArgumentParserFlag *current_flag = NULL;
        int args_parse_count = 0;

        for (int i = 1; i < parser->argc; i++) {
                char *curr_arg = parser->argv[i];

                switch (current_state) {
                case PARSE_FLAG:

                        if (!validate_short_flag_format (curr_arg) && !validate_long_flag_format (curr_arg)) {
                                if (!current_flag) {
                                        fprintf (stderr, "error: unknown argument %s\n", curr_arg);
                                        exit (EXIT_FAILURE);
                                }

                                fprintf (stderr,
                                         "error: flag %s received unexpected argument: %s\n",
                                         get_usable_flag_name (current_flag),
                                         curr_arg);

                                exit (EXIT_FAILURE);
                        }

                        current_flag = find_flag (parser, curr_arg);
                        args_parse_count = 0;

                        if (!current_flag)
                                return 0;

                        if (current_flag->action == ARGPARSE_ACTION_HELP) {
                                output_help_text (parser);
                                exit (EXIT_SUCCESS);
                        }

                        if (apply_no_argument_flag_action (current_flag)) {
                                if (current_flag->type != ARGPARSE_NOT_APPLICABLE) {
                                        fprintf (
                                                stderr,
                                                "error: flag data type must be ARGPARSE_NOT_APPLICABLE if flag does not take any arguments: %s\n",
                                                get_usable_flag_name (current_flag));
                                        exit (EXIT_FAILURE);
                                }

                        } else {
                                if (current_flag->action != ARGPARSE_ACTION_EXTEND) {
                                        if (current_flag->arguments != NULL) {
                                                fprintf (stderr,
                                                         "error: flag %s declared twice\n",
                                                         get_usable_flag_name (current_flag));
                                                exit (EXIT_FAILURE);
                                        }
                                }
                                current_state = PARSE_FLAG_ARG;
                        }

                        break;
                case PARSE_FLAG_ARG: {
                        if (validate_short_flag_format (curr_arg) || validate_long_flag_format (curr_arg)) {
                                current_state = PARSE_FLAG;
                                continue;
                        }

                        switch (current_flag->action) {
                        case ARGPARSE_ACTION_STORE:
                        case ARGPARSE_ACTION_EXTEND:

                                if (current_flag->argument_count != 0) {
                                        args_parse_count = current_flag->argument_count;
                                }

                                if (current_flag->nargs == args_parse_count)
                                        return 0;

                                switch (current_flag->type) {
                                case ARGPARSE_TYPE_STR: add_flag_str_argument (current_flag, curr_arg); break;
                                case ARGPARSE_TYPE_INT: {
                                        char *end_ptr = NULL;
                                        int64_t value = strtol (curr_arg, &end_ptr, 10);

                                        if (*end_ptr != '\0')
                                                return 0;

                                        add_flag_int_argument (current_flag, value);
                                        break;
                                }
                                case ARGPARSE_TYPE_DBL: {
                                        char *end_ptr = NULL;
                                        double value = strtod (curr_arg, &end_ptr);

                                        if (*end_ptr != '\0')
                                                return 0;

                                        add_flag_dbl_argument (current_flag, value);
                                        break;
                                }
                                default: {
                                        fprintf (stderr,
                                                 "error: invalid flag argument data type specified for %s\n",
                                                 get_usable_flag_name (current_flag));
                                        return 0;
                                }
                                }

                                break;

                        default: {
                                fprintf (stderr,
                                         "error: invalid action for flag %s\n",
                                         get_usable_flag_name (current_flag));

                                exit (EXIT_FAILURE);
                                break;
                        }
                        }
                        args_parse_count++;
                }
                default: {
                        __builtin_unreachable ();
                        break;
                }
                }
        }

        for (int i = 0; i < parser->n_flags; i++) {
        }

        return 1;
}
