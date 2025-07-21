#include <fcntl.h>
#include <stddef.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/fcntl.h>
#include <sys/mman.h>
#include <unistd.h>

#define N_NODES (1 << 13)

void *MEMORY_FILE = NULL;
size_t ALLOC_OFF = 0;

struct TrieNode {
        size_t child;
        size_t sibling;
        size_t data;
        char c;
};

void initialize_memory_file (char *filename)
{
        int fd = open (filename, O_RDWR | O_CREAT, 0600);
        if (fd < 0) {
                perror ("open");
                exit (EXIT_FAILURE);
        }

        ftruncate (fd, sizeof (struct TrieNode) * N_NODES);

        MEMORY_FILE = mmap (NULL, sizeof (struct TrieNode) * N_NODES, PROT_READ | PROT_WRITE, MAP_SHARED, fd, 0);
        
        if (!MEMORY_FILE) {
                perror ("mmap");
                exit (EXIT_FAILURE);
        }
}

void *allocate_data (size_t n)
{
        if (N_NODES * sizeof (struct TrieNode) - ALLOC_OFF < sizeof (struct TrieNode)) {
                printf ("No more memory\n");
                exit (EXIT_FAILURE);
        }

        void *data = (char *)MEMORY_FILE + ALLOC_OFF;
        ALLOC_OFF += n;
        return data;
}

struct TrieNode *allocate_node (char c)
{
        struct TrieNode *node = allocate_data (sizeof (struct TrieNode));

        node->data = 0;
        node->c = c;
        node->child = 0;
        node->sibling = 0;

        return node;
}

size_t node_address (struct TrieNode *node)
{
        return (char *)node - (char *)MEMORY_FILE;
}

struct TrieNode *get_node_by_address (size_t offset)
{
        return (struct TrieNode *)((char *)MEMORY_FILE + offset);
}

size_t data_address (void *data)
{
        return (char *)data - (char *)MEMORY_FILE;
}

void make_child (struct TrieNode *parent, struct TrieNode *child)
{
        parent->child = node_address (child);
}

void make_sibling (struct TrieNode *parent, struct TrieNode *sibling)
{
        parent->sibling = node_address (sibling);
}

struct TrieNode *insert_key (struct TrieNode *root, char *word)
{
        if (!*word)
                return root;

        if (!root) {
                root = allocate_node (*word);
                struct TrieNode *child = insert_key (NULL, word + 1);
                make_child (root, child);
                return root;
        }

        struct TrieNode *current = root;

        while (current->c != *word) {
                if (current->sibling != 0) {
                        current = get_node_by_address (current->sibling);
                        continue;
                }

                struct TrieNode *new_sibling = allocate_node (*word);
                make_sibling (current, new_sibling);
                current = new_sibling;
                break;
        }

        struct TrieNode *new_child =
                insert_key (current->child == 0 ? NULL : get_node_by_address (root->child), word + 1);

        make_child (current, new_child);

        return root;
}

int main (int argc, char **argv)
{
        FILE *unicode_text_file = fopen ("unicode.txt", "r");

        if (!unicode_text_file) {
                perror ("fopen");
                exit (EXIT_FAILURE);
        }

        initialize_memory_file ("unicode_latex.trie");

        struct TrieNode *root_node = NULL;

        char buffer[100];

        while (fgets (buffer, 100 - 1, unicode_text_file) != NULL) {
                char *tab = strchr (buffer, '\t');

                if (!tab)
                        break;

                *tab = '\0';

                root_node = insert_key (root_node, buffer);
        }

        printf ("%zu", ALLOC_OFF);

        return 0;
}
