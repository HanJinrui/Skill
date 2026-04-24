Give a N*N square matrix, return an array of its anti-diagonals. Look at the example for more details.
Example 1:
Input:
N = 2
matrix[][] = {{1,2},
              {3,4}}
Output:
1 2 3 4
Explanation:
Matrix is as below:
1 2
3 4
Printing it in anti-diagonal form will lead
to the output as 1 2 3 4
Example 2:
Input:
N = 3
matrix[][] = {{1,2,3},
              {4,5,6},
              {7,8,9}}
Output:
1 2 4 3 5 7 6 8 9
Explanation: 
Matrix is as below:
1 2 3
4 5 6
7 8 9
Printing it in anti-diagonal form will lead
to the output as 1 2 4 3 5 7 6 8 9 
Your Task:
You dont need to read input or print anything. Complete the function antiDiagonalPattern() that takes matrix as input parameter and returns a list of integers in order of the values visited in the anti-Diagonal pattern. 
Expected Time Complexity: O(N * N)
Expected Auxiliary Space: O(N * N) for the resultant list only.
 
Constraints:
1 <= N <= 100
0 <= mat[i][j] <= 100

Starter code:
```python
#User function Template for python3



class Solution:

    def antiDiagonalPattern(self,matrix):

        # Code here
```
