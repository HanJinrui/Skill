Given two sequences, one is increasing sequence a[] and another a normal sequence b[], find the K-th missing element in the increasing sequence which is not present in the given sequence. If no K-th missing element is there output -1
 
Example 1:
Input : Arr[] = {0, 2, 4, 6, 8, 10, 12, 14, 15}
Brr[] = {4, 10, 6, 8, 12} and K = 3
Output : 14
Explanation:
The numbers from increasing sequence that
are not present in the given sequence are 0, 2, 14, 15.
The 3rd missing number is 14.
Example 2:
Input : Arr[] = {1, 2, 3, 4, 5}
Brr[] = {5, 4, 3, 1, 2} and K = 3
Output : -1
Your Task:
This is a function problem. The input is already taken care of by the driver code. You only need to complete the function MissingNumber() that takes an array (a), another array (b), an element K, size of first array (n), size of the second array (m), and return the Kth missing number in an array a, if you can't find it return -1. The driver code takes care of the printing.
Expected Time Complexity: O(n + m).
Expected Auxiliary Space: O(m).
Constraints:
1 ≤ n,m,k ≤ 10^{5}
1 ≤ a[i] ≤ 10^{8}
1 ≤ b[i] ≤ 10^{3}

Starter code:
```python
#User function Template for python3



class Solution:

    def MissingNumber(self, a, b, k, n1, n2): 

      

        # Complete the function
```
