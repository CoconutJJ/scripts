#include "cs50.h"
#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>

char caesar_encrypt (char c, int key)
{
        if (islower (c)) {
                c = 97 + (((c - 97) + key) % 26);
        } else if (isupper (c)) {
                c = 65 + (((c - 65) + key) % 26);
        }

        return c;
}

int main (int argc, char **argv)
{
        if (argc != 2) {
                fprintf (stderr, "Usage: ./caesar key\n");
                exit (EXIT_FAILURE);
        }

        char *end = NULL;

        long key = strtol (argv[1], &end, 10);

        if (*end != '\0') {
                fprintf (stderr, "Usage: ./caesar key\n");
                exit (EXIT_FAILURE);
        }

        char *text = get_string ("plaintext:  ");

        printf ("ciphertext: ");
        while (*text) {
                putchar (caesar_encrypt (*text++, key));
        }
}