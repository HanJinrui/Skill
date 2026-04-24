Given an array nums of n positive integers. The task is to find the longest Zig-Zag subsequence problem such that all elements of this are alternating (nums_{i-1} < nums_{i} > nums_{i+1} or nums_{i-1} > nums_{i} < nums_{i+1}).
 
Example 1:
Input: nums = {1,5,4}
Output: 3
Explanation: The entire sequenece is a 
Zig-Zag sequence.
Examplae 2:
Input: nums = {1,17,5,10,13,15,10,5,16,8}
Ooutput: 7
Explanation: There are several subsequences
that achieve this length. 
One is {1,17,10,13,10,16,8}.
 
Your Task:
You don't need to read or print anyhting. Your task is to complete the function ZigZagMaxLength() which takes the sequence  nums as input parameter and returns the maximum length of alternating sequence.
Expected Time Complexity: O(n)
Expected Space Complexity: O(1)
Constraints:
1 <= n <= 10^{5}

Starter code:
```python
#Initial Template for Python 3
class Solution:
	def ZigZagMaxLength(self, nums):
		# Code here
```
