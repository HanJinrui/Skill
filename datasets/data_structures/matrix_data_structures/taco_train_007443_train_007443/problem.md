Given a matrix mat of size R*C with 0 and 1s, find the largest rectangle of all 1s in the matrix. The rectangle can be formed by swapping any pair of columns of given matrix.
Example 1:
Input: 
R = 3, C = 5
mat[][] = {{0, 1, 0, 1, 0},
           {0, 1, 0, 1, 1},
           {1, 1, 0, 1, 0}};
Output: 6
Explanation: The largest rectangle's area
is 6. The rectangle can be formed by
swapping column  2 with 3. The matrix
after swapping will be
     0 0 1 1 0
     0 0 1 1 1
     1 0 1 1 0
Example 2:
Input:
R = 4, C = 5
mat[][] = {{0, 1, 0, 1, 0},
           {0, 1, 1, 1, 1},
           {1, 1, 1, 0, 1},
           {1, 1, 1, 1, 1}};
Output: 9
Your Task:
You don't need to read input or print anything. Your task is to complete the function maxArea() which takes the 2D array of booleans mat, r and c as parameters and returns an integer denoting the answer.
Expected Time Complexity: O(R*(R + C))
Expected Auxiliary Space: O(R*C)
Constraints:
1<= R,C <=10^{3}
0 <= mat[i][j] <= 1

Starter code:
```python
#User function Template for python3

class Solution:



	def maxArea(self,mat, r, c):

		# code here
```
