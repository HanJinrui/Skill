Given an array nums[] of N positive integers. Find the minimum number of operations required to modify the array such that array elements are in strictly increasing order (A[i] < A[i+1]).
Changing a number to greater or lesser than original number is counted as one operation.
Example 1:
Input: nums[] = [1, 2, 3, 6, 5, 4]
Output: 2
Explanation: By decreasing 6 by 2 and
increasing 4 by 2, arr will be like
[1, 2, 3, 4, 5, 6] which is stricly 
increasing.
Example 2:
Input: nums[] = [1, 2, 3, 4]
Output: 0
Explanation: Arrays is already strictly
increasing.
 
Your Task:
You don't need to read or print anything. Your task is to complete the function min_opeartions() which takes the array nums[] as input parameter and returns the minimum number of opeartion needed to make the array strictly increasing.
 
Expected Time Complexity: O(n^2)
Expected Space Complexity: O(n)
 
Constraints: 
1 <= length of array <= 1000
1 <= arr[i] <= 1000000

Starter code:
```python
#User function Template for python3

class Solution:
	def min_operations(self,nums):
		# Code here
```
