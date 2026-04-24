Given an array of N integers Arr_{1}, Arr_{2}, ….Arr_{N}, count number of subarrays of Arr which are strictly increasing. 
A subarray Arr_{[i, j]} is the array where 1 <= i < j <= N is a sequence of integers of Arr_{i}, Arr_{i+1}, ….Arr_{j}. A subarray Arr_{[i, j]} is strictly increasing if Arr_{i} < Arr_{i+1} < Arr_{i+2} < ……. < Arr_{j}.
Example 1:
Input: 
N = 6
Arr[] = {1, 3, 3, 2, 3, 5}
Output: 4
Explanation:
(1,3), (2, 3), (3, 5) and (2, 3, 5)
are the only increasing subarrays.
Example 2:
Input: 
N = 2
Arr[] = {1 5} 
Output: 1
Explanation:(1, 5) is the only increasing
subarray.
Your Task:  
You don't need to read input or print anything. Your task is to complete the function countIncreasing() which takes the array of integers arr[] and n as parameters and returns a integer denoting the answer.
Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)
Constraints:
1 <= N <= 10^{7}
1 <= Arr_{i} <= 10^{7}

Starter code:
```python
#User function Template for python3
class Solution:

	def countIncreasing(self,arr, n):
		# code here
```
