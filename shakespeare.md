# To be or not to be

## ~~That is the question~~ These are the questions

4.1. Script.py initially generates 1000 DNA objects.

4.2. update.fitness first compares the first character in the string self.gene to the first character in the target string "to be or
not to be".  If the first character in self.gene is the same as the first character in the target string, it incriments a counter "score"
by 1.  It then compares the second character in the string self.gene to the second character in the target string "to be or not to
be", and adds 1 to the score if these two characters are the same.  It completes this same process ofr each character in self.gene and
in target, but compares the characters IN ORDER (i.e. even if the self.gene string has a t in it, if it is not the first or twelfth
character, score will not be incrimented).  The "fitness" is determined by dividing the score after iterating through all of the
characters by the total number of charaters in the targer string, effectively providing a number between zero and 1 that represents
the proportion of characters that match.

4.3. The fitness of KoMQ%25"zHnGt1whXY, as would be computed by update_fitness, is 1/18, approximately 0.05555555555.

4.4. Since self.genes has the same number of characters as the target string, there would be no need for any insertions or
deletions, and the score would simply be the number of characters that are not the same, i.e 18 - score as it is calculated now.
Therefore, fitness would be (number of characters(in order) that are not indentical/18).

4.5. Script.py "mutates" some of the characters in a string to ensure that even if two parents are entirely lacking 1 character that
will eventaully be necessary to reach the target string that there is a possibility that a string will randomly evenutally receive that
character.  If offspring were entirely based off of the genes of the parents, then children of parents who never had a certain character
would simply never receive it, so for this algorithm to work, we need to have some way of fixing this problem by randomly inserting new
characters into strings.

## Debrief

a. I found Problem Set 6 and the website https://medium.com/generative-design/evolving-design-b0941a17b759 helpful in answering this
problem's questions.

b. I spent about 1 hour to complete this problem's questions.
