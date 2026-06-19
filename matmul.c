#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define N 128

int main (int argc, char **argv)
{
        double A[N][N], B[N][N], C[N][N];

        srand (time (NULL));

        for (int i = 0; i < N; i++)
                for (int j = 0; j < N; j++) {
                        A[i][j] = (double)rand () / RAND_MAX;
                        B[i][j] = (double)rand () / RAND_MAX;
                }
        
#pragma omp parallel for
        for (int i = 0; i < N; i++)
                for (int k = 0; k < N; k++)
                        for (int j = 0; j < N; j++)
                                C[i][j] += A[i][k] * B[k][j];

        
}
