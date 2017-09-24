// Helper functions for music

#include <cs50.h>
#include <string.h>
#include "helpers.h"
#include <math.h>
#include <stdio.h>
// Define A4 and Zero so that these numers now have context
#define A4 440
#define zero 48

// Converts a fraction formatted as X/Y to eighths
int duration(string fraction)
{
    // Converts ASCII Value to Numerical Index
    int numerator = fraction[0] - zero;
    int denominator = fraction[2] - zero;
    // Uses cross-multipication to convert a fraction to the numerator of an equivalent fraction in eighths
    int newduration = (8 * numerator) / denominator;
    // Returns duration in eighths to function
    return newduration;
}
// Converts note formatted as AX or A#X to frequency
int frequency(string note)
{
    // Let first character in string 'note' be the "letter"
    char letter = note[0];
    // Initialize number of semitones away from 'A' at zero and change it according to letter
    int semitone = 0;
    // Let i be the index of note in which the octave is stored
    int i = 1;
    if (strlen(note) == 3)
    {
        // If note is in form A#X, note[1] is accidental and note[2] is octave
        i = 2;
        char accidental = note[1];
        // Add or subtract semitone given by accidental
        switch (accidental)
        {
            case '#':
                semitone += 1;
                break;
            case 'b':
                semitone -= 1;
                break;
        }
    }
    // Converts ASCII value of octave into Numerical Index
    double octave = note[i] - zero;
    // Add or subtract number of semitones from 'A' given by letter
    switch (letter)
    {
        case 'B':
            semitone += 2;
            break;
        case 'C':
            semitone -= 9;
            break;
        case 'D':
            semitone -= 7;
            break;
        case 'E':
            semitone -= 5;
            break;
        case 'F':
            semitone -= 4;
            break;
        case 'G':
            semitone -= 2;
            break;
    }
    // Finds the exponent to which to raise 2 in the equation freq = 2^n *440
    double exponent = (octave + (semitone / 12.00) - 4);
    // Raises 2 to this power and multiply by 440 to determine frequency
    double freq = pow(2, exponent) * A4;
    // Rounds frequency to nearest Hertz and returns to function
    return round(freq);
}
// Determines whether a string represents a rest
bool is_rest(string s)
{
    // If string s is length zero, the bool is_rest should be true, because there are no characters on the line.
    if (strlen(s) == 0)
    {
        return true;
    }
    // If string s has a non-zero length, the bool is_rest should be false.
    else
    {
        return false;
    }
}
