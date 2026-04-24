Given a binary string (consists of only 0 and 1). If there is “100” as a sub-string in the string, then we can delete this sub-string. The task is to find the length of longest sub-string which can be make removed?
Example 1:
Input  : 
str = "1011100000100"
Output :
6
Explanation :
Sub-strings present in str that can be make
removed 101{110000}0{100}. First
sub-string 110000-->100-->null, length is = 6.
Second sub-string 100-->null, length is = 3
 
Example 2:
Input  :
str = "111011"
Output :
0
Explanation :
There is no sub-string which can be make null.
 
Your Task:  
You don't need to read input or print anything. Your task is to complete the function longestNull() which takes the string S[] as inputs and returns the length of the longest string that can be removed.
 
Expected Time Complexity: O(N)
Expected Auxiliary Space: O(N)
Constraints:
1 ≤ string length ≤ 10^{4}
S[i] = {0, 1}

Starter code:
```python
#User function Template for python3

class Solution:
    def longestNull(self,S):
        # Your code goes here
```
