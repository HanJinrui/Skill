Given a tree with n nodes and edge connection between them . The tree is rooted at node 1. Your task is to remove minimum number of edges from the given tree such that the tree converts into disjoint union tree so that nodes of connected component left is divisible by 2.
 
Example 1:
Input: n = 10, edges = {{2,1},{3,1},{4,3},{5,2}
,{6,1},{7,2},{8,6},{9,8},{10,8}}
Output: 2
Explanation: Take two integers at a time i.e. 2 
is connected with 1, 3 is connected with 1,4 is 
connected with 3, 5 is connected with 2 and so 
on. Fig will understand you better.
Original tree:
   
After removing edge 1-3 and 1-6. So ans is 2
because all nodes are even
 
Your Task:
You don't need to read or print anyhting. Your task is to complete the function minimumEdgeRemove() which takes n and edges as input parameter and returns the minimum number of edges which is removed to make the tree disjoint union tree such that the tree converts into disjoint union tree so that nodes of connected component left is divisible by 2.
 
Expected Time Compelxity: O(n)
Expected Space Comeplxity: O(1)
 
Constraints:
1 <= n <= 10^{4}

Starter code:
```python
#User function Template for python3

class Solution:
	def minimumEdgeRemove(self, n, edges):
		#Code here
```
