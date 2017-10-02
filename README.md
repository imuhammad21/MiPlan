# Questions

## What's `stdint.h`?

Stdint.h is the library that bmp.h needs to run

## What's the point of using `uint8_t`, `uint32_t`, `int32_t`, and `uint16_t` in a program?

These allow one to specify the different sizes of the types to be used.

## How many bytes is a `BYTE`, a `DWORD`, a `LONG`, and a `WORD`, respectively?

A byte, dword, long, and word are 1, 4, 4, and 2 bytes, respectively.

## What (in ASCII, decimal, or hexadecimal) must the first two bytes of any BMP file be? Leading bytes used to identify file formats (with high probability) are generally called "magic numbers."

42 4d must be the first bytes of any bmp file.

## What's the difference between `bfSize` and `biSize`?

biSize is the number of bytes required by the structure, while bfSize is the size, in bytes, of the bitmap file.

## What does it mean if `biHeight` is negative?

If biHeight is negative, the bitmap is a top-down DIB and its origin is the upper-left corner.

## What field in `BITMAPINFOHEADER` specifies the BMP's color depth (i.e., bits per pixel)?

biBitCount specifies the BMP's number of bits per pixel, or the color depth.

## Why might `fopen` return `NULL` in lines 24 and 32 of `copy.c`?

fopen will return NULL if argv[1] doesn't exist.

## Why is the third argument to `fread` always `1` in our code?

The third argument in fread refers to the quantity of the unit of information we are reading, which is always 1.

## What value does line 65 of `copy.c` assign to `padding` if `bi.biWidth` is `3`?

Line 65 of 'copy.c' would assign '3' to padding if 'bi.biwidth' is '3'.

## What does `fseek` do?

fseek allows one to rewind or fast-forward through a file, or in other words, change the position of the cursor in a file.

## What is `SEEK_CUR`?

SEEK_CUR has the ability alter the pointers location to a given place based off of its current location.
