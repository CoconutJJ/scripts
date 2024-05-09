#include "cs50.h"
#include <math.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int get_grade (string s)
{
        int words = 1, letters = 0, sentences = 0;

        for (int i = 0, N = strlen (s); i < N; i++) {
                char c = s[i];

                switch (c) {
                case '.':
                case '?':
                case '!': sentences++; break;
                case ' ': words++; break;
                default:
                        if (('a' <= c && c <= 'z') || ('A' <= c && c <= 'Z'))
                                letters++;
                        break;
                }
        }

        double L = (letters * 100.0) / words, S = (sentences * 100.0) / words, index = 0.0588 * L - 0.296 * S - 15.8;

        printf ("%f\n", index);

        int grade = ((index - floor (index)) >= 0.5) ? (int)(ceil (index)) : (int)(floor (index));
        return grade;
}

int main (int argc, char **argv)
{
        int grade = get_grade (get_string ("Text: "));

        printf ("Grade: %d\n", grade);
}
