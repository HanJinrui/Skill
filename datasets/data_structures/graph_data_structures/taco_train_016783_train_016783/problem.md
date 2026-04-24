Given an undirected Connected graph of V vertices and E edges.
A critical connection is an edge that, if removed, will make some nodes unable to reach some other nodes. Find all critical connections in the graph.
Note: There are many possible orders for the answer. You are supposed to print the edges in sorted order, and also an edge should be in sorted order too. So if there's an edge between node 1 and 2, you should print it like (1,2) and not (2,1).
Example 1:
Input:
Output:
0 1
0 2
Explanation: 
Both the edges in the graph are Crtical
connections.
Example 2:
Input:
Output:
2 3
Explanation:
The edge between nodes 2 and 3 is the only
Critical connection in the given graph.
Your task:
You dont need to read input or print anything. Your task is to complete the function criticalConnections() which takes the integer V denoting the number of vertices and an adjacency list adj as input parameters and returns  a list of lists containing the Critical connections in the sorted order.
Expected Time Complexity: O(V + E)
Expected Auxiliary Space: O(V)
Constraints:
1 ≤ V, E ≤ 10^{5}

Starter code:
```python
#User function Template for python3



class Solution:

    def criticalConnections(self, V, adj):

        # code here
```
