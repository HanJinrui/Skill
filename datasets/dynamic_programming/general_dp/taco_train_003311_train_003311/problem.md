Given string s containing characters as integers only, the task is to delete all characters of this string in a minimum number of steps wherein one step you can delete the substring which is a palindrome. After deleting a substring remaining parts are concatenated.
Example 1:
Input: s = "2553432"
Output: 2
Explanation: In first step remove "55", 
then string becomes "23432" which is a 
palindrome.
Example 2:
Input: s = "1234"
Output: 4
Explanation: Remove each character in 
each step
Your Task:  
You don't need to read input or print anything. Complete the function minStepToDeleteString() which string s as input parameters and returns the integer value
Expected Time Complexity: O(|s|^{3})
Expected Auxiliary Space: O(|s|^{2})
Constraints:
1 ≤ |s| ≤ 10^{3}

Starter code:
```python
#User function Template for python3

class Solution:

	def minStepToDeleteString(self, s):

		# code here
```
