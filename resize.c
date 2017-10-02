#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "bmp.h"
#define RGBTRIPLEsize 3

int main(int argc, char *argv[])
{
    // Ensure proper usage
    if (argc != 4)
    {
        fprintf(stderr, "Usage: scale-factor infile outfile\n");
        return 1;
    }
    int sclfactor = atoi(argv[1]);
    if (sclfactor < 0 || sclfactor > 100)
    {
        printf("First command line argument must be positive int ≤ 100");
        return 1;
    }
    // Remember filenames
    char *infile = argv[2];
    char *outfile = argv[3];
    // Open input file
    FILE *inptr = fopen(infile, "r");
    // Ensure pointer is not null pointer
    if (inptr == NULL)
    {
        fprintf(stderr, "Could not open %s.\n", infile);
        return 2;
    }
    // Open output file
    FILE *outptr = fopen(outfile, "w");
    // Ensure pointer is not null pointer
    if (outptr == NULL)
    {
        fclose(inptr);
        fprintf(stderr, "Could not create %s.\n", outfile);
        return 3;
    }
    // Read infile's BITMAPFILEHEADER
    BITMAPFILEHEADER bf;
    fread(&bf, sizeof(BITMAPFILEHEADER), 1, inptr);
    // Read infile's BITMAPINFOHEADER
    BITMAPINFOHEADER bi;
    fread(&bi, sizeof(BITMAPINFOHEADER), 1, inptr);
    // Ensure infile is (likely) a 24-bit uncompressed BMP 4.0
    if (bf.bfType != 0x4d42 || bf.bfOffBits != 54 || bi.biSize != 40 ||
        bi.biBitCount != 24 || bi.biCompression != 0)
    {
        fclose(outptr);
        fclose(inptr);
        fprintf(stderr, "Unsupported file format.\n");
        return 4;
    }
    int ipadding = (4 - (bi.biWidth * RGBTRIPLEsize) % 4) % 4;
    int opadding = (4 - ((bi.biWidth * sclfactor) * RGBTRIPLEsize) % 4) % 4;
    int oldwidth = bi.biWidth;
    int oldheight = bi.biHeight;
    // Define biWidth and biHeight in terms of scaled image
    bi.biWidth *= sclfactor;
    bi.biHeight *= sclfactor;
    // Write outfile's BITMAPINFOHEADER
    bi.biSizeImage = ((RGBTRIPLEsize * bi.biWidth) + opadding) * abs(bi.biHeight);
    // Write outfile's BITMAPFILEHEADER
    bf.bfSize = bi.biSizeImage + sizeof(BITMAPFILEHEADER) + sizeof(BITMAPINFOHEADER);
    fwrite(&bf, sizeof(BITMAPFILEHEADER), 1, outptr);
    fwrite(&bi, sizeof(BITMAPINFOHEADER), 1, outptr);
    // Iterate over infile's scanlines
    for (int i = 0, biHeight = abs(oldheight); i < biHeight; i++)
    {
        for (int l = 0; l < sclfactor; l++)
        {
            // Iterate over pixels in scanline
            for (int j = 0; j < oldwidth; j++)
            {
                // Temporary storage
                RGBTRIPLE triple;
                // Read RGB triple from infile
                fread(&triple, RGBTRIPLEsize, 1, inptr);
                for (int k = 0; k < sclfactor; k++)
                    {
                        // Write RGB triple to outfile
                        fwrite(&triple, RGBTRIPLEsize, 1, outptr);
                    }
            // Add padding to outfile
            }
            for (int k = 0; k < opadding; k++)
            {
                fputc(0x00, outptr);
            }
            // Move cursor back to start of current scanline in infile to copy row
            fseek(inptr, -((oldwidth)*RGBTRIPLEsize), SEEK_CUR);
        }
        // Skip over infile padding to begin scanning subsequent row in infile
        fseek(inptr, ipadding + ((oldwidth)*RGBTRIPLEsize), SEEK_CUR);
    }
    // Close infile
    fclose(inptr);
    // Close outfile
    fclose(outptr);
    // Success
    return 0;
}
