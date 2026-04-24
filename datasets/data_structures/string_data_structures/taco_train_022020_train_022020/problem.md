Given a String S. Your task is to remove the given two strings(M and N) completely from the given string S. If String is completely removed then print -1.
Example 1:
Input:
S = abc
m = ab
n = bc
Output:
-1
Explanation: When we remove the two strings,
we get an empty string and thus the Output -1.
Example 2:
Input:
S =  abbbccab 
m = ab
n = bcc
Output:
b
Explanation: There are two instance of the String
"ab" in S and one occurence of "bcc". Removing
these from S we get "b".
Example 3:
Input:
S =  geeksforgks
m = for
n = gks
Output:
geeks
Explanation: After removing m and n from the String
S we get "geeks".
 
Your Task:
You don't need to read input or print anything. Your task is to complete the function demonitize() which takes Strings S , m and n as input and returns the answer.
 
Expected Time Complexity: O(|S|^{2})
Expected Auxiliary Space: O(|S|)
 
Constraints:
1 <= |S| <= 1000
1 <= |n| , |m| <= |S|

Starter code:
```python
#User function Template for python3



class Solution:

    def demonitize(self, S , m , n):

        # code here
```
