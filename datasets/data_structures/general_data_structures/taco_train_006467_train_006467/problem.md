You are given the head of a Linked List. You have to move the last element to the front of the Linked List and return the list.
 
Example 1:
Input:
N = 5
List = {2,5,6,2,1}
Output:
{1,2,5,6,2}
Explanation:
In the given linked list, the last element is 1,
after moving the last element to the front the
linked list will be {1,2,5,6,2}.
 
Example 2:
Input:
N = 1
List = {2}
Output:
{2}
Explanation:
Here 2 is the only element so, the linked list
will remain the same.
 
Your Task:
You don't need to read input or print anything. Your task is to complete the function moveToFront() which takes the address of the head of the linked list and returns the modified linked list.
 
Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)
 
Constraints:
1 <= N <= 10^{5}
0 <= Elements of List <= 10^{9}
Sum of N over all test cases doesn't exceeds 10^{6}

Starter code:
```python
from typing import Optional



"""



Definition for singly Link List Node

class Node:

    def __init__(self,x):

        self.data=x

        self.next=None



You can also use the following for printing the link list.

printList(node)

"""



class Solution:

    def moveToFront(self, head : Optional['Node']) -> Optional['Node']:

        # code here
```
