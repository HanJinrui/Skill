Given an array of n integers. We need to count all values of ‘k’ such that
arr[0] % k = arr[1] % k = ....... = arr[n-1] % k 
 
Example 1:
Input:
N=3
arr[] = {38, 6, 34} 
Output: 3
Explanation:
We can have values of k as 
1, 2 and 4.  
Example 2:
Input:
N=2
arr[] = {3, 2} 
Output: 1
Your Task:
Since, this is a function problem. You don't need to take any input, as it is already accomplished by the driver code. You just need to complete the function printEqualModNumbers() that takes array arr and integer n as parameters and returns the desired output.
Note- If values of k are infinite return -1.
 
Expected Time Complexity: O(N^{3/2}).
Expected Auxiliary Space: O(N).
 
Constraints:
1 ≤ N ≤ 10^{5}

Starter code:
```python
#User function Template for python3


class Solution:
    def printEqualModNumbers(self,arr, n):
        #code here.
```
