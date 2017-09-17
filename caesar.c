#include <stdio.h>
#include <cs50.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

int main(int argc, string argv[])
{
    // If ./caesar is not followed by 1 other string, ask the user to do so and quit program
    if (argc != 2 )
    {
        printf("Enter 1 integer after ./caesar\n");
        return 1;
    }
    int key = atoi(argv[1]);
    string plaintext = get_string("plaintext: ");
    printf("ciphertext: ");
    for (int i = 0, n = strlen(plaintext); i < n ; i++)
    {
        // Checks to see if each character is uppercase letter
        if isupper((plaintext[i]))
        {
            // Converts from ascii index to alphabetical index by subtracting, then converts back to ascii
            plaintext[i] -= 65;
            plaintext[i] = (plaintext[i] + (key)) % 26 + 65;
            printf("%c", plaintext[i]);
        }
        // Checks to see if each character is lowercase letter
        else if (islower(plaintext[i]))
        {
            // Converts from ascii index to alphabetical index by subtracting, then converts back to ascii
            plaintext[i] -= 97;
            plaintext[i] = (plaintext[i] + (key)) % 26 + 97;
            printf("%c", plaintext[i]);
        }
        // If not uppercase nor lowercase letter, must be character that should not be encrypted, so simply print
        else
        {
            printf("%c", plaintext[i]);
        }
    }
    printf("\n");
    return 0;
}
