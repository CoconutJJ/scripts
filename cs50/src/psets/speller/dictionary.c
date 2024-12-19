// Implements a dictionary's functionality

#include "dictionary.h"
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
node *table[N];

// Returns true if word is in dictionary, else false
bool check (const char *word)
{
        unsigned int h = hash (word) % N;

        node *bucket = table[h];

        for (; bucket != NULL; bucket = bucket->next) {
                if (strcmp (bucket->word, word) == 0) {
                        return true;
                }
        }

        return false;
}

// Hashes word to a number
unsigned int hash (const char *word)
{
        // TODO: Improve this hash function
        return toupper (word[0]) - 'A';
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
        return false;
}
