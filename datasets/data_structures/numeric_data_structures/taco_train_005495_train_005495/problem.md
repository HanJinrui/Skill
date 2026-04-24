Given a number n, the task is to find all 1 to n bit numbers with no consecutive 1's in their binary representation. 
 
Example 1:
Input: n = 3
Output: 1 2 4 5
Explanation: All numbers upto 2 bit are:
1 - 1
2 - 10
3 - 11
4 - 100
5 - 101
6 - 110
7 - 111
Here 3, 6 and 7 have consecutive 1's in their 
binary representation. 
Example 2:
Input: n = 2
Output: 1 2 
Explanation: All numbers upto 2 bit are:
1 - 1
2 - 10
3 - 11
Here 3 has consecutive 1's in it's
binary representation.
 
Your Task:
You don't need to read or print anything.Your task is to complete the function numberWithNoConsecutiveOnes() which takes n as input parameter and returns a list of numbers in increasing order which do not contains 1's in their binary reperesentation.
 
Expected Time Complexity: O(2^{n})
Expected Space Complexity: O(n)
 
Constraints:
1 <= n <= 20

Starter code:
```python
#User function Template for python3

class Solution:
	def numberWithNoConsecutiveOnes(self, n):
		# Code here
```
