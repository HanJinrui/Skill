Given an array arr[] of size N of non negative integers. We can perform a swap operation on any two adjacent elements in the array. The task is to find the minimum number of swaps needed to sort the array in non - decreasing order. 
 
Example 1: 
Input:
N = 4
arr[] = {4, 1, 2, 3}
Output: 3
Explanation: (4,1,2,3) -> (1,4,2,3) -> 
(1,2,4,3) -> (1,2,3,4). Hence we need 
a total of 3 swaps to sort it in 
non - decreasing order.
Ã¢â¬â¹Example 2: 
Input: 
N = 4
arr[] = {4, 4, 2, 3}
Output: 4
Explanation: (4,4,2,3) -> (4,2,4,3) ->
(4,2,3,4) -> (2,4,3,4) -> (2,3,4,4,).
Hence we need a total of 4 swap to 
sort it in increasing order.
Your Task:  
You don't need to read input or print anything. Your task is to complete the function countSwaps() which takes the array arr[] and N as inputs and returns the minimum number of swaps needed to sort the array in non - decreasing order.
Expected Time Complexity: O(NlogN)
Expected Auxiliary Space: O(N)
Constraints:
1 ≤ N ≤ 10^{4}
1 ≤ arr[i] ≤ 10^{9}

Starter code:
```python
#User function Template for python3
class Solution:
	def countSwaps(self, arr, n):
		# code here
```
