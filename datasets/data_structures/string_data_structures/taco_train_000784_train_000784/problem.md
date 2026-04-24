Given a sequence of strings, the task is to find out the second most repeated (or frequent) string in the given sequence.
Note: No two strings are the second most repeated, there will be always a single string.
Example 1:
Input:
N = 6
arr[] = {aaa, bbb, ccc, bbb, aaa, aaa}
Output: bbb
Explanation: "bbb" is the second most 
occurring string with frequency 2.
Example 2:
Input: 
N = 6
arr[] = {geek, for, geek, for, geek, aaa}
Output: for
Explanation: "for" is the second most
occurring string with frequency 2.
Your Task:
You don't need to read input or print anything. Your task is to complete the function secFrequent() which takes the string array arr[] and its size N as inputs and returns the second most frequent string in the array.
Expected Time Complexity: O(N*max(|S_{i}|).
Expected Auxiliary Space: O(N*max(|S_{i}|).
Constraints:
1<=N<=10^{3}

Starter code:
```python
#User function Template for python3

class Solution:
    def secFrequent(self, arr, n):
        # code here
```
