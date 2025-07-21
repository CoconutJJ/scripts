#include <_stdio.h>
#include <stdbool.h>
#include <stdint.h>
#include <stdio.h>

#define MASK 0b111111000000000000000000

int read_octet_triple (uint32_t *tri)
{

        for (int i = 0; i < 3; i++) {
                int c = fgetc (stdin);

                if (c == EOF) {
                        *tri <<= 8 * (3 - i);

                        return i;
                }

                *tri <<= 8;
                *tri |= c;
        }

        return 3;
}

int main (int argc, char **argv)
{
        char *alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/";

        while (1) {
                uint32_t tri = 0;

                int bytes_encoded = read_octet_triple (&tri);

                if (bytes_encoded == 0)
                        break;

                for (int i = 0; i < 4; i++) {
                        int index = (tri & MASK) >> 18;
                        tri <<= 6;

                        if ((bytes_encoded == 1 && i >= 2) || (bytes_encoded == 2 && i >= 3)) {
                                putchar ('=');
                        } else {
                                putchar (alphabet[index]);
                        }
                }

                fflush(stdout);

                if (bytes_encoded < 3)
                        break;
        }
}