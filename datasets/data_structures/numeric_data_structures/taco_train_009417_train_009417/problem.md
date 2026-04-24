Given an array a[ ] of N elements, the task is to find the number of ways to choose pairs {a[i], a[j]} such that their absolute difference is maximum.
Example:
Input:
N = 5
a[] = {3, 2, 1, 1, 3}
Output:
4
Explanation:
The maximum difference you can find is 2
which is from 3 - 1 = 2.
Number of ways of choosing it:
1) Choosing the first and third element
2) Choosing the first and fourth element
3) Choosing the third and fifth element
4) Choosing the fourth and fifth element
Hence, the answer is 4.
Your Task:
This is a function problem. The input is already taken care of by the driver code. You only need to complete the function countPairs() that take array(a) and sizeOfArray(N) as input parameters, and returns the count of pairs which has the maximum difference. The driver code takes care of the printing.
Expected Time Complexity: O(n).
Expected Auxiliary Space: O(1).
Constraints:
1 ≤ N ≤ 10^{5}
1 ≤ A[i] ≤ 10^{5}

Starter code:
```python
#User function Template for python3

def countPairs(a,n):
    return 0
```
