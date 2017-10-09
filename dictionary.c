// Implements a dictionary's functionality
#include <cs50.h>
#include <ctype.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <strings.h>
#include "dictionary.h"
#define TABLESIZE 3000
// Initialize number of words in dictionary to zero
int counter = 0;
// Hash Function found at http://www.cse.yorku.ca/~oz/hash.html
unsigned long
hash(const char *str)
{
    unsigned long hash = TABLESIZE - 1;
    int c = 0;
    while (c == (tolower(*str++)))
    {
        hash = (((hash << 5) + hash) + c) % TABLESIZE;
    }
    return hash;
}
// Define what a node is
typedef struct node
{
    char term[LENGTH + 1];
    struct node *next;
} node;
// Create hastable of type node pointer
node *hashtable[TABLESIZE];

// Returns true if word is in dictionary else false
bool check(const char *word)
{
    int index = hash(word);
    // Create pointer called 'head' pointing to the index in hashtable that the function spits out
    node *head = hashtable[index];
    // Point curosr initially to head
    node *cursor = head;
    while (cursor != NULL)
    {
        // If word is found, return true, else mocve cursor to next word in linked list
        if (strcasecmp(cursor->term, word) == 0)
        {
            return true;
        }
        else
        {
            cursor = cursor -> next;
        }
    }
    return false;
}

// Loads dictionary into memory, returning true if successful else false
bool load(const char *dictionary)
{
    // Open a file for reading the dictionary
    FILE *text = fopen(dictionary, "r");
    // Ensure pointer is not NULL
    if (text == NULL)
    {
        return false;
    }
    // Declare a buffer in which to temporarily store words
    char buffer[LENGTH + 1];
    // Scan words from dictionary into buffer until reached end of file
    while (fscanf(text, "%s", buffer) != EOF)
    {
        // Allocate memory for new node
        node *new_node = malloc(sizeof(node));
        // Ensure pointer is not NULL
        if (new_node == NULL)
        {
            unload();
            return false;
        }
        // Copy contents of node(the word) into the buffer
        strcpy(new_node->term, buffer);
        // Hash this word and then access the proper index in the hashtable array
        int index = hash(new_node->term);
        // Move to the insert the word into the next available place in the linked list
        new_node->next = hashtable[index];
        hashtable[index] = new_node;
        // Count how many words are in the dictionary
        counter++;
    }
    fclose(text);
    return true;
}
// Returns number of words in dictionary if loaded else 0 if not yet loaded
unsigned int size(void)
{
    if (&load)
    {
        return counter;
    }
    else
    {
        return 0;
    }
}
// Unloads dictionary from memory, returning true if successful else false
bool unload(void)
{
    // Go through each index in the hashtable one by one
    for (int wordcount = 0; wordcount < TABLESIZE; wordcount++)
    {
        // Name head pointer the index of each hastable
        node *head = hashtable[wordcount];
        // Point cursor to the same place head is pointing
        node *cursor = head;
        while (cursor != NULL)
        {
            // Point temp to where cursor is pointing, move cursor to next pointer, and then free temp, releasing the memory
            node *temp = cursor;
            cursor = cursor -> next;
            free(temp);
        }
        if (cursor != NULL)
        {
            return false;
        }
    }
    return true;
}
