Note: This POTD is a part of Geek Summer Carnival. Solve all POTD consecutively from 5th to 10th April and get a chance to win exclusive discount vouchers on our GfG courses.
Geek is at the geek summer carnival. To unlock discounts on exclusive courses he is given a card with a binary tree, a target node and a positive integer k on it. 
He needs to find the sum of all nodes within a max distance k from target node such that the target node is included in sum.
Example 1:
Input:
target = 9 
k = 1
Binary Tree = 
            1
           /  \
          2    9
        /     /  \
       4     5    7
      /  \       /  \
     8    19    20   11
    /   /   \
  30   40   50
Output: 22
Explanation: 
Nodes within distance 1 from 9 
9 + 5 + 7 + 1 = 22
Example 2:
Input:
target = 40 
k = 2
Binary Tree = 
            1
           /  \
          2    9
        /     /  \
       4     5    7
      /  \       /  \
     8    19    20   11
    /   /   \
  30   40   50
Output: 113
Explanation:
Nodes within distance 2 from 40,
40 + 19 + 50 + 4 = 113
Your Task:
You don't need to read input or print anything. Complete the function sum_at_distK() that takes the root of the given binary tree, target and k as input parameters and return the required sum. 
Expected time complexity: O(n)
Expected space complexity: O(n)
Constraints:
1 <= number of nodes <= 1000
1 <= data in nodes,target <= 10000
1 <= k <= 20

Starter code:
```python
'''

# node class:



class Node:

    def __init__(self, val):

        self.right = None

        self.data = val

        self.left = None



'''

class Solution:

    def sum_at_distK(self,root, target, k):

        # code here
```
