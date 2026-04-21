#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

void extractBits (uint8_t *bytes, size_t len, size_t n_bits)
{
        uint32_t acc = 0;
        size_t acc_bits = 0;

        for (size_t i = 0; i < len; i++) {
                uint8_t b = bytes[i];

                acc <<= 8;
                acc |= b;
                acc_bits += 8;
                while (acc_bits >= n_bits) {
                        uint32_t mask = ((1 << acc_bits) - 1) & ~((1 << (acc_bits - n_bits)) - 1);
                        uint32_t val = (acc & mask) >> (acc_bits - n_bits);
                        acc_bits -= n_bits;

                        printf ("%u\n", val);
                }
        }
}

int main (int argc, char **argv)
{
        FILE *fp = fopen (argv[1], "rb");
}
