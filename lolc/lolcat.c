/*
 * lolc
 * A version of lolcat written in C
 *
 * @author David Yue <davidyue5819@gmail.com>
 */

#include <getopt.h>
#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

#define FOREGROUND_RGB "\033[38;2;%d;%d;%dm"
#define BACKGROUND_RGB "\033[48;2;%d;%d;%dm"
#define RESET          "\033[0m"

struct configuration;

typedef void (*gradientf) (int, int, int *, int *, int *, struct configuration *);

struct configuration {
        int ncols;
        int nrows;
        char *buffer;
        gradientf grad;
};

int rgb_255 (double p)
{
        return (int)floor (p * 255.0);
}

void red_green_grad (int x, int y, int *r, int *g, int *b, struct configuration *config)
{
        *b = 0;
        *g = rgb_255 ((double)x / (double)config->ncols);
        *r = 255 - *g;
}

void red_green_blue_grad (int x, int y, int *r, int *g, int *b, struct configuration *config)
{
        *r = rgb_255 ((double)x / (double)config->ncols);

        *b = 255 - *r;

        *g = rgb_255 ((double)y / (double)config->nrows);
}

void print_help_message ()
{
        fprintf (stderr,
                 "lolc - A version of lolcat written in C\n"
                 "Usage: lolc [flags] <filename>\n"
                 "Possible Flags:\n"
                 "      --gradient=OPT   sets the gradient function\n"
                 "\n"
                 "OPT may be the following values:\n"
                 "      red_green        red and green horizontal gradient\n"
                 "      red_green_blue   red, green and blue horizontal gradient\n");
}

void initialize (FILE *fp, struct configuration *config)
{
        int c, count = 0, buffer_capacity = 512, buffer_count = 0;

        config->buffer = malloc (buffer_capacity * sizeof (char));

        if (!config->buffer) {
                perror ("malloc");
                exit (EXIT_FAILURE);
        }

        while ((c = fgetc (fp)) != EOF) {
                if (buffer_count == buffer_capacity - 2) {
                        buffer_capacity *= 2;
                        config->buffer = realloc (config->buffer, buffer_capacity * sizeof (char));
                }

                if (c == '\n') {
                        config->ncols = count > config->ncols ? count : config->ncols;
                        config->nrows++;
                        count = 0;
                } else {
                        count++;
                }
                config->buffer[buffer_count++] = (char)c;
        }
        config->buffer[buffer_count] = '\0';
}

gradientf parse_gradient_function (char *grad_name)
{
        if (strcmp (grad_name, "red_green") == 0) return red_green_grad;

        if (strcmp (grad_name, "red_green_blue") == 0) return red_green_blue_grad;

        return NULL;
}

void parse_cmd (int argc, char **argv, struct configuration *config)
{
        struct option cmd_args[] = {
                {"gradient", required_argument, 0, 'g'},
                {    "help",       no_argument, 0, 'h'}
        };
        int opt_index;
        int c;
        int valid_options = 1;

        while ((c = getopt_long (argc, argv, "hg:", cmd_args, &opt_index)) != -1) {
                switch (c) {
                case 'g': {
                        config->grad = parse_gradient_function ((char *)optarg);

                        if (!config->grad) {
                                fprintf (stderr, "error: unrecognized gradient function, see --help\n");
                                exit (EXIT_FAILURE);
                        }

                        break;
                }
                case 'h': {
                        print_help_message ();
                        exit (EXIT_SUCCESS);
                        break;
                }
                case '?': {
                        valid_options = 0;
                        break;
                }

                default: break;
                }
        }

        if (!valid_options) exit (EXIT_FAILURE);

        if (optind == argc) {
                initialize (stdin, config);
        } else {
                FILE *fp = fopen (argv[optind], "r");
                initialize (fp, config);
                fclose (fp);
        }
}

void normal_mode (struct configuration *config)
{
        int x = 0, y = 0;
        char *text_buffer = config->buffer;
        while (*text_buffer) {
                int r, g, b;

                config->grad (x, y, &r, &g, &b, config);

                printf (FOREGROUND_RGB "%c" RESET, r, g, b, *text_buffer);

                if (*text_buffer == '\n') {
                        x = 0;
                        y++;
                } else {
                        x++;
                }
                text_buffer++;
        }
}

void animation_mode (struct configuration *config)
{
}

int main (int argc, char **argv)
{
        struct configuration config = { .ncols = 0, .nrows = 0, .buffer = NULL, .grad = red_green_blue_grad };

        if (!isatty (STDOUT_FILENO)) { fprintf (stderr, "warning: output file is not a terminal"); }

        parse_cmd (argc, argv, &config);

        normal_mode (&config);
}
