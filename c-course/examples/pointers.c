#include <stdio.h>
#include <stdlib.h>

void lie(int *age) {

        *age = 12;

}

int main(int argc, char **argv) {

        
        int myAge = 12;

        lie(&myAge);


}