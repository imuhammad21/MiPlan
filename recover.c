#include <stdio.h>
#define RGBTRIPLEsize 3

int main(int argc, char *argv[])
{
    // ensure proper usage
    if (argc != 2)
    {
        fprintf(stderr, "Usage: ./recover forensic image\n");
        return 1;
    }
    // Name second command line argument forensic image
    char *forimage = argv[1];
    // Receive pointer adressing the foresnic image file
    FILE *inptr = fopen(forimage, "r");
    // Ensure forensic image can be opened for reading
    if (inptr == NULL)
    {
        fprintf(stderr, "Could not open %s.\n", forimage);
        return 2;
    }
    // Declare array in which to temporarily store bytes
    unsigned char buffer[512];
    fread(buffer, 1, 512, inptr);
    // Initialize number of jpg files to zero
    int jpegn = 0;
    // Declare array which can store name of each jpeg (max 8 characters)
    char filename[8];
    // Recieve the 'number' condition in the fread file pointer
    int result = fread(buffer, 1, 512, inptr);
    // Receive pointer adressing the file containing images
    FILE *outptr = fopen(filename, "w");
    // As long as not at EOF
    while (result == 512)
    {
        // If at the start of JPEG, close previous file
        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff)
        {
            fclose(outptr);
            sprintf(filename, "%03i.jpg", jpegn);
            jpegn++;
            if (outptr != NULL)
            {
                // Move outptr to a new location denoted by the next filename
                outptr = fopen(filename, "w");
                fwrite(buffer, result, 1, outptr);
            }
        }
        else
        {
            // If not at start of JPEG, write to the outfile
            if (outptr != NULL)
            {
                fwrite(buffer, result, 1, outptr);
            }
        }
        // Update result to see if reached EOF
        result = fread(buffer, 1, 512, inptr);
    }
    // When at EOF, close outpointer and exit program
    fclose(outptr);
    // success
    return 0;
}