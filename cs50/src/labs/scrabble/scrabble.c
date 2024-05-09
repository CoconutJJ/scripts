#include "cs50.h"
#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
// Points assigned to each letter of the alphabet
int POINTS[] = { 1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10 };

int get_char_point (char c)
{
        if (isupper (c))
                c -= 32;

        c -= 65;

        return POINTS[(int)c];
}

int compute_score (char *word)
{
        int sum = 0;
        while (*word)
                sum += get_char_point (*word++);

        return sum;
}

int main (void)
{
        // Get input words from both players
        char *word1 = get_string ("Player 1: ");
        char *word2 = get_string ("Player 2: ");

        // Score both words
        int score1 = compute_score (word1);
        int score2 = compute_score (word2);

        if (score1 == score2) {
        }

        printf (score1 > score2 ? "Player 1 wins!\n" : (score1 == score2 ? "Tie" : "Player 2 wins!\n"));
}
