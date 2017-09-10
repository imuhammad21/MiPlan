#include <stdio.h>
#include <cs50.h>

int main(void)
{
    int n;

    do
    {
        n = get_int("Height: ");
    }
    while (n < 0 || n > 23);
    // "bricks" denotes the number of blocks to be printed on each row
    for (int bricks = 0; bricks <= n - 1; bricks++)
    {
        // the number of spaces printed is the height minus the number of bricks
        for (int j = 0; j < n - bricks - 1; j++)
        {
            printf(" ");
        }
        // we want two bricks on the zeroth row, so we add 2 to do so
        for (int k = 0; k < bricks + 2; k++)
        {
            printf("#");
        }
        printf("\n");
    }
}


