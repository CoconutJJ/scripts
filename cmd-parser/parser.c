#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int is_whitespace (char c)
{
        switch (c) {
        case ' ':
        case '\t':
        case '\n':
        case '\0':
        case '\r': return 1;
        default: return 0;
        }
}

char *consume_whitespace (char *cmd)
{
        for (; *cmd; cmd++) {
                if (!is_whitespace (*cmd))
                        return cmd;
        }

        return NULL;
}

char **parse_argv (char *cmd)
{
        size_t n_args = 0;
        char *cmd_orig = cmd;
        for (;; cmd++) {
                if (is_whitespace (*cmd)) {
                        n_args++;

                        if (!*cmd)
                                break;

                        *cmd = '\0';
                        cmd++;
                        cmd = consume_whitespace (cmd);
                }
        }
        char **argv = malloc (n_args * sizeof (char *));

        if (!argv) {
                perror ("malloc");
                exit (EXIT_FAILURE);
        }

        for (size_t i = 0; i < n_args; i++) {
                argv[i] = cmd_orig;

                cmd_orig = strchr (cmd_orig, '\0');
                cmd_orig++;
                cmd_orig = consume_whitespace (cmd_orig);
        }

        return argv;
}

int main (int argc, char **argv)
{
        char cmd[] = "python --help -c -d -k hello.py\0";

        char **args = parse_argv (cmd);

        for (int i = 0; i < 6; i++) {
                printf ("%s\n", args[i]);
        }
}
