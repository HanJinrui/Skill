Given an array arr[] of size n such that array elements are distinct and in the range from 1 to n. The task is to count minimum number of move-to-front operations to arrange items as {1, 2, 3,… n}. The "move-to-front" operation is to pick any element arr[i] and place it at first position.
Example 1:
Input:
N=4
arr[] = {3, 2, 1, 4} 
Output: 2
Explanation:
We need to perform "move-to-front" on 1 
and 2 to make the array sorted.             
Example 2:
Input:
N=7
arr[] = {5, 7, 4, 3, 2, 6, 1} 
Output: 6
Your Task:
Since, this is a function problem. You don't need to take any input, as it is already accomplished by the driver code. You just need to complete the function minMoves() that takes array a and n as parameters and return the minimum number of move to front operation to sort the array.
 
Expected Time Complexity: O(N).
Expected Auxiliary Space: O(1).
 
Constraints:
1 ≤ N ≤ 10^{6}

Starter code:
```python
#User function Template for python3

class Solution:
    def minMoves(self,arr, n): 
        #code here.
```
