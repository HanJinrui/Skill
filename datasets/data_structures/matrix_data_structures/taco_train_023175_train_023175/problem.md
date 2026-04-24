Given a matrix of size n x m with 0’s and 1’s , you enter the matrix at cell (0,0) in left to right direction. whenever you encounter a 0 you retain in same direction , if you encounter a 1’s you have to change direction to right of current direction and change that 1 value to 0, you have to find out from which index you will leave the matrix at the end.
 
Example 1:
Input: matrix = {{0, 1, 0},
{0, 1, 1}, {0, 0, 0}}
Output: 1 0
Explanation: We enter at 0,0 then move towards 
0,1 and we encountered a 1 so we turned right 
and moved towards 1,1 and again we encountered 
a 1 so we turned right and moved towards 1,0 after
which we leave the matrix.
Example 2:
Input: matrix = {{0, 0}}
Output: 0 1
 
Your Task:
You don't need to read or print anyhting. Your task is to complete the function FindExitPoint() which takes the matrix as input parameter and returns a list containg the exit point.
 
Expected Time Complexity: O(n * m) where n is number of rows and m is number of columns.
Expected Space Complexity: O(1)
 
Constraints:
1 <= n, m <= 100

Starter code:
```python
#User function Template for python3

class Solution:
	def FindExitPoint(self, matrix):
		# Code here
```
