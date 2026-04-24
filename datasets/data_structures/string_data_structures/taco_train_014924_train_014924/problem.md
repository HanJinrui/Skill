You are given an encoded string S of length N. The encoded string is mixed with some number of substring "LIE" and some secret message. You have to extract secret message from it by removing all the "LIE" substrings.
For example - "I AM COOL" is given as "LIEILIEAMLIELIECOOL".
Example 1:
Input: S = "LIEILIEAMLIELIECOOL"
Output: "I AM COOL"
Example 2:
Input: S = "LIELIEALIEBCLIE"
Output: "A BC"
Your Task:  
You don't need to read input or print anything. Your task is to complete the function ExtractMessage() which accepts a string as input parameter and returns a string containing secret message.
Expected Time Complexity: O(N)
Expected Auxiliary Space: O(N)
Constraints:
1 ≤ N ≤ 10^{6}
String contains only Upper Case Letters.

Starter code:
```python
#User function Template for python3

class Solution:

    def ExtractMessage(self, s):
        # code here
```
