There are p balls of type P, q balls of type Q and r balls of type R. Using the balls we want to create a straight line such that no two balls of same type are adjacent.
 
Example 1:
Input: p = 2, q = 2, r = 2
Output: 30
Explanation: There are 30 possible arrangements
of balls. Some of them are PQR, PRQ, PRP, PRQ,
PQR,...
Example 2:
Input: p = 1, q = 1, r = 1
Output: 6
Explanation: There are 6 possible arrangements
and these are PQR, PRQ, QPR, QRP, RPQ, RQP.
 
Your Task:
You don't need to read or print anything. Your task is to complete the function CountWays() which takes count of P type balls, Q type balls and R type balls and returns total number of possible arrangements such that no two balls of same type are adjacent modulo 10^{9} + 7.
 
Expected Time Complexity: O(N^{3}) where N = max(p, q, r)
Expected Space Complexity: O(N^{3})
 
Constranits: 
1 <= p, q, r <= 100

Starter code:
```python
#User function Template for python3



class Solution:

	def CountWays(self, p, q, r):

		# Code here
```
