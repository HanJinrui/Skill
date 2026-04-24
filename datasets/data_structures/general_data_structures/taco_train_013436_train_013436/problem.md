Given a array a[] of non-negative integers. Count the number of pairs (i, j) in the array such that a[i] + a[j] < a[i]*a[j]. (the pair (i, j) and (j, i) are considered same and i should not be equal to j)
Example 1:
Input:
N=3
arr[] = {3, 4, 5} 
Output: 3
Explanation: Pairs are (3, 4) , (4, 5) and (3,5).  
 
Example 2:
Input:
N=3
arr[] = {1, 1, 1 } 
Output: 0
Your Task:
Since, this is a function problem. You don't need to take any input, as it is already accomplished by the driver code. You just need to complete the function CountPairs() that takes array arr and integer n as parameters and return the total number of pairs possible.
 
Expected Time Complexity: O(N).
Expected Auxiliary Space: O(1).
 
Constraints:
1 ≤ N ≤ 10^{5}

Starter code:
```python
#User function Template for python3


class Solution:
    def CountPairs (self,arr,n): 
        #code here.
```
