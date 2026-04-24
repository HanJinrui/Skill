Given a Binary Tree and a target key, you need to find all the ancestors of the given target key.
              1
            /   \
          2      3
        /  \
      4     5
     /
    7
Key: 7
Ancestor: 4 2 1
Example 1:
Input:
        1
      /   \
     2     3
target = 2
Output: 1
Example 2:
Input:
         1
       /   \
      2     3
    /  \   /  \
   4    5 6    8
  /
 7
target = 7
Output: 4 2 1
Your Task:
Your task is to complete the function Ancestors() that finds all the ancestors of the key in the given binary tree.
Note:
The return type is
cpp: vector
Java: ArrayList
python: list
Expected Time Complexity: O(N).
Expected Auxiliary Space: O(H).
Note: H is the height of the tree and this space is used implicitly for the recursion stack.
Constraints:
1 ≤ N ≤ 10^{3}
1 ≤ data of node ≤ 10^{4}

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

    def Ancestors(self, root,target):

        '''

        :param root: root of the given tree.

        :return: None, print the space separated post ancestors of given target., don't print new line

        '''

        #code here
```
