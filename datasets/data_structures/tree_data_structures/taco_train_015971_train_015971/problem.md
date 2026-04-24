Given a binary tree of size N, your task is to complete the function pairwiseSwap(), that swap leaf nodes in the given binary tree pairwise starting from from left to right.
Example 1:
Input: 
Output: 7 2 1 4 5 9 3 8 6 10 
Explanation:
The sequence of leaf nodes in original binary tree
from left to right is (4, 7, 8, 9, 10). Now if we 
try to form pairs from this sequence, we will have 
two pairs as (4, 7), (8, 9). The last node (10) is 
unable to form pair with any node and thus left unswapped
 
Example 2:
Input: 
          1
       /     \
      2       3
       \    /    \
        5  6      7
Output: 2 6 1 5 3 7
        1
     /     \
    2       3
     \    /   \
      6  5     7
 
Your Task:
You don't need to read input or print anything. Your task is to complete the function pairwiseSwap() which takes root node of the tree as input parameter. 
Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)
Constraints:
1<=N<=10^{3}
1<=Data of a node <=10^{3}

Starter code:
```python
#User function Template for python3

'''
class Node:
    def __init__(self,val):
        self.data=val
        self.left=None
        self.right=None
'''
class Solution:
    def pairwiseSwap(self,root):
        #code here
```
