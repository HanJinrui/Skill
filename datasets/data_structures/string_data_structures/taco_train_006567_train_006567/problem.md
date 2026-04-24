You are given 3 different arrays A, B, and C of the same size N. Find the number of indexes i such that:
A_{i} = B_{i }+ C_{k }
where k lies between [1, N].
 
Example 1:
Input: N = 3
A = {1, 2, 3}
B = {3, 2, 4}
C = {0, 5, -2}
Output: 2
Explaination: The possible i's are 0 and 1. 
1 = 3 + (-2) and 2 = 2 + 0.
 
Your Task:
You do not need to read input or print anything. Your task is to complete the function pairCount() which takes the value N and the arrays A, B, and C as input parameters and returns the number of possible indices.
 
Expected Time Complexity: O(N)
Expected Auxiliary Space: O(N)
 
Constraints:
1 ≤ N ≤ 10^{4}
1 ≤ A[i], B[i] ≤ 100
-100 ≤ C[i] ≤ 100

Starter code:
```python
#User function Template for python3



class Solution:

    def pairCount(self, N, A, B, C):

        # code here
```
