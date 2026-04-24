Given binary string s consisting of 0s and 1s only. You are allowed to do exactly one move that is you have to choose two indices i and j (1 ≤ i ≤ j ≤ |str| where |str| is string length) and toggle all the characters at position k where i ≤ k ≤ j. Toggling means changing 0 to 1 and 1 to 0. The task is to count the maximum possible number of 1's after exactly one move.
Example 1:
Input: s = "1010"
Output: 3
Explanation: You can make move on [2, 2]
or [2, 4]
Example 2:
Input: s = "0000"
Output: 4
Explanation: Make move on [1, 4]
Your Task:  
You don't need to read input or print anything. Complete the function maxOnes() which takes s as an input parameter and returns the maximum number of 1's count.
Expected Time Complexity: O(N)
Expected Auxiliary Space: O(N)
Constraints:
1 ≤ N ≤ 10^{5}

Starter code:
```python
#User function Template for python3
class Solution:
	def maxOnes(self, s):
		# code here
```
