Given inorder and level-order traversals of a Binary Tree, construct the Binary Tree and return the root Node. 
Input:
First line consists of T test cases. First line of every test case consists of N, denoting number of elements is respective arrays. Second and third line consists of arrays containing Inorder and Level-order traversal respectively.
Output:
Single line output, print the preOrder traversal of array.
Constraints:
1<=T<=100
1<=N<=100
Example:
Input:
2
3
1 0 2 
0 1 2 
7
3 1 4 0 5 2 6 
0 1 2 3 4 5 6 
Output:
0 1 2
0 1 3 4 2 5 6

Starter code:
```python
#User function Template for python3

'''
class Node:

    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None
'''

def buildTree(level, ino):
    #code here
    #return root of tree
```
