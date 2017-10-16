# Now Boarding

## Questions

1.

typedef struct
{
    int* front;
    unsigned int *next;
    int priority;
    int size;
}
pqueue;


2.
Intitialize pointer p to point to front of linked list
For each element in queue
    If passenger.group <= pqueue.priority
        Point previous pointer to current element
    If passenger.group > pqueue.priority
        Point p to next element in linked list
    If p = NULL
        Break

3. This algorithm has an upper bound running time of O(n).  In the worst case scenario, the passenger will have to traverse the entire
linked list to find out that he/she should be at the end of the list, which will take n steps.

4.
Initialize pointer p to point to front of linked list
Intialize pointer front to point to first element in linked list
Free pointer p.

5. The upper bound on this algorithm's running time is O(1).  Because the queue is already in order, the first passenger to be
dequeued is always the first element in the linked list.  Therefore, regardless of the total amount of passengers, dequeing a passenger
will take a constant amount of time, or O(1).

## Debrief

1. I found Lecture 5 and the short on linked lists as helful resoucres for answering this problem's questions.

2. I spent about an hour and a half on this problem's questions.
