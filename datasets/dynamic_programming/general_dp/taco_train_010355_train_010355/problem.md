Given a n*m matrix, find the maximum length path (starting from any cell) such that all cells along the path are in strictly increasing order.
We can move in 4 directions from a given cell (i, j), i.e., we can move to (i+1, j) or (i, j+1) or (i-1, j) or (i, j-1).
 
Example 1:
Input: matrix = {{1,2,9},{5,3,8},{4,6,7}}
Output: 7
Explanation: The longest increasing path is
{1,2,3,6,7,8,9}.
Example 2:
Input: matrix = {{3,4,5},{3,2,6},{2,2,1}}
Output: 4
Explanation: The longest increasing path is
{3,4,5,6}.
 
Your Task:
You don't need to read or print anyhting. Your task is to complete the function longestIncreasingPath() which takes matrix as input parameter and returns the length of the lonest increasing path.
Expected Time Complexity: O(n*m)
Expected Space Comeplxity: O(n*m)
 
Constraints:
1 <= n, m <= 100
1 <= matrix[i][j] <= 10^{4}

Starter code:
```python
#User function Template for python3



class Solution:

	def longestIncreasingPath(self, matrix):

		#Code here
```
