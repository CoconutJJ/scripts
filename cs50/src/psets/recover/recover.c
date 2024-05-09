#include <stdbool.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

bool check_jpeg_signature (uint8_t *buffer)
{
        if (buffer[0] != 0xff || buffer[1] != 0xd8 || buffer[2] != 0xff)
                return false;

        if ((buffer[3] & 0xf0) != 0xe0)
                return false;

        return true;
}

int main (int argc, char *argv[])
{
        if (argc < 2) {
                fprintf (stderr, "Expected image file.");
                return 1;
        }

        uint8_t buffer[512];

        FILE *image = fopen (argv[1], "rb");

        FILE *curr_image = NULL;

        int image_no = 0;

        while (fread (buffer, sizeof (buffer), 1, image) == 1) {
                if (check_jpeg_signature (buffer)) {
                        if (curr_image)
                                fclose (curr_image);

                        char filename[9] = { 0 };

                        sprintf (filename, "%03d.jpeg", image_no++);

                        curr_image = fopen (filename, "wb");

                        if (!curr_image) {
                                perror ("fopen");
                                return 1;
                        }
                }
                if (curr_image)
                        fwrite (buffer, 512, 1, curr_image);
        }

        if (curr_image)
                fclose (curr_image);

        fclose (image);

        return 0;
}