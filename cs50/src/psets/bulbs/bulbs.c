#include <stdio.h>
#include <string.h>

const int BITS_IN_BYTE = 8;

int main (void)
{
        char c;
        printf ("Message: ");

        while ((c = fgetc (stdin)) != EOF) {
                if (c == '\n') {
                        printf ("Message: ");
                        continue;
                }

                for (int i = 0; i < BITS_IN_BYTE; i++) {
                        int bit = (c & (1 << (7 - i))) > 0;
                        printf (bit ? "\U0001F7E1" : "\U000026AB");
                }
                printf ("\n");
        }
}
