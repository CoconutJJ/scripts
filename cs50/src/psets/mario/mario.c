#include "cs50.h"
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>

void putchar_repeated (char c, int N)
{
        while (N-- > 0)
                putchar (c);
}

int main (int argc, char **argv)
{
        int height = get_int ("Height: ");

        for (int level = 0; level < height; level++) {
                putchar_repeated (' ', height - (level + 1));
                putchar_repeated ('#', level + 1);
                putchar (' ');
                putchar (' ');
                putchar_repeated ('#', level + 1);
                putchar ('\n');
        }
}
