Due to the rise of covid-19 cases in India, this year BCCI decided to organize knock-out matches in IPL rather than a league. 
Today is matchday 3 and it is between Geek's favorite team Royal Challengers Banglore and the most powerful batting team - Sunrisers Hyderabad. Virat Kholi captain of the team RCB tried everything to win the trophy but never succeeded. He went to guruji to seek the blessing, but the guruji gave him a problem and asked him to solve it. Guruji gave him a tree-like structure, asked him to stand at the target node and find the sum of all nodes within a maximum distance of k from the target node. can Kholi solve this problem to qualify for the next round?
Note: The target node should be included in the sum. 
Example 1:
Input:
                   1
                 /    \
                2      9
               /      /  \
              4      5     7
            /   \         /  \
           8     19     20    11
          /     /  \
         30   40   50
target = 9, K = 1
Output:
22
Explanation:
Nodes within distance 1 from 9 are 9, 5, 7, 1  
Example 2:
Input:
                   1
                 /    \
                2      9
               /      /  \
              4      5     7
            /   \         /  \
           8     19     20    11
          /     /  \
         30   40   50
target = 40, K = 2
Output:
113
Explanation:
Nodes within distance 2 from 40 are 40, 19, 50, 4
Your Task:
You don't need to read input or print anything. Complete the function sum_at_distK() which takes the root of the tree, target, and K  as input parameter and returns the sum of all nodes within a max distance of k from the target 
Constraints:
1 ≤ N, Node Value ≤ 10^{5}
1 ≤ K ≤ 20

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

    def sum_at_distK(self, root, target, k):

        # Your code goes here
```
