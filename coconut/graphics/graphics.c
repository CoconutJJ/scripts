#include "../coconut.h"
#include "../buffer/buffer.h"
#include "../io/io.h"

extern editor_configuration configuration;

void draw_splash_screen ()
{
#define TITLE_LEN 87

        char *title =
                "Coconut Editor (Ctrl-q to exit) -- Version 0.0.1 -- David Yue <davidyue5819@gmail.com>";

        int width = configuration.editor.width;
        int height = configuration.editor.height;

        int width_offset = (width - TITLE_LEN) / 2;
        int height_offset = (height - 1) / 2;

        set_cursor_position (width_offset, height_offset);

        _out (title, TITLE_LEN);

#undef TITLE_LEN
}

void draw_left_margin ()
{
        write_buffer buf = WRITE_BUFFER_INIT;

        for (int i = 0; i < configuration.editor.height; i++) {
                buffer_write (&buf, "~ \r\n", 4);
        }

        set_cursor_position (configuration.editor.left_margin, 1);

        _out (buf.buffer, buf.count);

        synchronize_cursor_position ();
}
