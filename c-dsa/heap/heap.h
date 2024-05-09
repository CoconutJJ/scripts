#ifndef heap_h
#define heap_h

#include <stdlib.h>

typedef struct {
    void *elem;
    int priority;
} HeapElement;


typedef struct {

    HeapElement *heap;
    size_t capacity;
    size_t count;

} Heap;



#endif