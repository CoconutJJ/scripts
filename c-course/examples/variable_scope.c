#include <stdio.h>
#include <stdlib.h>

int main(int argc, char **argv) {

        double temperature = 24;

        if (temperature > 22) {

                double temp_diff = temperature - 22;

                printf("It is above room temperature by %lf degrees", temp_diff);

        }

        printf("temp_diff = %lf", temp_diff);

}
