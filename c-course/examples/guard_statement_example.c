#include <stdio.h>
#include <stdlib.h>

int main (int argc, char **argv)
{
        FILE *fp = fopen ("data.txt", "r");

        if (fp) {
                char buf[10];
                if (fread (buf, 10, 1, fp) == 1) {
                
                        
                
                } else {
                        perror("fread");
                        return 1;
                }
        } else {
                perror("fopen");
                return 1;
        }

        return 0;
}
