Given a string A and a dictionary of n words B, find out if A can be segmented into a space-separated sequence of dictionary words. 
Example 1:
Input:
n = 12
B = { "i", "like", "sam", "sung", "samsung",
"mobile","ice","cream", "icecream", "man",
"go", "mango" }, A = "ilike"
Output: 1
Explanation: The string can be segmented as
"i like".
Example 2:
Input: 
n = 12 
B = { "i", "like", "sam", "sung", "samsung",
"mobile","ice","cream", "icecream", "man", 
"go", "mango" }, A = "ilikesamsung" 
Output: 1
Explanation: The string can be segmented as 
"i like samsung" or "i like sam sung".
Your Task:
Complete wordBreak() function which takes a string and list of strings as a parameter and returns 1 if it is possible to break words, else return 0. You don't need to read any input or print any output, it is done by driver code.
Expected time complexity: O(n*l+|A|^{2}) where l is the leght of longest string present in the dictionary and |A| is the length of string A
Expected auxiliary space: O(|A| + k) , where k = sum of length of all strings present in B
 
Constraints:
1 <= N <= 12
1 <= s <=1000 , where s = length of string A
 The length of each word is less than 15.

Starter code:
```python
#User function Template for python3



class Solution:

    def wordBreak(self, A, B):

        # Complete this function
```
