#include <stdio.h>
#include <cs50.h>
#include <math.h>
int main(void)
{
    float n;
    int i = 0;
    do
    {
        n = get_float("How much change?: ");
    }
    while (n < 0 );
    // Makes the hundreths place now the ones place to perform cleaner subraction
    n = n * 100;
    // This function rounds any value to the nearest cent
    n = round(n);
    // As long as the amount of change is greater than 25 cents, subract a quarter and add 1 coin to total
    while (n >= 25)
    {
        i++;
        // Make the new n the previous n subtracted by 25, and then perform this process again until n >= 25
        n = n - 25;
    }
    // As long as the amount of change is greater than 10 cents, subract a dime and add 1 coin to total
    while (n >= 10)
    {
        i++;
        n = n - 10;
    }
    // As long as the amount of change is greater than 5 cents, subract a nickel and add 1 coin to total
    while (n >= 5)
    {
        i++;
        n = n - 5;
    }
    // As long as the amount of change is greater than 1 cent, subract a penny and add 1 coin to total
    while (n >= 1)
    {
        i++;
        n = n - 1;
    }
    // Show total number of coins used
    printf("%i\n", i);
}