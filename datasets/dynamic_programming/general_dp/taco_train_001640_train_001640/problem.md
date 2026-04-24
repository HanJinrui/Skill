Given string s consisting of digits 0-9 and a number N, the task is to count the number of subsequences that are divisible by N.
Note: Answer can be large, output answer modulo 10^{9} + 7
Example 1:
Input: s = "1234", N = 4
Output: 4
Explanation: The subsequences 4, 12, 24 and 
124 are divisible by 4.
Example 2:
Input: s = "330", N = 6
Output: 4
Explanation: The subsequences 30, 30, 330 
and 0 are divisible by 6.
Your Task:  
You don't need to read input or print anything. Complete the function countDivisibleSubseq() which takes s and N as input parameters and returns the integer value
Expected Time Complexity: O(|s|*N)
Expected Auxiliary Space: O(|s|*N)
Constraints:
1 ≤ |s|*N ≤ 10^{6}

Starter code:
```python
#User function Template for python3
class Solution:
	def countDivisibleSubseq(self, s, N):
		# code here
```
