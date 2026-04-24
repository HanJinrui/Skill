Given a Linked List Representation of Complete Binary Tree. The task is to construct the Binary tree.
Note : The complete binary tree is represented as a linked list in a way where if root node is stored at position i, its left, and right children are stored at position 2*i+1, 2*i+2 respectively.
Example 1:
Input:
N = 5
K = 1->2->3->4->5
Output: 1 2 3 4 5
Explanation: The tree would look like
      1
    /   \
   2     3
 /  \
4   5
Now, the level order traversal of
the above tree is 1 2 3 4 5.
Example 2:
Input:
N = 5
K = 5->4->3->2->1
Output: 5 4 3 2 1
Explanation: The tree would look like
     5
   /  \
  4    3
 / \
2    1
Now, the level order traversal of
the above tree is 5 4 3 2 1.
Your Task:
The task is to complete the function convert() which takes head of linked list and root of the tree as the reference. The driver code prints the level order.
Expected Time Complexity: O(N).
Expected Auxiliary Space: O(N).
Note: H is the height of the tree and this space is used implicitly for recursion stack.
Constraints:
1 <= N <= 10^{5}
1 <= K_{i} <= 10^{5}

Starter code:
```python
# User function Template for python3



'''

class ListNode:



    # Constructor to create a new node

    def __init__(self, data):

        self.data = data

        self.next = None





# Tree Node structure

class Tree:



    # Constructor to create a new node

    def __init__(self, data):

        self.data = data

        self.left = None

        self.right = None



'''



#Function to make binary tree from linked list.

def convert(head):

  

    # code here
```
