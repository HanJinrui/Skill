Given two linked lists, your task is to complete the function mergeList() which inserts nodes of second list into first list at alternate positions of first list. The lists are given in the reverse order.
Constraints:
1 <= T <= 100
1 <= N <= 100
Example:
Input:
2
2
9 10
6
5 4 3 2 1 6
5
99 88 77 66 55
5
55 44 33 22 11
Output:
10 6 9 12 3 4 5
55 11 66 22 77 33 88 44 99 55
Explanation:
Testcase 1:
The two linked list are 10 -> 9 and 6 -> 1-> 2 -> 3 -> 4 -> 5
After merging the two lists as required, the new list is like: 10-> 6-> 9-> 1-> 2-> 3-> 4-> 5.
User Task:
The task is to complete the function mergeList() which should merge the two lists as required. For each test case modify the given head of the lists.

Starter code:
```python
# your task is to complete this function
# function should return a list of the
# two new heads
def mergeList(head1, head2):
    # Code here
    return [head1, head2]
```
