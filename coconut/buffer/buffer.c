#include "./buffer.h"
#include "../io/io.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

void buffer_alloc (write_buffer *buffer)
{
        buffer->buffer = NULL;
        buffer->count = 0;
        buffer->size = 0;
        buffer_resize (buffer, 8);
}

void buffer_resize (write_buffer *buffer, size_t new_size)
{
        buffer->buffer = realloc (buffer->buffer, new_size);

        if (!buffer->buffer) {
                perror ("realloc");
                exit (EXIT_FAILURE);
        }
        buffer->size = new_size;
        buffer->count = buffer->count <= new_size ? buffer->count : new_size;
}

static void buffer_auto_resize (write_buffer *buffer, size_t min_free_space)
{
        if (buffer->size <= buffer->count + min_free_space) {
                if (buffer->size == 0)
                        buffer->size = min_free_space;
                else
                        while (buffer->size <= buffer->count + min_free_space)
                                buffer->size *= 2;

                buffer_resize (buffer, buffer->size);
        } else if (buffer->count + min_free_space < buffer->size / 4) {
                buffer->size /= 4;
                buffer_resize (buffer, buffer->size);
        }
}

void buffer_write (write_buffer *buffer, char *data, size_t len)
{
        buffer_auto_resize (buffer, len);

        memcpy (buffer->buffer + buffer->count, data, len);
        buffer->count += len;
}

void buffer_write_char_at (write_buffer *buffer, char c, size_t index)
{
        buffer_auto_resize (buffer, 1);

        char *remaining = buffer->buffer + index;

        memmove (remaining + 1, remaining, buffer->count - index);

        *remaining = c;
        buffer->count++;
}

void buffer_delete_char_at (write_buffer *buffer, size_t index)
{
        if (index >= buffer->count)
                return;

        char *del = buffer->buffer + index;

        memmove (del, del + 1, buffer->count - index - 1);

        buffer->count--;
}

void buffer_destroy (write_buffer *buffer)
{
        free (buffer->buffer);
        buffer->buffer = NULL;
        buffer->count = 0;
        buffer->size = 0;
}

void buffer_output (write_buffer *buffer)
{
        _out (buffer->buffer, buffer->count);
}
