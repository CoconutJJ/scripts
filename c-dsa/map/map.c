#include "map.h"
#include <errno.h>
#include <stdarg.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define DEFAULT_MAP_SIZE           8
#define MAP_OPTION_ISSET(map, opt) ((map)->options & (1 << (opt)))

static char *map_error = NULL;

size_t map_djb2_hash (char *key)
{
        size_t hash = 5381;
        int c;
        while ((c = *key++))
                hash = ((hash << 5) + hash) + c; /* hash * 33 + c */

        return hash;
}

void map_set_error (char *error)
{
        map_error = error;
}

char *map_strerror ()
{
        return map_error;
}

void map_perror (char *prefix)
{
        if (!map_error) {
                fprintf (stderr, "map success");
                return;
        }

        fprintf (stderr, "%s: %s", prefix, map_error);
}

void *map_copy_value (Map *map, void *value)
{
        if (!MAP_OPTION_ISSET (map, MAP_VALUE_COPY))
                return value;

        void *copied = malloc (map->value_size);

        if (!copied) {
                map_set_error(strerror(errno));
                return NULL;
        }

        memcpy (copied, value, map->value_size);

        return copied;
}

char *map_copy_key (Map *map, char *key)
{
        if (!MAP_OPTION_ISSET (map, MAP_KEY_COPY))
                return key;

        char *copied = malloc (strlen (key) + 1);

        if (!copied) {
                map_set_error(strerror(errno));
                return NULL;
        }

        strcpy (copied, key);

        return copied;
}

void map_unlink_key (Map *map, char *key)
{
        if (MAP_OPTION_ISSET (map, MAP_KEY_COPY))
                free (key);
}

void map_unlink_value (Map *map, void *value)
{
        if (MAP_OPTION_ISSET (map, MAP_VALUE_COPY))
                free (value);
}

void map_init_entries (Map *map)
{
        MapEntry *entry;
        size_t pos = 0;
        while ((entry = map_entry_iter (map, &pos))) {
                entry->deleted = false;
                entry->key = NULL;
                entry->value = NULL;
        }
}

bool map_init (Map *map, MapHashMethod method)
{
        memset (map, 0, sizeof (Map));

        map->capacity = DEFAULT_MAP_SIZE;

        map->map = malloc (DEFAULT_MAP_SIZE * sizeof (MapEntry));

        if (!map->map) {
                map_error = strerror (errno);
                return false;
        }

        map_init_entries (map);

        switch (method) {
        case MAP_DJB2_HASH: map->hash = map_djb2_hash; break;

        default:
                map_set_error ("unknown hash method");
                return false;
                break;
        }
}

bool map_set_option (Map *map, MapOptions opt, ...)
{
        if (map->count != 0) {
                map_set_error ("cannot perform map_set_option on non-empty Map");
                return false;
        }

        map->options |= opt;

        va_list args;

        va_start (args, opt);

        switch (opt) {
        case MAP_VALUE_COPY: map->value_size = va_arg (args, size_t); break;
        }

        va_end (args);

        return true;
}

MapEntry *map_entry_iter (Map *map, size_t *pos)
{
        if (*pos >= map->capacity)
                return NULL;

        return map->map + (*pos)++;
}

MapEntry *map_live_entry_iter_loop (Map *map, size_t *pos)
{
        MapEntry *entry;

        size_t start_pos = *pos;

        while (1) {
                entry = map_entry_iter (map, pos);

                if (*pos == start_pos)
                        break;

                if (!entry) {
                        *pos = 0;
                        continue;
                }

                if (entry->deleted || !entry->key)
                        continue;

                return entry;
        }

        return NULL;
}

MapEntry *map_find_iter_loop (Map *map, size_t *pos)
{
        MapEntry *entry;
        size_t start_pos = *pos;
        while ((entry = map_entry_iter (map, pos))) {
                if (*pos == map->capacity)
                        *pos = 0;

                if (!entry->deleted && !entry->key)
                        return NULL;

                if (start_pos == *pos)
                        return NULL;

                if (entry->deleted)
                        continue;

                return entry;
        }
        return NULL;
}

size_t map_hash (Map *map, char *key)
{
        return map->hash (key) % map->capacity;
}

bool map_resize (Map *map)
{
        if (map->count < map->capacity / 4) {
                map->capacity /= 2;
        } else {
                map->capacity *= 2;
        }

        MapEntry *new_entries = malloc (map->capacity * sizeof (MapEntry));

        if (!new_entries) {
                map_set_error (strerror (errno));
                return false;
        }

        Map buf = { .map = new_entries, .capacity = map->capacity, .count = 0, .hash = map->hash };

        map_init_entries (&buf);

        MapEntry *entry;
        size_t pos = 0;

        while ((entry = map_live_entry_iter_loop (map, &pos))) {
                if (!map_add_entry (&buf, entry->key, entry->value)) {
                        map_set_error ("failed to resize map: could not add entry to new map");
                        return false;
                }
        }

        free (map->map);
        *map = buf;

        return true;
}

bool map_add_entry (Map *map, char *key, void *value)
{
        MapEntry *entry = map_find_entry (map, key);

        if (entry) {
                entry->value = value;
                return true;
        }

        if (map->count == map->capacity)
                map_resize (map);

        size_t start_pos = map_hash (map, key);
        size_t pos = start_pos;

        while ((entry = map_entry_iter (map, &pos))) {
                if (pos == map->capacity)
                        pos = 0;

                if (entry->deleted || !entry->key) {
                        entry->key = map_copy_key (map, key);
                        entry->value = map_copy_value (map, value);
                        entry->deleted = false;
                        map->count++;
                        return true;
                }

                if (pos == start_pos)
                        return false;
        }

        return false;
}

MapEntry *map_find_entry (Map *map, char *key)
{
        MapEntry *entry;
        size_t start_pos = map_hash (map, key);
        size_t pos = start_pos;

        while ((entry = map_find_iter_loop (map, &pos))) {
                if (pos == start_pos)
                        return NULL;

                if (strcmp (key, entry->key) == 0)
                        return entry;
        }

        return NULL;
}

bool map_delete_entry (Map *map, char *key)
{
        MapEntry *entry = map_find_entry (map, key);

        if (!entry)
                return false;

        map_unlink_key (map, entry->key);
        map_unlink_value (map, entry->value);

        entry->key = NULL;
        entry->value = NULL;
        entry->deleted = true;
        map->count--;

        if (map->count < map->capacity / 4)
                map_resize (map);

        return true;
}

size_t map_length(Map *map) {
        return map->count;
}
