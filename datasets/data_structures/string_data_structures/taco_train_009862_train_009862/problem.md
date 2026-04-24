Given a string S, check if it is possible to convert it into a string that is the repetition of a substring with K characters. To convert, we can replace one substring of length K starting at index i (zero-based indexing), such that i is divisible by K, with K characters.
Example 1:
Input:
N = 4, K = 2, S = "bdac"
Output: 1
Explanation: We can replace either
"bd" with "ac" or "ac" with "bd"
Example 2:
Input: 
N = 5, K = 2, S = "abcde"
Output: 0
Explanation: Since N % K != 0, it's not 
possible to convert S into a string which
is a concatanation of a substring with 
length K.
Your Task:
You don't need to read input or print anything. Your task is to complete the function kSubstrConcat() which takes a string S, its length N and an integer K as inputs and return 1/0 accordingly.
Expected Time Complexity: O(N).
Expected Auxiliary Space: O(N).
Constraints:
2 <= K < N <= 100000

Starter code:
```python
#User function Template for python3

class Solution:

	def kSubstrConcat(self, n, s, k):

		# Your Code Here
```
