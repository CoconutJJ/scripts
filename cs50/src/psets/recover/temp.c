#include <stdlib.h>
#include <stdio.h>
#include <string.h>
int main (int argc, char **argv)
{
        printf ("%lu \n", strlen (argv[1]));
        // Creating the buffer.
        unsigned char *buffer = malloc (512);
        if (buffer == NULL) {
                printf ("Memmory not allocated!\n");
        } else {
                printf ("Memory allocated!\n");
        }
        // REMANING CODE
        // The file name.
        char file[9];
        strcpy (file, argv[1]);
        printf ("%s \n", argv[1]);
        // Is the file open?
        int is_open = 1;
        // Open the raw file
        FILE *f = fopen (argv[1], "r");
        if (f == NULL) {
                printf ("file pointer Not Open!\n");
        } else {
                printf (" file pointer Open!\n");
        }
        perror ("fopen");
        is_open = 0;
        // while loop to do the code until the end of the file.
        int c = 0;
        // Read the file.
        int n = fread (buffer, 512, 1, f);
        // Create variables to store the image.
        FILE *img = NULL;
        int w = 0;
        while (n > 0) {
                // Checking for the first four bytes.
                if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] & 0xf0) == 0xe0) {
                        // Update the counter variable.
                        c++;
                        if (is_open == 0) {
                                // Naming the new file correctly.
                                sprintf (file, "%03i.jpg", c);
                                // Closing the file.
                                fclose (img);
                                // Opening the file to write the recoverd JPEG.
                                img = fopen (file, "w");
                                if (img == NULL) {
                                        printf ("Image pointer not open!\n");
                                } else {
                                        printf ("Image pointer open!\n");
                                }
                                // Updating the is_open variable.
                                is_open = 1;
                                // Writing the JPEG file.
                                for (int i = 0; i < n; i++) {
                                        // Writing the ne JPEG.
                                        w = fwrite (buffer, 512, 1, img);
                                        if (w != 1) {
                                                // Handle error.
                                                printf ("ERROR!");
                                        }
                                }
                        }
                }
                n = fread (buffer, 512, 50, f);
        }
        // Freeing the memory.
        free (buffer);
        printf ("%lu \n", strlen (argv[1]));
        // Creating the buffer.
        unsigned char *buffer = malloc (512);
        if (buffer == NULL) {
                printf ("Memmory not allocated!\n");
        } else {
                printf ("Memory allocated!\n");
        }
        // REMANING CODE
        // The file name.
        char file[9];
        strcpy (file, argv[1]);
        printf ("%s \n", argv[1]);
        // Is the file open?
        int is_open = 1;
        // Open the raw file
        FILE *f = fopen (argv[1], "r");
        if (f == NULL) {
                printf ("file pointer Not Open!\n");
        } else {
                printf (" file pointer Open!\n");
        }
        perror ("fopen");
        is_open = 0;
        // while loop to do the code until the end of the file.
        int c = 0;
        // Read the file.
        int n = fread (buffer, 512, 1, f);
        // Create variables to store the image.
        FILE *img = NULL;
        int w = 0;
        while (n > 0) {
                // Checking for the first four bytes.
                if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] & 0xf0) == 0xe0) {
                        // Update the counter variable.
                        c++;
                        if (is_open == 0) {
                                // Naming the new file correctly.
                                sprintf (file, "%03i.jpg", c);
                                // Closing the file.
                                fclose (img);
                                // Opening the file to write the recoverd JPEG.
                                img = fopen (file, "w");
                                if (img == NULL) {
                                        printf ("Image pointer not open!\n");
                                } else {
                                        printf ("Image pointer open!\n");
                                }
                                // Updating the is_open variable.
                                is_open = 1;
                                // Writing the JPEG file.
                                for (int i = 0; i < n; i++) {
                                        // Writing the ne JPEG.
                                        w = fwrite (buffer, 512, 1, img);
                                        if (w != 1) {
                                                // Handle error.
                                                printf ("ERROR!");
                                        }
                                }
                        }
                }
                n = fread (buffer, 512, 50, f);
        }
        // Freeing the memory.
        free (buffer);
}