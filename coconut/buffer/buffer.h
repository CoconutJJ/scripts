#ifndef buffer_h
#define buffer_h
#define WRITE_BUFFER_INIT (write_buffer){ NULL, 0, 0 };

#include <stdlib.h>

typedef struct write_buffer {
        size_t count;
        size_t size;
        char *buffer;
} write_buffer;
void buffer_alloc (write_buffer *buffer);
void buffer_resize (write_buffer *buffer, size_t new_size);
void buffer_write (write_buffer *buffer, char *data, size_t len);
void buffer_write_char_at (write_buffer *buffer, char c, size_t index);
void buffer_delete_char_at (write_buffer *buffer, size_t index);
void buffer_destroy (write_buffer *buffer);
void buffer_output (write_buffer *buffer);

#endif