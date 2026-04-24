You need to calculate the following sum over Q queries.:
Assume array to be 1-indexed.
 
Example 1:
Input: nums = {2, 3, 4, 5, 1, 6, 7},
Query = {{2, 4}, {2, 6}}
Output: {64, 230}
Explanation: For the 1st query,
(1^{2} * 3 + 2^{2} * 4 + 3^{2} * 5) = 64.
For the second query
(1^{2} * 3 + 2^{2} * 4 + 3^{2} * 5 + 4^{2} * 1 + 5^{2} * 6) = 
230
 
Your Task:
You don't need to read or print anyhting. Your task is to complete the function FindQuery() which takes nums and Query as input parameter and returns a list containg the answer modulo 10^{9} + 7 for each query.
 
Expected Time Complexity: O(n)
Expected Space Complexity: O(n)
 
Constraints:
1 <= n <= 10^{5}
1 <= nums[i] <= 10^{5}
1 <= no. of queries <= 10^{4}

Starter code:
```python
#User function Template for python3

class Solution:
	def FindQuery(self, nums, Query):
		# Code here
```
