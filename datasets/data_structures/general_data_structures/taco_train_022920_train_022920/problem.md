Given a linked list of size N and a key. The task is to insert the key in the middle of the linked list.
Example 1:
Input:
LinkedList = 1->2->4
key = 3
Output: 1 2 3 4
Explanation: The new element is inserted
after the current middle element in the
linked list.
Example 2:
Input:
LinkedList = 10->20->40->50
key = 30
Output: 10 20 30 40 50
Explanation: The new element is inserted
after the current middle element in the
linked list and Hence, the output is
10 20 30 40 50.
 
Your Task:
The task is to complete the function insertInMiddle() which takes head reference and element to be inserted as the arguments. The printing is done automatically by the driver code.
Expected Time Complexity : O(N)
Expected Auxilliary Space : O(1)
Constraints:
1 <= N <= 10^{4}

Starter code:
```python
#User function Template for python3

'''

    Your task is to insert a new node in 

	the middle of the linked list with

	the given value.

	

	{

		# Node Class

		class Node:

		    def __init__(self, data):   # data -> value stored in node

		        self.data = data

		        self.next = None

	}

	

	Function Arguments: head (head of linked list), node 

	(node to be inserted in middle)

	Return Type: None, just insert the new node at mid.

'''

#Function to insert a node in the middle of the linked list.

def insertInMid(head,node):

    #code here
```
