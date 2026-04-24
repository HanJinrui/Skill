Given a binary tree, you need to find the number of all root to leaf paths along with their path lengths.
Example 1:
Input:
      3
    /   \
   2     4
Output:
2 2 $
Explanation :
There are 2 roots to leaf paths
of length 2(3 -> 2 and 3 -> 4)
Example 2:
Input:
        10
     /   \
    20    30
   / \    
  40  60
Output:
2 1 $3 2 $
Explanation:
There is 1 root leaf paths of
length 2 and 2 roots to leaf paths
of length 3.
Your Task:
Your task is to complete the function pathCounts that prints the path length and the number of root to leaf paths of this length separated by space.  Every path length and number of root to leaf path should be separated by  "$".
Constraints:
1 <= T <= 30
1 <= Number of nodes <= 100
1 <= Data of a node <= 1000

Starter code:
```python
'''

class Node:

    def __init__(self, value):

        self.left = None

        self.data = value

        self.right = None

'''

# Your task is to complete this function

# Function should print all possible lengths

# print a new at end of function

def pathCounts(root):

    # Code here
```
