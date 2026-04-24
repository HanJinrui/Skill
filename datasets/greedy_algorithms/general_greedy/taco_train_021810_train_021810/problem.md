You are given a string str of lower case english alphabets. You can choose any two characters in the string and replace all the occurences of the first character with the second character and replace all the occurences of the second character with the first character. Your aim is to find the lexicographically smallest string that can be obtained by doing this operation at most once.
 
Exampel 1:
Input: str = "ccad"
Output: "aacd"
Explanation: In ccad, we choose ‘a’ and ‘c’
and after doing the replacement operation 
once we get, aacd and this is the 
lexicographically smallest string possible.
Example 2:
Input: "abba"
Output: "abba"
Explanation: In abba, we can get baab after 
doing the replacement operation once for ‘a’ 
and ‘b’ but that is not lexicographically 
smaller than abba and so the answer is abba.
 
Your Task:
You don't need to read or print anything. Your task is to complete the function LexicographicallyMinimum() which takes string str as input parameter and retruns the lexicographically minimum possible string after doing the operation.
 
Expected Time Complexity: O(n)
Expected Space Complexity: O(1)
 
Constraints:
1 <= |str| <= 10^{4}

Starter code:
```python
#User function Template for python3

class Solution:
	def LexicographicallyMinimum(self, str):
		# Code here
```
