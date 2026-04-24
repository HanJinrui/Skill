You are given a string ‘str’, the task is to check that reverses of all possible substrings of ‘str’ are present in ‘str’. If yes then the answer is 1, otherwise, the answer will be 0.
Example 1:
Input: n = 2, str = "ab"
Output: 0
Explanation: All substrings are "a",
"b","ab" but reverse of "ab" is not 
present in str.
Ã¢â¬â¹Example 2:
Input: n = 3, str = "aba"
Output: 1
Explanation: Reverse of all possible 
substring is present in str.
Your Task:  
You don't need to read input or print anything. Your task is to complete the function isReversibleÃ¢â¬â¹() which takes the string str and n (the length of str) as inputs and returns the answer.
Expected Time Complexity: O(n)
Expected Auxiliary Space: O(1)
Constraints:
1 ≤ n ≤ 2 * 10^{5}

Starter code:
```python
#User function Template for python3
class Solution:
    def isReversible(self, str, n):
        # code here
```
