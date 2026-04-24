Given two strings in lowercase, your task is to find minimum number of manipulations required to make two strings anagram without deleting any character. If two strings contains same data set in any order then strings are called Anagrams.
Example 1:
Input:
S1 = "aba", S2 = "baa", N = 3
Output: 0
Explanation: Both the strings are already
anagrams.
Ã¢â¬â¹Example 2:
Input: 
S1 = "ddcf", S2 = "cedk", N = 4
Output: 2
Explanation: We can change 'e' and 'k' in
S2 to 'd' and 'f' to make both the strings
anagram. 
Your Task:
You don't need to read input or print anything. Your task is to complete the function minManipulation() which takes the strings S1 and S2 and their length N as inputs and returns the minimum number of manipulations required to make both the strings anagram.
Expected Time Complexity: O(N).
Expected Auxiliary Space: O(1).
Constraints:
1<=N<=10^{5}
|S1| = |S2| = N
|S| represents the length of the string S.

Starter code:
```python
#User function Template for python3
class Solution:
    def minManipulation(self, N, S1, S2): 
        # code here
```
