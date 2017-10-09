# Questions

## What is pneumonoultramicroscopicsilicovolcanoconiosis?

Pneumonoultramicroscopicsilicovolcanoconiosis is an obscure term ostensibly referring to a lung disease caused by silica dust, sometimes cited
as one of the longest words in the English language.  Its length represents the length of the longest word in our dictionary, and is also a text file in our program.

## According to its man page, what does `getrusage` do?

'getrusage' times the execution of check, load, size, and unload.

## Per that same man page, how many members are in a variable of type `struct rusage`?

There are sixteen members in a variable of type 'struct rusage'

## Why do you think we pass `before` and `after` by reference (instead of by value) to `calculate`, even though we're not changing their contents?

Both pointers a and b are set to the ru_utime.tv_usec and ru_stime.tv_usec, so instead of having to copy the values of these constants in two different places,
you pass before and after reference in order to give them flexibiltiy in what they can print to and elimnate the need for more than two variables.

## Explain as precisely as possible, in a paragraph or more, how `main` goes about reading words from a file. In other words, convince us that you indeed understand how that function's `for` loop works.

First, main must open a file with fopen and specify that the file just opened must be available for reading.  This function returns to main a pointer to that file,
unless it is NULL, in which case main informs the user that it could not open the file and stops the program.  Then, main utilizes a 'for' loop that contains the
file pointer fgetc.  fgetc goes to the next(or first) character in a file and returns a char that is the value stored at that particular address.  The condition
of this for loop designates that the loop will keep going until the character retrieved by fgetc is the EOF, at which point the loop would stop.  This for loop
is able to "read" the words from the file because it iterates over each character in the file using fgetc and then stores each value into a varialbe titled 'c',
as given by the third parameter in the for loop.

## Why do you think we used `fgetc` to read each word's characters one at a time rather than use `fscanf` with a format string like `"%s"` to read whole words at a time? Put another way, what problems might arise by relying on `fscanf` alone?

Because valid words may be entirely alphabetical or mostly alphabetical with an apostorphe, we must go through each character one by one checking both
conditions.  Reading string by string would make it more difficult to check if each word is a valid word, because char arrays don't allow one to view
each character in the array at once.

## Why do you think we declared the parameters for `check` and `load` as `const` (which means "constant")?

Declaring parameters for 'check' and 'load' as constants protects against anyone's code who redefines check or load from altering the true input to the
function.  In other words, if the input to check is a constant, even if I write 'check = x' later on in my code, the input stays the same, which is what
we want in order to evaluate everyone's code equally and fairly.
