Given a tree with N nodes and (N-1) edges such that each edge has some weight. You are given Q queries. Each query contains a number X. Find the number of paths in which the edge that has the maximum weight is less than or equals to X. 
Note: Path from A to B and B to A are considered to be the same.
 
Example 1:
Input: N = 7
Tree = 
              1
           ^{3} /
            /
           2
          / \
       ^{1} /   \^{ 9}
        /     \
       3       4
      / \     
   ^{7} /   \ ^{8}
    /     \
   6       5
          /    
       ^{4} /
        /
       7
list of edges {start,end,weight}= 
{{1, 2, 3}, {2, 3, 1}, {2, 4, 9},
{3, 6, 7}, {3, 5, 8}, {5, 7, 4}}
Q = 3
queries[] = {1, 3, 5}
Output: 1 3 4
Explanation: 
Query 1: Path from 2 to 3
Query 2: Path from 1 to 2, 1 to 3, and 
         2 to 3
Query 3: Path from 1 to 2, 1 to 3, 2 to 3, 
         and 5 to 7
 
Example 2:
Input: N = 3
list of edges {start, end, weight}= 
{{1, 2, 1}, {2, 3, 4}}
Q = 1
queries[] = {3}
Output: 1
Explanation:
Query 1: Path from 1 to 2
 
Your Task:  
You don't need to read input or print anything. Complete the function maximumWeight()which takes integers N, list of edges where each edge is given by {start,end,weight}, an integer Q and a list of Q queries as input parameters and returns a list of integers denoting the maximum number of possible paths for each query. 
Expected Time Complexity: O(NlogN + QlogN)
Expected Auxiliary Space: O(N)
Constraints:
2 ≤ N ≤ 10^{4}
Number of edges = N - 1
1 ≤ val[i] ≤ 10^{5}

Starter code:
```python
#User function Template for python3



class Solution:

    def maximumWeight(self, n, edges, q, queries):

        # code here
```
