Given two integers n and k, count the number of binary strings of length n where adjacent 1 appear k times. Since the answer can be huge, print it modulo 10^{9}+7.
Example 1:
Input:
n = 3 , k = 2
Output: 1
Explanation: Possible string is "111".
Example 2:
Input:
n = 5 , k = 2
Output: 6
Explanation: Possible strings are:
"00111" , "10111" , "01110"
"11100" , "11101" , "11011".
 
Your Task:
You don't need to read input or print anything. Your task is to complete the function countStrings() which accepts integers n and k as input parameter and returns the number of binary strings that satisfy the given condition.
Expected Time Complexity: O(n*k).
Expected Auxiliary Space: O(n*k). 
Constraints:
1 <= n, k <= 10^{3}

Starter code:
```python
#User function Template for python3



class Solution:

    def countStrings(self, n, k): 

        # code here
```
