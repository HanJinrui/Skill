Given a Binary Tree, find the In-Order Traversal of it.
Example 1:
Input:
       1
     /  \
    3    2
Output: 3 1 2
Example 2:
Input:
        10
     /      \ 
    20       30 
  /    \    /
 40    60  50
Output: 40 20 60 10 50 30
Your Task:
You don't need to read input or print anything. Your task is to complete the function inOrder() that takes root node of the tree as input and returns a list containing the In-Order Traversal of the given Binary Tree.
Expected Time Complexity: O(N).
Expected Auxiliary Space: O(N).
Constraints:
1 <= Number of nodes <= 10^{5}
0 <= Data of a node <= 10^{5}

Starter code:
```python
#User function Template for python3


'''
# Node Class:
class Node:
    def init(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

#Function to return a list containing the inorder traversal of the tree. 
class Solution:
    def InOrder(self,root):
        # code here
```
