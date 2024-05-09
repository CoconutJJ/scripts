#ifndef editor_h
#define editor_h
#include "../buffer/buffer.h"

write_buffer *line_no (size_t n);
write_buffer *append_line ();
void write_line (write_buffer *line);
void scroll_up ();
void redraw ();
void scroll_down ();
void cursor_up ();
void cursor_down ();
void cursor_left ();
void cursor_right ();
void backspace ();
void enter ();
int get_cursor_col (int n);
void setup_editor ();
void clear_editor_screen ();
void write_char (char c);
#endif