Given an array arr[] of non-negative integers and an integer sum, the task is to count all subsets of the given array with a sum equal to a given sum.
Note: Answer can be very large, so, output answer modulo 10^{9}+7
Example 1:
Input: N = 6, arr[] = {2, 3, 5, 6, 8, 10}
       sum = 10
Output: 3
Explanation: {2, 3, 5}, {2, 8}, {10}
Example 2:
Input: N = 5, arr[] = {1, 2, 3, 4, 5}
       sum = 10
Output: 3
Explanation: {1, 2, 3, 4}, {1, 4, 5}, 
             {2, 3, 5}
Your Task:  
You don't need to read input or print anything. Complete the function perfectSum() which takes N, array arr[] and sum as input parameters and returns an integer value
Expected Time Complexity: O(N*sum)
Expected Auxiliary Space: O(N*sum)
Constraints:
1 ≤ N*sum ≤ 10^{6}
0<=arr[I]<=10^{6}

Starter code:
```python
#User function Template for python3

class Solution:

	def perfectSum(self, arr, n, sum):

		# code here
```
