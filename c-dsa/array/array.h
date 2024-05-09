#ifndef array_h
#define array_h

#include <stdlib.h>

typedef struct {
        void *item;
} ArrayItem;

typedef struct {

        ArrayItem *items;
        size_t count;
        size_t capacity;
        
} Array;

#endif