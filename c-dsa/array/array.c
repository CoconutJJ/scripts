#include "array.h"
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

bool init_array (Array *array)
{
        array->capacity = 1;

        array->items = malloc (sizeof (ArrayItem));

        if (!array->items)
                return false;

        array->count = 0;

        return true;
}

bool array_resize (Array *array)
{
        if (array->count == array->capacity)
                array->capacity *= 2;
        else if (array->count < array->capacity / 4)
                array->capacity /= 2;
        else
                return true;

        void *ptr =
                realloc (array->items, array->capacity * sizeof (ArrayItem));

        if (!ptr)
                return false;

        array->items = ptr;

        return true;
}

bool array_append (Array *array, void *item)
{
        if (!array_resize (array))
                return false;

        array->items[array->count++].item = item;
}

bool array_prepend (Array *array, void *item)
{
        if (!array_resize (array))
                return false;

        memmove (array->items + 1,
                 array->items,
                 array->count * sizeof (ArrayItem));

        array->items[0].item = item;

        array->count++;

        return true;
}

void *array_get_item (Array *array, size_t index)
{
        if (index >= array->count)
                return NULL;

        return array->items[index].item;
}