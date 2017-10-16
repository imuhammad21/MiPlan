# Z++

## Questions

1.
function subtract($x, $y)
{
    return(add($x, -$y))
}

2.
function multiply($x, $y)
{
    if(not($x))
    {
        return($x)
    }
    if(not($y))
    {
        return($y)
    }
    if (0 < $y)
    {
        return add($x, multiply($x, subtract($y, 1)))
    }
    if ($y < 0)
    {
        return -multiply($x, -$y)
    }
}

3.
function multiply($x, $y)
{
    if(not($x))
    {
        return($x)
    }
    if(not($y))
    {
        return($y)
    }
    if (0 < $y)
    {
        return add($x, multiply($x, subtract($y, 1)))
    }
    if ($y < 0)
    {
        return -multiply($x, -$y)
    }
}

## Debrief

1. I used the site http://www.geeksforgeeks.org/multiply-two-numbers-without-using-multiply-division-bitwise-operators-and-no-loops/
to find a useful algoritm for problem 3.

2. I spent about 5 hours on this problem's questions.
