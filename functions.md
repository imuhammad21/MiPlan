# #functions

## Questions

1. This hashtable only has a maximum of 52 'buckets', or indices in which to place inputs into its array; all of the uppercase
alphabetical characters and all of the lowercase alphabetical characters.  Therefore, any number of inputs above 52 is destined to
cause collsions, and collisions make a hash function slower.  If the hash function utlizes linear probing, it can accept a maximum of
52 inputs, but if its indices are pointers to the first node in a linked list, the function would have to iterate over each node in
the linked list to find a particular value.  Since 52 is a rather small number compared to the capablities of a hash table, these
linked lists can become very long, and iterating through a long linked list(because of a lack of sorting) makes one's hash function
slower. Therefore, this hash function would be rather slow.

2. By defintion, this hash function is perfect because each character has a value that maps to a specific number, and this number can
be represented in decimal form.  Therefore, a string of characters can be represented by an even longer, or larger number.  However,
each character has a particular value when represented with its smallest value in the ones place, so if one strings characters together
to represent a larger number, they disrupt the true ASCII value of each character.  In other words, "16" has a value of sixteen when
the 6 is in the ones place and the 1 is in the tens place, but "16" has a value of 160 when the 6 is in the tens place and the 1 in
in the hundreths place.  When one changes the place of a digit in a sequence, they disrupt its true value, and treating characters in
a string as continuous numbers that can be added on to one another back to back destroys the true value of each individual character,
and would therefore cause one to lose the meaning of the characters in a string.

3. A hash function allows a program the ability to account for a wide range of scenarios with much less storage than it would take
to compare each and every scenario to a hard-coded expected outcome.  In recover's check50, the 64-digit hexadecimal string which is
the output of a hash function allows one the ability to take a very long JPEG file and distinguish it from the other JPEG files without
comparing each and every byte to a copy of it, which would take a large amount of time.  Instead of iterating over the 512 bytes in each
JPEG file, the output of this hash function is able to compared to a 64-byte hexadecimal string, which takes up 1/8 of the bytes of a
JPEG.  Essentially, storing hashes that dsitinguish each partiucalr JPEG form one another serves the same duty of ensuring that the
recovered images are correct, but takes up much less space in memory.

4. Omega describes the upper bound, or worst case scenario for an algorithm to complete.  When looking up a word in a hash table,
one must first hash the word to find the correct index in the array, but then iterate over every node in the linked list in order to
look up a particular word.  The length of this linked list theoretically should be equal to the total number of words in the hash table(n),
divided by the size of the array, which provides an O(n/k), where k is the size of the array/number of distinct hashes.  O(n/k) is on
the order of O(n), so we say that hash tables have an upper bound of O(n).  A trie, however, has a constant upper bound run time irrelevant
of the total number of words in the trie.  Because after each iteration, one is narrowing down the list of possible words to the point
where one either finds a path to the word for which they are looking or not, the majority of the words in the dictionary become insignificant
rather quickly. The upper bound on word lookup in a trie is essentially the length of the word, which does not change when one adds
or subtracts words to or from the dictionary.  Therefore, we say that this algorithm has a constant upper bound running time, or O(1).

## Debrief

1. The problem set 4 specification was helpful in answering this problem's questions.

2. I spent about 1 hour on this problem's questions.
