#include "../coconut.h"
#include "../io/io.h"

extern editor_configuration configuration;

void cursor_enter ()
{
        set_cursor_position (configuration.editor.x,
                             configuration.editor.y + 1);
}



