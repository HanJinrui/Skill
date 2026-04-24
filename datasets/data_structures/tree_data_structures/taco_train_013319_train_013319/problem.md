Given a Binary tree, the problem is to find mirror of a given node. The mirror of a node is a node which exist at the mirror position of node in opposite subtree at the root.
Example 1:
Input: 
          1        
        /   \       
       2     3     
      / \   / \    
     4   5 6   7   
and target = 4
Output: 7
Explanation: You can see below that the mirror 
node of 4 is 7.
          1       |       1
        /   \     |     /   \
       2     3    |    3     2
      / \   / \   |   / \   / \
     4   5 6   7  |  7   6 5   4
Example 2:
Input: 
        1
      /   \
     2     3
    / \
   4   5
and target = 4
Output: -1
Your Task:
You don't need to read input or print anything. Your task is to complete the function findMirror() which takes root node of the tree and a integer target as input parameter and returns the value of the mirror node of the given target node. If the mirror node does not exists return -1.
Expected Time Complexity: O(N)
Expected Auxiliary Space: O(N)
Constraints:
1<=n<=10^{4}
1<=data of node<=10^{4}
1<=target<=10^{4}

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
    def findMirror(self,root, target):
        #code here
```
