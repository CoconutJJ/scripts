// Implements a dictionary's functionality

#include "dictionary.h"
#include <_string.h>
#include <assert.h>
#include <ctype.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Represents a node in a hash table
typedef struct node {
        char word[LENGTH + 1];
        struct node *next;
} node;

// TODO: Choose number of buckets in hash table
const unsigned int N = 26;

static size_t dict_size = 0;

// Hash table
node *table[N] = { 0 };

// Returns true if word is in dictionary, else false
bool check (const char *word)
{
        char *word_copy = strdup(word), *current = word_copy;

        while (*current) {
                *current = tolower(*current);
                current++;
        }

        unsigned int h = hash (word_copy) % N;

        node *bucket = table[h];

        for (; bucket != NULL; bucket = bucket->next) {
                if (strcmp (bucket->word, word_copy) == 0) {
                        free(word_copy);
                        return true;
                }
        }

        free(word_copy);

        return false;
}

// Hashes word to a number
unsigned int hash (const char *word)
{

        unsigned long hash = 5381;
        int c;

        while (c = *word++)
                hash = ((hash << 5) + hash) + c; /* hash * 33 + c */

        return hash;
}

node *create_node (const char *word)
{
        if (strlen (word) > LENGTH) {
                fprintf (stderr, "error: word length exceeds maximum of %d characters", LENGTH);
                exit (EXIT_FAILURE);
        }

        node *new_node = malloc (sizeof (node));

        if (!new_node) {
                perror ("malloc");
                exit (EXIT_FAILURE);
        }

        strcpy (new_node->word, word);

        new_node->next = NULL;

        return new_node;
}

void insert_word (const char *word)
{
        node *word_node = create_node (word);

        unsigned int h = hash (word) % N;

        node *bucket = table[h];

        if (!bucket) {
                table[h] = word_node;
                return;
        }

        while (bucket->next)
                bucket = bucket->next;

        bucket->next = word_node;

        dict_size++;
}

// Loads dictionary into memory, returning true if successful, else false
bool load (const char *dictionary)
{
        char word_buf[LENGTH + 1];

        FILE *dict_fp = fopen (dictionary, "r");

        if (!dict_fp) {
                perror ("fopen");
                return false;
        }

        while (fgets (word_buf, LENGTH + 1, dict_fp) != NULL) {
                char *newline = strchr (word_buf, '\n');
                char *carriage_return = strchr (word_buf, '\n');

                if (newline)
                        *newline = '\0';
                if (carriage_return)
                        *carriage_return = '\0';

                insert_word (word_buf);
        }

        return true;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size (void)
{
        return dict_size;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload (void)
{
        for (int i = 0; i < N; i++) {
                node *current = table[i];
                while (current) {
                        node *next = current->next;

                        free (current);

                        current = next;
                }
        }

        return true;
}
