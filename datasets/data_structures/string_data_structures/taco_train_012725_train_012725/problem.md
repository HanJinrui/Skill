Given a matrix containing lower alphabetical characters only of size n*m. We need to count the number of palindromic paths in the given matrix.
A path is defined as a sequence of cells starting from top-left cell and ending at bottom-right cell. We are allowed to move to right and down only from current cell.
 
Example 1:
Input: matrix = {{a,a,a,b},{b,a,a,a},{a,b,b,a}}
Output: 3
Explanation: Number of palindromic paths are 3 
from top-left to bottom-right.
aaaaaa (0, 0) -> (0, 1) -> (1, 1) -> (1, 2) -> 
(1, 3) -> (2, 3)    
aaaaaa (0, 0) -> (0, 1) -> (0, 2) -> (1, 2) -> 
(1, 3) -> (2, 3)    
abaaba (0, 0) -> (1, 0) -> (1, 1) -> (1, 2) -> 
(2, 2) -> (2, 3)
Example 2:
Input: matrix = {{a,b},{c,d}}
Output: 0
Explanation: There is no palindromic paths.
 
Your Task:
You don't need to read or print anyhting. Your task is to complete the function countPalindromicPaths() which takes the matrix as input parameter and returns the total nuumber of palindromic paths modulo 10^{9} + 7.
 
Expected Time Complexity: O(n^{2}*m^{2})
Space Complexity: O(n*m)
 
Constraints:
1 ≤ n, m ≤ 100

Starter code:
```python
#User function Template for python3

class Solution:
	def countOfPalindromicPaths(self, matrix):
		# Code here
```
