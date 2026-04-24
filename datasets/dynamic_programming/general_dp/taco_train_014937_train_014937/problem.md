There are N points on the road ,you can step ahead by 1 or 2 . Find the number of ways you can reach at point N. 
Example 1:
Input: N = 4
Output: 5
Explanation: Three ways to reach at 4th
point. They are {1, 1, 1, 1}, {1, 1, 2},
{1, 2, 1} {2, 1, 1}, {2, 2}.
Example 2:
Input: N = 5
Output: 8
Explanation: Three ways to reach at 5th
point. They are {1, 1, 1, 1, 1},
{1, 1, 1, 2}, {1, 1, 2, 1}, {1, 2, 1, 1},
{2, 1, 1, 1}{1, 2, 2}, {2, 1, 2}, {2, 2, 1}
Your Task:
You don't need to read or print anyhting. Your task is to complete the function nthPoint() which takes N as input parameter and returns the total number of ways modulo 10^{9} + 7 to reach at Nth point.
Expected Time Complexity: O(N)
Expected Space Complexity: O(N)
Constraints:
1 ≤ N ≤ 10^{4}

Starter code:
```python
#User function Template for python3



class Solution:

	def nthPoint(self,n):

		# Code here
```
