Given a weighted graph of N vertices numbered from 0 to N-1 in the form of adjacency matrix A[ ][ ] and two integers S denoting the number of source vertex and T denoting the number of sink vertex. The task is to find minimum capacity s-t cut of the given network. An s-t cut is a cut that requires the source node ‘S’ and the sink node ‘T’ to be in different subsets, and it consists of edges going from the source’s side to the sink’s side. The capacity of an s-t cut is defined by the sum of the capacity of each edge in the cut-set. In other words, you have to find out all the edges which has to be removed to make it impossible to reach the sink node from source node, and the edges you select should have a minimum sum of weights. You have to return all the edges included in the minimum capacity s-t cut and if there are no edges in minimum capacity s-t cut, return "-1".
Example 1:
Input:
N = 2
A[][] = [[0, 3],
         [0, 0]]
S = 0
T = 1
Output:
0 1
Explanation: We have to remove the edge going
from 0^{th} vertex to 1^{st} vertex.
 
Example 2:
Input:
N = 5
A[][] = [[0, 0, 0, 0, 0],
         [0, 0, 2, 3, 0],
         [0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0]]
S = 0
T = 4
Output:
-1
Explanation: There are no edges in 
minimum capacity s-t cut.
Your Task: 
You don't need to read input or print anything. Your task is to complete the function minimumCut() which takes the adjacency matrix A[ ][ ], source node number S, sink node number T and number of vertices N and returns a list of integers res[ ] where res[2*i-1] and res[2*i] denotes an edge in minimum capacity s-t cut where 1 ≤ i ≤ length(res)/2, if there are no edges in minimum capacity s-t cut, return only one integer "-1" in res[ ].
Expected Time Complexity: O(max_flow * N^{2})
Expected Auxiliary Space: O(N^{2})
Constraints:
1 ≤ N ≤ 50
0 ≤ S, T < N

Starter code:
```python
#User function Template for python3
    
class Solution:
    def minimumCut(self, A, S, T, N):
        #code here
```
