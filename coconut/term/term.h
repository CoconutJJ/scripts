#ifndef term_h
#define term_h

#include <stdbool.h>
#include <termios.h>

struct termios _get_terminal_configuration ();
void reset_terminal ();
bool read_screen_dimensions (int *width, int *height);
void setup_terminal_for_editor ();


#endif