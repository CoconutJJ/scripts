#ifndef coconut_h
#define coconut_h

#include "buffer/buffer.h"
#include <stdlib.h>
#include <termios.h>
#include <stdbool.h>

#define ESC_BUFFER_SIZE 32

typedef struct editor_configuration {
        struct termios original_terminal_configuration;
        struct termios current_terminal_configuration;

        struct {
                char c;
                bool _should_read;
        } in;

        struct {
                char *filename;
                int x;
                int y;
                int row_offset;
                int width;
                int height;
                int left_margin;
                int last_col;
        } editor;

        write_buffer *lines;
        size_t line_count;
        size_t line_size;

} editor_configuration;

#endif