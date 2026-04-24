Given an array arr[] of size N, the task is to check whether it is possible to obtain an array having distinct neighboring elements by swapping two neighboring array elements.
Example 1:
Input: N = 3, arr[] = {1, 1, 2}
Output:  YES
Explanation: Swap 1 (second last element) 
and 2 (last element), to obtain 1 2 1,
which has distinct neighbouring elements.
Example 2:
Input: N = 4, arr[] = {7, 7, 7, 7}
Output: NO
Explanation: We can't swap to obtain 
distinct elements in neighbor .
Your Task:
You don't need to read input or print anything. You just need to complete the function distinctAdjacentElement() that takes array arr[]  and its size N as input parameters and returns a boolean value denoting if distinct neighbours are possible or not. 
Note: The generated output is YES or NO according to the returned value.
 
Expected Time Complexity: O(N).
Expected Auxiliary Space: O(N).
 
Constraints:
2 ≤ N ≤ 10^{6}

Starter code:
```python
#User function Template for python3



class Solution:

    def distinctAdjacentElement(self,arr, n): 

        # code here
```
