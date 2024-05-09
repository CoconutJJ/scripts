#include "../coconut.h"
#include "./io.h"
#include <errno.h>
#include <stdbool.h>
#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>
#include <string.h>
extern editor_configuration configuration;

void _out (char *buffer, size_t len)
{
        if (write (STDOUT_FILENO, buffer, len) != len) {
                perror ("write");
                exit (EXIT_FAILURE);
        }
}

char read_char ()
{
        ssize_t nbytes;
        if (configuration.in._should_read)
                while ((nbytes = read (STDIN_FILENO,
                                       &(configuration.in.c),
                                       sizeof (char))) != 1)
                        if (nbytes == -1 && errno != EAGAIN) {
                                perror ("read");
                                exit (EXIT_FAILURE);
                        }

        return configuration.in.c;
}

char advance_char ()
{
        if (!configuration.in._should_read) {
                configuration.in._should_read = true;
                return configuration.in.c;
        }

        return read_char ();
}

bool has_char ()
{
        // check if a char already in buffer, then no need to read
        if (!configuration.in._should_read)
                return true;

        if (read (STDIN_FILENO, &(configuration.in.c), sizeof (char)) == 1) {
                configuration.in._should_read = false;
                return true;
        }

        return false;
}

bool match_char (char c)
{
        // read a character and check if it matches.
        // if it doesn't match, we make sure not to read a new character next
        // time...
        configuration.in._should_read = (read_char () == c);

        return configuration.in._should_read;
}

bool read_cursor_position (int *line, int *col)
{
        _out (REQUEST_CURSOR_POS, sizeof (REQUEST_CURSOR_POS));

        // expect ESC[ escape sequence prefix
        if (!match_char ('\x1b'))
                return false;

        if (!match_char ('['))
                return false;

        char buf[ESC_BUFFER_SIZE] = { '\0' };

        for (int i = 0; i < ESC_BUFFER_SIZE; i++) {
                buf[i] = advance_char ();

                if (buf[i] == 'R')
                        break;
        }

        // read in the values.
        if (sscanf (buf, "%d;%dR", line, col) != 2) {
                perror ("sscanf");
                exit (EXIT_FAILURE);
        }

        return true;
}

void set_cursor_position (int x, int y)
{
        char buf[ESC_BUFFER_SIZE] = { '\0' };
        sprintf (buf, CURSOR_POS ("%d", "%d"), y, x);
        _out (buf, strlen (buf));
}

void synchronize_cursor_position ()
{
        set_cursor_position (configuration.editor.x, configuration.editor.y);
}

