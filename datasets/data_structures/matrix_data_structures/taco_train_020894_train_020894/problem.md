Consider the generalized Fibonacci number G, which is dependent on a, b and c as follows :-
G(1) = 1, G(2) = 1. G(n) = aG(n-1) + bG(n-2) + c.
Your task is to calculate G(n)%m for given values of n and m.
Example 1:
Input:
a = 3, b = 3, c = 3, n = 3, m = 5
Output:
4
Explanation:
G(1) = 1 and G(2) = 1 
G(3) = 3*G(2) + 3*G(1) + 3 = 3*1 + 3*1 + 3 = 9
We need to return answer modulo 5, so 9%5 = 4, is the answer.
Example 2:
Input:
a = 2, b = 2, c = 2, n = 4, m = 100
Output:
16
Explanation:
G(1) = 1 and G(2) = 1 
G(3) = 2*G(2) + 2*G(1) + 2 = 2*1 + 2*1 + 2 = 6
G(4) = 2*G(3) + 2*G(2) + 2  = 2*6 + 2*1 + 2 = 16
We need to return answer modulo 100, so 16%100 = 16, is the answer.
Your Task:
You don't need to read input or print anything. Your task is to complete the function genFibNum() which takes 5 Integers a, b, c, n, and m as input and returns G(n)%m.
Expected Time Complexity: O(logn)
Expected Auxiliary Space: O(1)
Constraints:
1 <= a,b,c,n,m <= 10^{9}+7

Starter code:
```python
#User function Template for python3



class Solution:

    def genFibNum(self, a, b, c, n, m):

        # code here
```
