# Stack Smashing

## Questions

1. A stack canary is a value that one stores directly before the return address.  It is essentially a litmus test that one can use
to check to see if stack overflow has occurred before they attempt to go to the return address.  The stack canary should not change
if one's program is running correctly, so by checking to see if it has, we can stop our program before going to the return adress
because it is likely some type of stack overflow has taken place if the canary value has changed.

2. A stack canary is called a canary because it is a warning that the return address is being attempting to be rewritten.  Canaries
serves as warnings when the toxic gas concentration is too high, so both types of canaries carry a warning sign.

3.
int overflow(int array[5])
{
    array[12] = 4;
    return 5 * array[12];
}

## Debrief

1. I found the attached youtube link and stack overflow's discussion of the stack vs the heap helpful in answering this problem's
questions.

2. I spent about an hour on this problem's questions.
