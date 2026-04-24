Given a Binary tree. Find the level in binary tree which has the maximum number of nodes.
Example 1:
Input:
      2
    /    \ 
   1      3
 /   \     \
4    6      8
     / 
    5
Output: 2
Explanation: The level 2 with nodes 4,
6 and 8 is the level with maximum
number of nodes. 
Your Task:
You don't need to read input or print anything. Your task is to complete the function maxNodeLevel() that takes root node of the tree as input and returns an integer which is level of the tree with maximum nodes. The root is at level 0. If two or more levels have same number of maximum nodes , then return smallest level.
Expected Time Complexity: O(N).
Expected Auxiliary Space: O(N).
Constraints:
1<=Number of level<=10

Starter code:
```python
'''

class Node:

    def __init__(self,val):

        self.data = val

        self.left = None

        self.right = None

'''



# Return the level (0-indexed) with maximum number of nodes.

def maxNodeLevel(root):

    # code here
```
