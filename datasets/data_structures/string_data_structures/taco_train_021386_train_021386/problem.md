Given a number N. The task is to return all the numbers less than or equal to N in increasing order, with the fact that absolute difference between any adjacent digits of number should be 1.
 
Example 1:
Input: N = 20
Output: 10 12
Explanation: Diff between 1 and 0 and
Diff between 1 and 2 is one.
Example 2:
Input:
N = 9
Output: -1
Explanation: No such number exist.
 
Your Task:
You don't need to read input or print anything. Your task is to complete the function absDifOne() which takes an integer as input and returns a list of numbers.
 
Expected Time Complexity : O(2^{Number of Digits in N})
Expected Auxiliary Space : O(2^{Number of Digits in N})
Constraints:
1 <= N <= 10^{12}

Starter code:
```python
#User function Template for python3

class Solution:
    def absDifOne(self, N):
        # code here
```
