Given string s consisting of only A’s and B’s. You can transform the given string to another string by toggling any character. Thus many transformations of the given string are possible. The task is to find the Weight of the maximum weight transformation.
The weight of a string is calculated using the below formula.
Weight of string = Weight of total pairs + weight of single characters - Total number of toggles.
 
Note: 
1. Two consecutive characters are considered a pair only if they are different.
2. Weight of a single pair (both characters are different) = 4
3. Weight of a single character = 1 
 
Example 1:
Input: s = "AA"
Output: 3
Explanation: Transformations of given 
string are "AA", "AB", "BA" and "BB". 
Maximum weight transformation is "AB" 
or "BA".  And weight is "One Pair - 
One Toggle" = 4-1 = 3.
Example 2:
Input: s = "ABB"
Output: 5
Explanation: Transformations are "ABB", 
"ABA", "AAB", "AAA", "BBB", "BBA", "BAB" 
and "BAA" Maximum weight is of original 
string 4 + 1 (One Pair + 1 character)
Your Task:  
You don't need to read input or print anything. Complete the function getMaxWeight() which takes string s as input and return an integer
Expected Time Complexity: O(N)
Expected Auxiliary Space: O(N)
Constraints:
1 ≤ N ≤ 10^{5}

Starter code:
```python
#User function Template for python3
class Solution:
	def getMaxWeight(self, s):
		# code here
```
