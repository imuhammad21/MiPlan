# Emoji

## Questions

1. 2.5 bytes are necessary to represnt the jack-o-lantern emoji in Unicode. The code has 5 hexadecimal characters after the predeing 0x,
and 2 hexadeciaml charcters desrbie 1 byte. 5/2 = 2.5, which is the number of bytes necessary to represent this emoji.

2. The storage size for a char in c is one byte, and the jack-o-lantern requires 2.5 bytes to be represented.  Therefore, the
jack-o-lantern cannot be represented by a char.

3.
bool hex(int n, string s);

emoji get_emoji(string prompt)
{
    string emj;
    do
    {
        emj = get_string("%s", prompt);
    }
    while(emj[0] != 'U' || emj[1] != '+' || !hex(strlen(emj), emj));
    emj[0] = '0';
    emj[1] = 'x';
    char null_terminator = '\0';
    char * endptr = &null_terminator;
    return strtol(emj, &endptr, 16);
}

bool hex(int n, string s)
{
    for (int i = 2; i < n; i++)
    {
        if (!isxdigit(s[i]))
        {
            return false;
        }
    }
    return true;
}


## Debrief

1. I used nearly every resource available to attempt to answer this problem's questions.  I looked at Lectures 1-3, looked up the
source code for positive.c, went on cs50.reference to look up get_string function, and went on https://linux.die.net/man/3/printf
to check to see what the format "printf(3)" meant.

2. I spent about 7 hours on this problem's questions.
