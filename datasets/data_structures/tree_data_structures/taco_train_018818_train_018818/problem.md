Given a Two Binary Trees, write a function that returns true if one is mirror of other, else returns false.
             
Example 1:
Input:
T1:     1     T2:     1
      /   \         /   \
     2     3       3     2
Output: 1
Example 2:
Input:
T1:     10      T2:   10
       /  \          /  \
      20  30        20  30
     /  \          /  \
    40   60       40  60
Output: 0
Your Task:
You don't need to take input. Just complete the function areMirror() that takes root node of two tree as parameter and returns true, if one is the mirror of other else returns false. (The driver's code print 1 if the returned value is true, otherwise 0)
Expected Time Complexity: O(N).
Expected Auxiliary Space: O(Height of the Tree).
Constraints:
1 <= Number of nodes<= 10000
-1000 <= Data of a node<= 1000

Starter code:
```python
#User function Template for python3

'''
# Node Class:
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''
class Solution:
    def areMirror(self,root1,root2):
        '''
        :param root1,root2: two root of the given trees.
        :return: True False
        
        '''
        #code here
```
