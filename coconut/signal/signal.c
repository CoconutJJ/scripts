#include <stdlib.h>
#include <signal.h>
#include <stdio.h>
#include "../io/io.h"
#include "../coconut.h"
#include "../term/term.h"

extern editor_configuration configuration;

void _handle_window_size_change (int signal)
{
        int width, height;

        if (!read_screen_dimensions (&width, &height)) {
                fprintf (
                        stderr,
                        "Detected screen dimension change: Could not read new screen dimensions!");
                exit (EXIT_FAILURE);
        }

        configuration.editor.width = width;
        configuration.editor.height = height;

        synchronize_cursor_position ();
}

void _handle_memory_error (int sig)
{
        /**
         * If we run into a fatal error, such as a Segmentation fault,
         * let us disable raw mode, so terminal is restored back to normal
         * state.
         *
         * But first we must restore this signal back to it's default action, so
         * in case we screw ourselves up even more and this signal is raised
         * again during the execution of our current handler we don't fall into
         * a loop.
         */

        signal (sig, SIG_DFL);

        reset_terminal ();

        /**
         * We do not take any recovery actions to try and restore program state
         * pre-signal, just signal ourselves with the same signal and execute
         * the default handler.
         *
         * This is done instead of exit() as it helps with error reporting.
         */
        if (raise (sig) != 0)
                exit (EXIT_FAILURE);
}

