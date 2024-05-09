#ifndef map_h
#define map_h

#include <stdbool.h>
#include <stdint.h>
#include <stdlib.h>

/**
 * Map Hash Function Pointer Type
 */
typedef size_t (*MapHashFn) (char *key);

/**
 * Type of hash methods
 */
typedef enum { MAP_DJB2_HASH } MapHashMethod;

/**
 * Map Options
 *
 */

typedef enum { MAP_KEY_COPY = 1, MAP_VALUE_COPY = 2 } MapOptions;

typedef struct {
        char *key;    /* Hash Key */
        void *value;  /* Pointer to hash value*/
        bool deleted; /* Deleted*/
} MapEntry;

typedef struct {
        MapEntry *map;   /* List of MapEntry */
        size_t capacity; /* List allocated size */
        size_t count;    /* List used size */
        MapHashFn hash;  /* Hash function */


        int32_t options; /* Hash Map Options */
        size_t value_size;

} Map;

/**
 * DJB2 String Hash method
 */
size_t map_djb2_hash (char *key);
void map_set_error (char *error);
void map_perror (char *prefix);
void map_init_entries (Map *map);
bool map_init (Map *map, MapHashMethod method);
MapEntry *map_entry_iter (Map *map, size_t *pos);
MapEntry *map_live_entry_iter_loop (Map *map, size_t *pos);
MapEntry *map_find_iter_loop (Map *map, size_t *pos);
size_t map_hash (Map *map, char *key);
bool map_resize (Map *map);
bool map_add_entry (Map *map, char *key, void *value);
MapEntry *map_find_entry (Map *map, char *key);
bool map_delete_entry (Map *map, char *key);
size_t map_length(Map *map);
#endif