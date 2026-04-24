Given an array of N integers, the task is to find all pairs with an absolute difference less than K.
NOTE: Pair (i, j) is considered same as (j, i)
Example 1:
Input : Arr[] = {1, 10, 4, 2}, K = 3
Output : 2
Explanation:
we have an array a[] = {1, 10, 4, 2} and 
K = 3 We can make only two pairs with a 
difference of less than 3.
(1, 2) and (4, 2). So, the answer is 2.
Example 2:
Input : Arr[] = {2, 3, 4}, K = 5
Output : 3
Your Task:
This is a function problem. The input is already taken care of by the driver code. You only need to complete the function countPairs() that takes an array (arr), sizeOfArray (n), the integer K, and return the number of pairs whose difference is less than K. The driver code takes care of the printing.
Expected Time Complexity: O(NLog(n)).
Expected Auxiliary Space: O(1).
 
Constraints:
2 ≤ N ≤ 10^{5}
0 ≤ K ≤ 10^{4}
1 ≤ A[i] ≤ 10^{5}

Starter code:
```python
#User function Template for python3

class Solution:
    def countPairs(self,a, n, k): 
          
        # Complete the function
```
