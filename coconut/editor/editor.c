#include "editor.h"
#include "../buffer/buffer.h"
#include "../coconut.h"
#include "../graphics/graphics.h"
#include "../io/io.h"
#include <stdio.h>
#include <string.h>

extern editor_configuration configuration;

void resize_lines_if_full ()
{
        if (configuration.line_count < configuration.line_size)
                return;

        if (configuration.line_size == 0)
                configuration.line_size++;
        else
                configuration.line_size *= 2;

        configuration.lines =
                realloc (configuration.lines,
                         configuration.line_size * sizeof (write_buffer));

        if (!configuration.lines) {
                perror ("realloc");
                exit (EXIT_FAILURE);
        }
}

write_buffer *line_no (size_t n)
{
        if (n > configuration.line_count)
                return NULL;

        return configuration.lines + n - 1;
}

write_buffer *add_line_at (size_t line)
{
        resize_lines_if_full ();

        size_t index = line - 1;
        write_buffer *line_buf = configuration.lines + index;

        if (index < configuration.line_count)
                memmove (line_buf + 1,
                         line_buf,
                         (configuration.line_count - index) *
                                 sizeof (write_buffer));

        buffer_alloc (line_buf);
        configuration.line_count++;

        return line_buf;
}

write_buffer *del_line_at (size_t line)
{
        size_t index = line - 1;

        write_buffer *line_buf = configuration.lines + index;
        buffer_destroy (line_buf);
        memmove (line_buf,
                 line_buf + 1,
                 (configuration.line_count - index - 1) *
                         sizeof (write_buffer));

        configuration.line_count--;
        return line_buf;
}

write_buffer *append_line ()
{
        resize_lines_if_full ();

        write_buffer *new_line = configuration.lines + configuration.line_count;

        buffer_alloc (new_line);
        configuration.line_count++;

        return new_line;
}

int get_cursor_col (int n)
{
        write_buffer *line = line_no (n);

        int col = line->count + 2;

        if (configuration.editor.last_col < col) {
                return configuration.editor.last_col;
        } else {
                return col < 3 ? 3 : col;
        }
}

void write_line (write_buffer *line)
{
        _out (ERASE_FROM_CURSOR_TO_EOL, sizeof (ERASE_FROM_CURSOR_TO_EOL));
        _out (line->buffer, line->count);
}

void write_char (char c)
{
        int n = configuration.editor.y + configuration.editor.row_offset - 1;
        int col = configuration.editor.x - 3;

        write_buffer *line = line_no (n);

        if (!line)
                line = append_line ();

        buffer_write_char_at (line, c, col);

        set_cursor_position (3, configuration.editor.y);

        _out (ERASE_FROM_CURSOR_TO_EOL, sizeof (ERASE_FROM_CURSOR_TO_EOL));
        _out (line->buffer, line->count);

        configuration.editor.x++;

        synchronize_cursor_position ();
}

void redraw ()
{
        for (int n = configuration.editor.row_offset;
             n < configuration.editor.row_offset + configuration.editor.height;
             n++) {
                write_buffer *line = line_no (n);

                if (!line)
                        break;

                set_cursor_position (configuration.editor.left_margin,
                                     n - configuration.editor.row_offset + 1);

                write_line (line);
        }

        synchronize_cursor_position ();
}

void clear_editor_screen ()
{
        _out (ERASE_SCREEN, sizeof (ERASE_SCREEN));
        draw_left_margin ();
}

void rewrite_lines ()
{
        for (size_t i = 0; i < configuration.line_size; i++) {
                set_cursor_position (3, i + 1);

                if (i < configuration.line_count) {
                        write_line (configuration.lines + i);
                } else {
                        set_cursor_position (3, i + 1);
                        _out (ERASE_FROM_CURSOR_TO_EOL,
                              sizeof (ERASE_FROM_CURSOR_TO_EOL));
                }
        }
        synchronize_cursor_position ();
}
void scroll_up ()
{
        configuration.editor.row_offset -= 1;

        if (configuration.editor.row_offset != 0) {
                redraw ();
        } else {
                configuration.editor.row_offset = 1;
        }
}

void scroll_down ()
{
        configuration.editor.row_offset += 1;

        if (configuration.editor.row_offset <=
            configuration.line_count - configuration.editor.height + 1) {
                redraw ();
        } else {
                configuration.editor.row_offset -= 1;
        }
}

void cursor_up ()
{
        int y = configuration.editor.y;
        int new_x, new_y;

        new_y = y - 1;
        int line = new_y + configuration.editor.row_offset - 1;

        if (new_y < 1) {
                scroll_up ();
                new_y = 1;
                return;
        }

        new_x = get_cursor_col (line);

        set_cursor_position (new_x, new_y);

        configuration.editor.x = new_x;
        configuration.editor.y = new_y;
        synchronize_cursor_position ();
}

void cursor_down ()
{
        int y = configuration.editor.y;
        int new_x, new_y;

        new_y = y + 1;

        int line = new_y + configuration.editor.row_offset - 1;

        if (line > configuration.line_count)
                return;

        if (new_y > configuration.editor.height) {
                scroll_down ();
                new_y = configuration.editor.height;
        }

        new_x = get_cursor_col (line);

        set_cursor_position (new_x, new_y);

        configuration.editor.x = new_x;
        configuration.editor.y = new_y;
        synchronize_cursor_position ();
}

void cursor_left ()
{
        int x = configuration.editor.x, y = configuration.editor.y;

        int new_x = x - 1, new_y = y;

        if (new_x < 3) {
                cursor_up ();
                return;
        }

        configuration.editor.last_col = new_x;

        set_cursor_position (new_x, new_y);

        configuration.editor.x = new_x;
        configuration.editor.y = new_y;

        synchronize_cursor_position ();
}

void cursor_right ()
{
        int x = configuration.editor.x, y = configuration.editor.y;

        int new_x = x + 1, new_y = y;

        int n = configuration.editor.row_offset + y - 1;

        if (n > configuration.line_count)
                return;

        int max_col = line_no (n)->count;

        if (new_x > max_col + 3) {
                configuration.editor.last_col =
                        configuration.editor.left_margin;
                cursor_down ();
                return;
        }

        configuration.editor.last_col = new_x;

        configuration.editor.x = new_x;
        configuration.editor.y = new_y;

        synchronize_cursor_position ();
}

void backspace ()
{
        int x = configuration.editor.x, y = configuration.editor.y;

        int n = y + configuration.editor.row_offset - 1;

        int del_index = (x - 1) - 3;

        write_buffer *line = line_no (n);

        if (!line)
                return;

        if (del_index <= 0) {
                write_buffer *prev_line = line_no (n - 1);

                if (!prev_line)
                        return;

                int prev_x = prev_line->count + 3;

                buffer_write (prev_line, line->buffer, line->count);

                memmove (line,
                         line + 1,
                         (configuration.line_count - n) *
                                 sizeof (write_buffer));

                configuration.line_count--;
                configuration.editor.x = prev_x;
                configuration.editor.y = y - 1;
        } else {
                buffer_delete_char_at (line, del_index);
                configuration.editor.x--;
        }
        rewrite_lines ();
        synchronize_cursor_position ();
}

void enter ()
{
        int x = configuration.editor.x, y = configuration.editor.y;

        int index = x - 4;

        write_buffer *line = line_no (y);

        if (!line)
                line = append_line ();

        char *start = line->buffer + index;

        size_t nbytes = line->count - index - 1;

        write_buffer *next_line = add_line_at (y + 1);

        buffer_write (next_line, start + 1, nbytes);

        line->count -= nbytes;

        rewrite_lines ();

        configuration.editor.y = y + 1;
        configuration.editor.x = 3;

        synchronize_cursor_position ();
}

void setup_editor ()
{
        draw_left_margin ();

        draw_splash_screen ();

        configuration.editor.x = configuration.editor.left_margin;
        configuration.editor.y = 1;
        synchronize_cursor_position ();
}