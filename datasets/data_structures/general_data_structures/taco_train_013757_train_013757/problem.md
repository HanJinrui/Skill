Given two strings, s1 and s2, composed of only English alphabets (both upper and lower cases), find the alphabets that occur in both the strings. find the common alphabets (if any).
Note:
1. Upper and lower alphabets are different.
2. Don't print any duplicates, even if they exit multiple times.
 
Example 1:
Input: s1 = "tUvGH", s2 = "Hhev"
Output: Hv
Explanation: The common letter are H and v. 
Hence output is, "Hv".
Example 2:
Input: s1 = "aabb", s2 = "ccll"
Output: nil
Explanation: There is nothing common, hence
the output is "nil".
 
Your Task:
You don't need to read or print anything. Your task is to complete the function commom_String() which takes s1 and s2 as input parameter and returns the letters which are common in both the strings in string format. If there is nothing common then returns "nil". The string which is returned must contain all the capital letters followed by small letter in ascending order.
 
Expected Time Complexity:  O(max(|s1|, |s2|)
Expected Space Complexity: O(k) where k is constant.
 
Constraints:
1 ≤ |s1|, |s2| ≤ 1000

Starter code:
```python
#User function Template for python3



class Solution:

	def common_String(self, s1, s2):

		# Code here
```
