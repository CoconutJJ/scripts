#include "cs50.h"
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

bool read_credit_card_number (char *buffer)
{
        int i = 0;
        char c;
        bool valid = true;
        buffer[0] = '\0';
        while ((c = fgetc (stdin)) != EOF) {
                if ('0' <= c && c <= '9') {
                        buffer[i++] = c;
                        buffer[i] = '\0';
                } else {
                        switch (c) {
                        case '\n':
                        case '\r': goto out;

                        default: valid = false; break;
                        }
                }
        }

out:
        return valid;
}

int compute_digit_sum (int N)
{
        int sum = 0;
        while (N != 0) {
                sum += N % 10;
                N /= 10;
        }
        return sum;
}

int main (int argc, char **argv)
{
        char *card_number = get_string ("Number: ");

        int fst = 0, snd = 0, N = strlen (card_number), checksum = 0;

        for (int j = 0; j < N; j++) {
                int digit = card_number[j] - '0';

                checksum += (j % 2) ? digit : compute_digit_sum (digit * 2);
        }

        if (checksum % 10 != 0) {
                printf ("INVALID\n");
                exit (0);
        }

        switch (card_number[0]) {
        case '4': printf ("VISA\n"); break;
        case '3':
                switch (card_number[1]) {
                case '4':
                case '7': printf ("AMEX\n"); break;
                default: printf ("INVALID\n"); break;
                }
                break;
        case '5':
                switch (card_number[1]) {
                case '1':
                case '2':
                case '3':
                case '4':
                case '5': printf ("MASTERCARD\n"); break;

                default: printf ("INVALID\n"); break;
                }
                break;
        default: printf ("INVALID\n"); break;
        }
}
