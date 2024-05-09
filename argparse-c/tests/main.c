#include "argparse.h"
#include <stdio.h>
#include <stdlib.h>

int main (int argc, char **argv)
{
        struct ArgumentParser parser;

        argparse_init (&parser, argc, argv);

        argparse_add_argument (
                &parser, "-c", "--choice", 0, ARGPARSE_ACTION_STORE_TRUE, ARGPARSE_NOT_APPLICABLE, "Choice");
        argparse_add_argument (&parser, "-n", "--nums", 3, ARGPARSE_ACTION_STORE, ARGPARSE_TYPE_STR, "Choice");
        argparse_add_argument (&parser, "-h", "--help", 0, ARGPARSE_ACTION_HELP, ARGPARSE_NOT_APPLICABLE, "Show help message");
        argparse_parse_args (&parser);

        struct ArgumentParserFlag *flag = argparse_get_flag (&parser, "-n");

        for (int i = 0; i < flag->argument_count; i++) {
                printf ("%s\n", flag->arguments[i].str_value);
        }
}