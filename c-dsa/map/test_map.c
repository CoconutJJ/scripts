#include <stdio.h>
#include <stdlib.h>
#include "map.h"

void fail(char *message) {
        fprintf(stderr, "FAIL: %s", message);
}

void assert_map_find(Map *m, char *key) {
        
        MapEntry *map = map_find_entry(&m, key);

        if (!map) {
                fprintf(stderr, "");
        }

}

int main (int argc, char **argv)
{
        Map m;

        map_init(&m, MAP_DJB2_HASH);
        
        char *s = "hello";
        char *k = "bye";
        int p = 9;

        if (!map_add_entry(&m, s, &p)) {
                map_perror("map");
        }

        if (!map_add_entry(&m, k, &p)) {
                map_perror("map");
        }

        MapEntry *entry = map_find_entry(&m, k);

        if (entry) {

                printf("%s\n", entry->key);

        }

        if (map_delete_entry(&m, k)) {
                printf("deleted\n");
        }

        entry = map_find_entry(&m, k);

        if (!entry) {
                printf("success!");
        }
        entry = map_find_entry(&m, s);

        if (entry) {
                printf("success!");
        }
}