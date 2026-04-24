Given an undirected graph with n vertices and connections between them. Your task is to find whether you can come to same vertex X if you start from X by traversing all the vertices atleast once and use all the paths exactly once.
 
Example 1:
Input: paths = {{0,1,1,1,1},{1,0,-1,1,-1},
{1,-1,0,1,-1},{1,1,1,0,1},{1,-1,-1,1,0}}
Output: 1
Exaplanation: One can visit the vertices in
the following way:
1->3->4->5->1->4->2->1
Here all the vertices has been visited and all
paths are used exactly once.
 
Your Task:
You don't need to read or print anything. Your task is to complete the function isPossible() which takes paths as input parameter and returns 1 if it is possible to visit all the vertices atleast once by using all the paths exactly once otherwise 0.
 
Expected Time Complexity: O(n^{2})
Expected Space Compelxity: O(1)
 
Constraints:
1 <= n <= 100
-1 <= paths[i][j] <= 1
Note: If i == j then paths[i][j] = 0. If paths[i][j] = 1 it means there is a path between i to j. If paths[i][j] = -1 it means there is no path between i to j.

Starter code:
```python
#User function Template for python3



class Solution:

	def isPossible(self, paths):

		# Code here
```
