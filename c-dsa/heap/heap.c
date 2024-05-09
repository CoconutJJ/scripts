
#include "heap.h"
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>

#define HEAP_DEFAULT_CAPACITY  8
#define LEFT_CHILD_INDEX(ind)  (2 * (ind) + 1)
#define RIGHT_CHILD_INDEX(ind) (2 * (ind) + 2)
#define PARENT_INDEX(ind)      (((ind)-1) / 2)

bool heap_init (Heap *heap)
{
        heap->capacity = HEAP_DEFAULT_CAPACITY;
        heap->count = 0;
        heap->heap = malloc (HEAP_DEFAULT_CAPACITY * sizeof (HeapElement));

        if (!heap->heap)
                return false;

        return true;
}

int heap_compare (HeapElement *a, HeapElement *b)
{
        if (a->priority < b->priority)
                return -1;

        if (a->priority == b->priority)
                return 0;

        if (a->priority > b->priority)
                return 1;

        __builtin_unreachable ();
}

void heap_swap (HeapElement *a, HeapElement *b)
{
        HeapElement temp;
        temp = *a;
        *a = *b;
        *b = temp;
}

void heap_percolate_up (Heap *heap, size_t index)
{
        while (index != 0) {
                size_t parent_idx = PARENT_INDEX (index);

                HeapElement *curr = heap->heap + index;
                HeapElement *parent = heap->heap + parent_idx;

                if (heap_compare (curr, parent) < 0)
                        heap_swap (curr, parent);
                else
                        break;

                index = parent_idx;
        }
}

void heap_percolate_down (Heap *heap, size_t index)
{
        while (index < heap->count) {
                HeapElement *curr = heap->heap + index;
                HeapElement *left = heap->heap + LEFT_CHILD_INDEX (index);
                HeapElement *right = heap->heap + RIGHT_CHILD_INDEX (index);

                if (LEFT_CHILD_INDEX (index) >= heap->count)
                        break;

                if (RIGHT_CHILD_INDEX (index) >= heap->count)
                        right = left;

                HeapElement *min =
                        heap_compare (left, right) < 0 ? left : right;
                HeapElement *max =
                        heap_compare (left, right) < 0 ? right : left;

                if (heap_compare (curr, min) < 0) {
                        heap_swap (curr, min);
                        index = min - heap->heap;
                } else if (heap_compare (curr, max) < 0) {
                        heap_swap (curr, max);
                        index = max - heap->heap;
                } else {
                        break;
                }
        }
}

bool heap_resize (Heap *heap)
{
        if (heap->count == heap->capacity) {
                heap->capacity *= 2;
        } else if (heap->count < heap->capacity / 4) {
                heap->capacity /= 2;
        } else {
                return true;
        }

        heap->heap =
                realloc (heap->heap, sizeof (HeapElement) * heap->capacity);

        if (!heap->heap)
                return false;

        return true;
}

bool heap_push (Heap *heap, void *elem, int priority)
{
        if (heap->count == heap->capacity)
                if (!heap_resize (heap))
                        return false;

        HeapElement *slot = heap->heap + (heap->count++ - 1);

        slot->elem = elem;
        slot->priority = priority;

        heap_percolate_up (heap, slot - heap->heap);

        return true;
}

bool heap_change_key (Heap *heap, void *elem, int new_priority)
{
        for (size_t i = 0; i < heap->count; i++) {

                HeapElement *slot = heap->heap + i;


                if (slot->elem != elem)
                        continue;
                
                if (slot->priority > new_priority) {
                        slot->priority = new_priority;
                        heap_percolate_down(heap, i);
                } else  {
                        slot->priority = new_priority;
                        heap_percolate_up(heap, i);
                }

                return true;
        }

        return false;
}

HeapElement heap_pop (Heap *heap)
{
        HeapElement *top = heap->heap;
        HeapElement *end = heap->heap + (heap->count-- - 1);

        HeapElement pop = *top;

        heap_swap (top, end);

        heap_percolate_down (heap, 0);

        return pop;
}
