#pragma once

#include <stdint.h>
#include <stdlib.h>

#define MAX_FLAGS             100
#define MAX_LONG_FLAG_LENGTH  120
#define MAX_SHORT_FLAG_LENGTH 2

enum ArgumentParserOptions {
        ARGPARSE_ACTION_STORE_TRUE,
        ARGPARSE_ACTION_STORE_FALSE,
        ARGPARSE_ACTION_STORE,
        ARGPARSE_ACTION_COUNT,
        ARGPARSE_ACTION_HELP,
        ARGPARSE_ACTION_EXTEND,
        ARGPARSE_TYPE_STR,
        ARGPARSE_TYPE_DBL,
        ARGPARSE_TYPE_INT,
        ARGPARSE_NOT_APPLICABLE
};

struct ArgumentParserArg {
        union {
                int64_t int_value;
                char *str_value;
                double dbl_value;
        };
};

struct ArgumentParserFlag {
        char long_flag[MAX_LONG_FLAG_LENGTH + 1];
        char short_flag[MAX_SHORT_FLAG_LENGTH + 1];
        char *help_text;
        enum ArgumentParserOptions action;
        union {
                struct {
                        enum ArgumentParserOptions type;
                        size_t nargs;
                        size_t argument_size;
                        size_t argument_count;
                        struct ArgumentParserArg *arguments;
                };

                int occurence_count;
                int exists;
        };
};

struct ArgumentParser {
        int argc;
        char **argv;
        int n_flags;
        struct ArgumentParserFlag flags[MAX_FLAGS];
};

void argparse_free (struct ArgumentParser *parser);
struct ArgumentParserFlag *argparse_get_flag (struct ArgumentParser *parser, char *flag);
int argparse_add_argument (struct ArgumentParser *parser,
                           const char *short_name,
                           const char *long_name,
                           int nargs,
                           enum ArgumentParserOptions action,
                           enum ArgumentParserOptions type,
                           char *help_text);

int argparse_parse_args (struct ArgumentParser *parser);
void argparse_init (struct ArgumentParser *parser, int argc, char **argv);