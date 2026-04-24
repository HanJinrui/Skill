Given a matrix A of dimensions NxN where every element is either O or X. Find the largest subsquare surrounded by X.
Example 1:
Input:
N=2
A=[[X,X][X,X]]
Output:
2
Explanation:
The largest square submatrix 
surrounded by X is the whole 
input matrix.
Example 2:
Input:
N=4
A=[[X,X,X,O],[X,O,X,X],
[X,X,X,O],[X,O,X,X]]
Output:
3
Explanation:
Here,the input represents following 
matrix of size 4 x 4
X X X O
X O X X
X X X O
X O X X
The square submatrix starting at 
(0,0) and ending at (2,2) is the 
largest submatrix surrounded by X.
Therefore, size of that matrix would be 3.
Your Task:
You don't need to read input or print anything. Your task is to complete the function largestSubsquare() which takes the integer N and the matrix A as input parameters and returns the size of the largest subsquare surrounded by 'X'.
Expected Time Complexity:O(N^{2})
Expected Auxillary Space:O(N^{2})
Constraints:
1<=N<=1000
A[i][j]={'X','O'}

Starter code:
```python
#User function Template for python3



class Solution:

    def largestSubsquare(self,N,A):

        #code here
```
