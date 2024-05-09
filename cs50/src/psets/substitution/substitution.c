#include "cs50.h"
#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char substitution_encrypt (char c, char *key)
{
        return isupper (c) ? toupper (key[c - 65]) : (islower (c) ? tolower (key[c - 97]) : c);
}

int main (int argc, char **argv)
{
        if (argc != 2) {
                fprintf (stderr, "Usage: ./substitution key\n");
                exit (EXIT_FAILURE);
        }

        char *key = argv[1];

        if (strlen (key) != 26) {
                fprintf (stderr, "Key must contain 26 characters.\n");
                exit (EXIT_FAILURE);
        }

        char *text = get_string ("plaintext:  ");

        printf ("ciphertext: ");
        while (*text) {
                putchar (substitution_encrypt (*text++, key));
        }
}
