#include <stdio.h>
#include <cs50.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

int main(int argc, string argv[])
{
    // Make sure there are two command line arguments total
    if (argc != 2)
    {
        printf("Enter 1 string after ./vigenere\n");
        return 1;
    }
    // Make sure second command line argument contains entirely letters
    for (int i = 0, n = strlen(argv[1]); i < n; i++)
    {
        if (!isalpha(argv[1][i]))
        {
            printf("Ensure string is fully alphabetical\n");
            return 1;
        }
    }
    string plaintext = get_string("plaintext: ");
    printf("ciphertext: ");
    // Save "keylength" as variable so that argv1 knows when to wrap around itself
    int keylength = strlen(argv[1]);
    for (int i = 0, n = strlen(plaintext); i < n; i++)
    {
        // Make sure each plaintext character is alphabetical.  If not, don't encipher and just print.
        if (isalpha(plaintext[i]))
        {
            // Converts keyword character from ascii index to alphabetical index by subtracting
            if (isupper(argv[1][i % keylength]))
            {
                argv[1][i % keylength] -= 65;
            }
            // Converts keyword character from ascii index to alphabetical index by subtracting
            if (islower(argv[1][i % keylength]))
            {
                argv[1][i % keylength] -= 97;
            }
            // Converts plaintext character from ascii index to alphabetical index by subtracting, then converts back to ascii after being enciphered
            if (isupper(plaintext[i]))
            {
                plaintext[i] -= 65;
                plaintext[i] = (plaintext[i] + (argv[1][i % keylength])) % 26 + 65;
                printf("%c", plaintext[i]);
            }
            // Converts plaintext character from ascii index to alphabetical index by subtracting, then converts back to ascii after being enciphered
            if (islower(plaintext[i]))
            {
                plaintext[i] -= 97;
                plaintext[i] = (plaintext[i] + (argv[1][i % keylength])) % 26 + 97;
                printf("%c", plaintext[i]);
            }
        }
        // If not alphabetical character, should not be encrypted, so simply print
        else
        {
            printf("%c", plaintext[i]);
        }
    }
    printf("\n");
    return 0;
}
