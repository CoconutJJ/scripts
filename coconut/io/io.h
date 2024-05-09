#ifndef io_h
#define io_h

#include <stdlib.h>
#include <stdbool.h>

#define ESC(x)                   "\x1b[" x
#define ERASE_SCREEN             ESC ("2J")
#define ERASE_FROM_CURSOR_TO_EOL ESC ("0K")
#define REQUEST_CURSOR_POS       ESC ("6n")
#define CURSOR_POS(y, x)         ESC (y ";" x "H")
#define CURSOR_UP(n)             ESC (#n "A")
#define CURSOR_DOWN(n)           ESC (#n "B")
#define CURSOR_RIGHT(n)          ESC (#n "C")
#define CURSOR_LEFT(n)           ESC (#n "D")

typedef enum key_control_code {
        ARROW_UP = 'A',
        ARROW_DOWN = 'B',
        ARROW_RIGHT = 'C',
        ARROW_LEFT = 'D',
        BACKSPACE = 127,
        ENTER = 13
} key_control_code;

void _out (char *buffer, size_t len);
char read_char ();
char advance_char ();
bool has_char ();
bool match_char (char c);
void synchronize_cursor_position ();
void set_cursor_position (int x, int y);
bool read_cursor_position (int *line, int *col);
#endif