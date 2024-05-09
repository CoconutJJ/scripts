#include "../term/term.h"
#include "../coconut.h"
#include "../io/io.h"
#include "../signal/signal.h"
#include <signal.h>
#include <stdbool.h>
#include <stdio.h>
#include <sys/ioctl.h>
#include <termios.h>
#include <unistd.h>

extern editor_configuration configuration;

void _set_terminal_configuration (struct termios *term)
{
        if (tcsetattr (STDIN_FILENO, TCSAFLUSH, term) == -1) {
                perror ("tcsetattr");
                exit (EXIT_FAILURE);
        }
}

void __set_raw_mode_flags (struct termios *term)
{
        term->c_iflag &= ~(BRKINT | ICRNL | INPCK | ISTRIP | IXON);
        term->c_oflag &= ~(OPOST);
        term->c_cflag |= (CS8);
        term->c_lflag &= ~(ECHO | ICANON | IEXTEN | ISIG);

        term->c_cc[VMIN] = 0;
        term->c_cc[VTIME] = 1;
}
void _enable_raw_mode ()
{
        // set the raw mode flags in the current terminal configuration
        __set_raw_mode_flags (&configuration.current_terminal_configuration);

        // raw mode is enabled after this call.
        _set_terminal_configuration (
                &configuration.current_terminal_configuration);
}

void _disable_raw_mode ()
{
        // restore original configuration
        _set_terminal_configuration (
                &configuration.original_terminal_configuration);
        configuration.current_terminal_configuration =
                configuration.original_terminal_configuration;
}
struct termios _get_terminal_configuration ()
{
        struct termios configuration;

        if (tcgetattr (STDIN_FILENO, &configuration) == -1) {
                perror ("tcgetattr");
                exit (EXIT_FAILURE);
        }

        return configuration;
}

void reset_terminal ()
{
        _disable_raw_mode ();
}

bool read_screen_dimensions (int *width, int *height)
{
        struct winsize sz;

        if (ioctl (STDIN_FILENO, TIOCGWINSZ, &sz) == -1) {
                perror ("ioctl");
                exit (EXIT_FAILURE);
        }

        *width = sz.ws_col;
        *height = sz.ws_row;

        return true;
}

void setup_terminal_for_editor ()
{
        // enter raw mode
        _enable_raw_mode ();

        // on program exit, disable raw mode so user doesn't end up with broken
        // terminal
        atexit (_disable_raw_mode);

        // erase the screen, set cursor to origin
        _out (ERASE_SCREEN, sizeof (ERASE_SCREEN));

        configuration.editor.row_offset = 1;

        read_screen_dimensions (&configuration.editor.width,
                                &configuration.editor.height);

        // if window size changes we should redraw the
        signal (SIGWINCH, _handle_window_size_change);
        signal (SIGSEGV, _handle_memory_error);
}
