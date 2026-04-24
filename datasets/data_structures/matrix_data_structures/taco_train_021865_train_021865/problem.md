The Postmaster wants to write a program to answer the queries regarding letter collection in a city. A city is represented as a matrix mat of size n*m. Each cell represents a house and contains letters which are denoted by a number in the cell. The program should answer q queries which are of following types:
1 i j : To sum all the letters which are at a 1-hop distance from the cell (i,j) in any direction
2 i j : To sum all the letters which are at a 2-hop distance from the cell (i,j) in any direction 
The queries are given in a 2D matrix queries[][].
 
Example 1:
Input: 
n = 4, m = 4
mat = {{1, 2, 3, 4}, 
       {5, 6, 7, 8}, 
       {9, 1, 3, 4}, 
       {1, 2, 3, 4}}
q = 2
queries = {{1 0 1}, 
           {2 0 1}}
Output: 22 29
Explaination: 
For the first query sum is 1+5+6+7+3 = 22. 
For the second query sum is 9+1+3+4+8+4 = 29.
 
Your Task:
You do not need to read input or print anything. Your task is to complete the function matrixSum() which takes n, m, mat, q and queries as input parameters and returns a list of integers where the ith value is the answers for ith query.
 
Expected Time Complexity: O(q)
Expected Auxiliary Space: O(q)
 
Constraints:
1 ≤ n, m ≤ 20
1 ≤ q ≤ 100

Starter code:
```python
#User function Template for python3



class Solution:

    def matrixSum(self, n, m, mat, q, queries):

        # code here
```
