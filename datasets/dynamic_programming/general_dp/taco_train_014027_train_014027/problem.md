Given an integer N, the task is to find the number of binary strings of size 2*N in which each prefix of the string has more than or an equal number of 1's than 0's.
Note: The answer can be very large. So, output answer modulo 10^{9}+7
Example 1:
Input: N = 2
Output: 2
Explanation: 1100, 1010 are two 
such strings of size 4
Example 2:
Input: N = 3
Output: 5
Explanation: 111000 101100 101010 110010 
110100 are such 5 strings
Your Task:  
You don't need to read input or print anything. Complete the function prefixStrings() which takes N as input parameter and returns an integer value.
Expected Time Complexity: O(N^{2})
Expected Auxiliary Space: O(|N|)
Constraints:
1 ≤ |N| ≤ 10^{3}

Starter code:
```python
#User function Template for python3
class Solution:
	def prefixStrings(self, N):
		# code here
```
