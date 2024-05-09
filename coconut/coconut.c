/**
 * Coconut Editor
 *
 * Author: David Yue <davidyue5819@gmail.com>
 */
#include <ctype.h>
#include <errno.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include <unistd.h>

#include "./coconut.h"
#include "buffer/buffer.h"
#include "editor/editor.h"
#include "io/io.h"
#include "term/term.h"

void write_performance_log (char *tag, long ms)
{
        FILE *fp = fopen ("perf.log", "a+");

        char buf[32];
        
        sprintf (buf, "%s %ld\n", tag, ms);

        fwrite (buf, strlen (buf), 1, fp);

        fclose (fp);
}

editor_configuration configuration;

void initialize_configuration ()
{
        // save the current configuration of the terminal
        configuration.original_terminal_configuration =
                _get_terminal_configuration ();
        configuration.current_terminal_configuration =
                configuration.original_terminal_configuration;

        // character buffer is invalid at startup, make sure next read() doesn't
        // read from buffer
        configuration.in._should_read = true;

        // no lines in terminal at startup
        configuration.line_count = 0;
        configuration.line_size = 0;
        configuration.lines = NULL;

        // left margin is set to 3 spaces to accomodate tidle
        configuration.editor.left_margin = 3;
        configuration.editor.last_col = configuration.editor.left_margin;
}

void process_control_character (char c)
{
        switch (c) {
        case BACKSPACE: backspace (); break;
        case ENTER: enter (); break;
        default: break;
        }
}

void process_normal_character (char c)
{
        switch (c) {
        default: write_char (c); break;
        }
}

void process_escape_sequence ()
{
        if (!has_char ())
                return;
        // printf("%d,%d\r\n", configuration.editor.x, configuration.editor.y);
        switch (advance_char ()) {
        case ARROW_UP: cursor_up (); break;
        case ARROW_DOWN: cursor_down (); break;
        case ARROW_LEFT: cursor_left (); break;
        case ARROW_RIGHT: cursor_right (); break;
        default: break;
        }
}

void load_file_contents (char *filename)
{
        FILE *fp = fopen (filename, "r");

        if (!fp) {
                perror ("fopen");
                exit (EXIT_FAILURE);
        }

        clear_editor_screen ();

        write_buffer *line = append_line ();
        char line_buf[120];

        while (fgets (line_buf, 120, fp) != NULL) {
                int line_size = strlen (line_buf);

                if (line_buf[line_size - 1] == '\n') {
                        buffer_write (line, line_buf, line_size - 1);

                        line = append_line ();
                } else {
                        buffer_write (line, line_buf, line_size);
                }
        }

        redraw ();

        synchronize_cursor_position ();
}

void init_editor ()
{
#ifdef PERF
        time_t start = clock (), delta;
#endif
        /**
         * Sets up space to store editor state and intializes a bunch
         * of parameters required throughout the lifetime of the program
         */
        initialize_configuration ();

        /**
         * Enables raw mode, adds a exit handler to also disable it when
         * program exits, clears the screen and prepares to draw editor
         * interface
         */
        setup_terminal_for_editor ();

        /**
         * We finally have a workable "canvas" to use. Let's begin drawing
         * the editor interface
         */
        setup_editor ();

        if (configuration.editor.filename)
                load_file_contents (configuration.editor.filename);

#ifdef PERF
        delta = clock () - start;
        write_performance_log ("Setup: ", delta);
        exit (EXIT_SUCCESS);
#endif

        for (;;) {
                if (match_char ('\x1b') && match_char ('['))
                        process_escape_sequence ();
                else if (match_char (CTRL ('q'))) {
                        _out (ERASE_SCREEN, sizeof (ERASE_SCREEN));
                        set_cursor_position (1, 1);
                        break;
                } else {
                        char c = advance_char ();

                        if (iscntrl (c)) {
                                process_control_character (c);
                        } else {
                                if (!configuration.editor.filename) {
                                }

                                process_normal_character (c);
                        }
                }
        }
}

void parse_cmd_args (int argc, char **argv)
{
        if (argc > 1)
                configuration.editor.filename = argv[1];
        else
                configuration.editor.filename = NULL;

        init_editor ();
}

int main (int argc, char **argv)
{
        parse_cmd_args (argc, argv);
}
