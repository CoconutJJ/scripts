#include "cs50.h"
#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char substitution_encrypt (char c, char *key)
{
        return isupper (c) ? toupper (key[c - 65]) : (islower (c) ? tolower (key[c - 97]) : c);
}

void check_key (char *key)
{
        if (strlen (key) != 26) {
                fprintf (stderr, "Invalid key");
                exit (EXIT_FAILURE);
        }

        int letter_bitmap = 0;
        for (char *c = key; *c != '\0'; c++) {
                char curr = *c;
                if (!isalpha (curr)) {
                        fprintf (stderr, "Invalid key");
                        exit (EXIT_FAILURE);
                }

                if (isupper (curr))
                        curr -= 65;
                else if (islower (curr))
                        curr -= 97;

                if (letter_bitmap & (1 << curr)) {
                        fprintf (stderr, "Invalid key");
                        exit (EXIT_FAILURE);
                }

                letter_bitmap |= (1 << curr);
        }
}

int main (int argc, char **argv)
{
        if (argc != 2) {
                fprintf (stderr, "Usage: ./substitution key\n");
                exit (EXIT_FAILURE);
        }


        char *key = argv[1];

        check_key (key);

        printf ("plaintext:  ");

        int c, is_first = 1;
        while ((c = fgetc (stdin)) != '\n') {
                if (is_first) {
                        printf ("ciphertext: ");
                        is_first = 0;
                }

                putchar (substitution_encrypt (c, key));
        }
}
