# Fair and Balanced

## Questions

1. Yes, the array {16, 26, 39, 3, 39} is balanced.

2. Yes, the array {0, 0, 0, 0, 0} is balanced.

3.
bool balanced(int array[], int size)
{
    int partial1 = array[0];
    int partial2 = array[size-1];
    if (size <= 3)
    {
        if (array[0] == array[size-1])
        {
            return true;
        }
        else
        {
            return false;
        }
    }
    for(int i = 1; i < floor(size/2); i++)
    {
        partial1 += array[i];
    }
    for(int j = 1; j < floor(size/2); j++)
    {
        partial2 += array[size-(j+1)];
    }
    if (partial1 == partial2)
    {
        return true;
    }
    else
    {
        return false;
    }
}

## Debrief

1. The source code for swap proved to be very helpful in testing the implementation of my function.

2. I spent about an hour on this problem's question.
