In a given array A[] find the maximum value of (A[i] – i) - (A[j] – j) where i is not equal to j. 
i and j vary from 0 to N-1 and N is the size of input array A[].  The value of N is always greater than 1.
Example 1:
Input
N = 5
A[] = {9, 15, 4, 12, 13}
Output
12
Explanation:
(a[1]-1) - (a[2]-2) = (15-1)-(4-2) = 12
 
Example 2:
Input
N = 4
A[] = {3, 1, 2, 4}
Output
3
Explanation:
(a[1]-1) - (a[2]-2) = (3-1)-(1-2) = 3
 
Your Task:  
You don't need to read input or print anything. Your task is to complete the function maxVal() which takes the array A[] and its size N as inputs and returns the maximum value
 
Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)
 
Constraints:
2 ≤ N ≤ 10^{5}
1 ≤ A[i] ≤ 10^{5}

Starter code:
```python
#User function Template for python3

class Solution:
    def maxVal(self, a, n):
        #Code Here
```
