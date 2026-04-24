Given an unsorted array Arr of size N. Find the minimum number of removals required such that twice of minimum element in the array is greater than or equal to the maximum in the array.
Example 1:
Input:
N = 9
Arr[] = {4,5,100,9,10,11,12,15,200}
Output: 4
Explanation: In the given array 4 elements 
4, 5, 200 and 100 are removed from the
array to make the array such that
2*minimum >= max (2*9 > 15).
Example 2:
Input:
N = 4
Arr[] = {4,7,5,6}
Output: 0
Explanation: We don't need to remove any
element as  4*2 > 7 (Note that min = 4,
max = 7).
Your Task:
You don't need to read input or print anything. Your task is to complete the function minRemoval() which takes the array of integers arr and n as parameters and returns an integer denoting the answer.
Expected Time Complexity: O(N*logN)
Expected Auxiliary Space: O(1)
Constraints:
1 ≤ N ≤ 10^{7}
1 ≤ Arr_{i} ≤ 10^{9}

Starter code:
```python
#User function Template for python3
class Solution:

	def minRemoval(self,arr, n):
		# code here
```
