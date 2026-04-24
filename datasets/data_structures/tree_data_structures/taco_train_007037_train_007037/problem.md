Given a connected undirected tree with N nodes. In one move, you can merge any two adjacent nodes. Calculate the minimum number of moves required to turn the tree into a star tree.
-> Merging adjacent nodes means deleting the edge between them and considering both the nodes as a single one.
-> A Star tree is a tree with a center node, and all other nodes are connected to the center node only.
 
Example 1:
Input:
N = 5
p[] = {-1, 0, 0, 1, 1}
Output:
1
Explanation: 
Tree looks like:
            0
           / \ 
         1    2 
       /  \ 
      3    4
Merge the edge 0 - 2 in one operation
Example 2:
Input: N = 8
p[] = {-1 0 0 0 0 2 2 5}
Output:
2
Explanation:
Tree looks like:
              0
           / / \ \
          / |   |  \
        1   2   3   4
           / \
          5   6
          |
          7
Merge node 5 to 2 and then 2 to 0, 
thus tree formed will be a star tree. 
Your Task:
You don't need to read, input, or print anything. Your task is to complete the function solve( ), which takes integer N, and an array p[ ] as input parameters and returns the minimum number of moves required to turn the tree into a star tree.
Expected Time Complexity: O(N)
Expected Auxiliary Space: O(N)
Constraints:
1 ≤ N ≤ 10^{5}
0 ≤ p[i] < N
p[0] = -1, 0 is the root node.

Starter code:
```python
from typing import List





class Solution:

    def solve(self, N : int, p : List[int]) -> int:

        # code here
```
