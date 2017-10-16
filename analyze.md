# Analyze This

## Questions

1a. Yes, this alogrithm is correct.

1b. The upper bound on this algorithm's runtime is 2n, or O(n).  In the worst case scenario, Stelios will have to iterate over n
cards to put them in piles based off of their second digit, which will take n steps, and then iterate over n cards again in
the second big stack to put them in piles based off of their first digit.  Therefore, this alogirtm takes n steps to complete its first
sorting, and n steps to complete its second sorting, at which point the alogirthm is complete. n + n =2n, so this algorithm has
a running time of 2n.

2a. Yes, this algorithm is correct.

2b. The upper bound on this alogirthm's runtime is ((n^2)-n)/2,, or O(n^2) the same upper bound as bubble sort itself.  The reason why this
algorithm's runtime is ((n^2)-n)/2 is because this is the sum of (n-1)+(n-2)+(n-3)+...1.  The first time Maria interates through her
list, she will have to make n-1 comparisons to bubble the largest number to the far right.  Then, the largest number will be at the
far right and the list that she needs to sort has become one unit shorter.  When she bubbles the smallest number to the left from right
to left, she checks n-1 numbers, and therefore needs to make n-2 comparisons.  The total number of comparisons total is (n-1)(bubbling
to the right) + (n-2)(bubbling to the left).  After the bubbling to the left, the list is two units shorter than it was initially,
because the number on the far left is sorted and the number on the far right is sorted.  Therefore, the total number of comparisons
will be (n-3), which we will then add to (n-1) and (n-2).  This process continues until we get down to two elements in the 'center'
of the list, for which one comparison is needed.  Therefore, the upper bound on running time, assuming we need each and every one
of these comparisons, is (n-1)+(n-2)+(n-3)+...1, or ((n^2)-n)/2.

3a. Yes, this algorithm is correct.

3b. The upper bound on this algorithm's runtime is 2n, or O(n).  Should the card never be shuffled to the top of the deck/not exist
in the deck, Natalie would have to, for each card in the deck, discard the card once she realizes it is not the Queen of Hearts and
then shuffle the remaining deck.  The deck does become smaller each time she shuffles, but since shuffling is not correlated to the
number of cards in the deck, it is considered one step regardless of the size.

## Debrief

1. Lecture 3's notes on sorting were extrememly helpful in completing this problem

2. I spent about one hour on this problem's questions
