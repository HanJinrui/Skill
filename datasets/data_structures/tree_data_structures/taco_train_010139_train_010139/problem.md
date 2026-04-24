You are given a binary tree. Your task is pretty straightforward. You have to find the sum of the product of each node and its mirror image (The mirror of a node is a node which exists at the mirror position of the node in opposite subtree at the root.). Don’t take into account a pair more than once. The root node is the mirror image of itself.
 
Example 1:
Input:
      4         
    /    \
   5      6
Output:
46
Explanation:
Sum = (4*4) + (5*6) = 46
Example 2:
Input:
                       1                 
                   /        \
                 3            2
                  /  \         /  \
              7     6       5    4
            /   \    \     /  \    \
          11    10    15  9    8    12
Output:
332
Explanation:
Sum = (1*1) + (3*2) + (7*4) + (6*5) + (11*12) + (15*9) = 332
 
Your Task:
You need to complete the function imgMultiply() that takes root as parameter and returns the required sum.The answer may be very large, compute the answer modulo 10^{9} + 7.
Expected Time Complexity: O(Number of nodes).
Expected Auxiliary Space: O(Height of the Tree).
Constraints:            
1 <= Number of nodes <= 10^{5}
1 <= Data of a node <= 10^{5}

Starter code:
```python
#User function Template for python3
'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''

class Solution:
    # your task is to complete this function
    def imgMultiply(self, root):
        # Code here
```
