Given an undirected graph with V nodes and E edges. The task is to check if there is any cycle in undirected graph.
Note: Solve the problem using disjoint set union(dsu).
 
Example 1:
Input: 
Output: 1
Explanation: There is a cycle between 0->2->4->0
Example 2:
Input: 
Output: 0
Explanation: The graph doesn't contain any cycle
 
Your Task:
You don't need to read or print anyhting. Your task is to complete the function detectCycle() which takes number of vertices in the graph denoting as V and adjacency list denoting as adj and returns 1 if graph contains any cycle otherwise returns 0.
Expected Time Complexity: O(V + E)
Expected Space Complexity: O(V)
 
Constraints:
1 ≤ V, E ≤ 10^{4}

Starter code:
```python
class Solution:



    #Function to detect cycle using DSU in an undirected graph.

	def detectCycle(self, V, adj):

		#Code here
```
