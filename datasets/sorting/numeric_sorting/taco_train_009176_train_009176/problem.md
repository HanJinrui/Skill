Given a sorted integer array Arr[ ] of size N, and three integers A, B, and C. The task is to find a new array  where i^{th} element of the new array = A * Arr[i] * Arr[i] + B * Arr[i] + C where A ≠ 0. You have to print the new array in sorted (ascending) order.
Example 1:
Input:
A = -1, B = 2, C = -1.
N = 6
Arr[] = {-1, 0, 1, 2, 3, 4}
Output: 
-9 -4 -4 -1 -1 0
Explanation: After applying the equation 
A * Arr[i] * Arr[i] + B * Arr[i] + C on every 
element Arr[i] we get {-4, -1, 0, -1, -4, -9}.
After sorting, we get {-9, -4, -4, -1, -1, 0}. 
Example 2:
Input:
A = 1, B = 1, C = 1.
N = 3
Arr[] = {1, 2, 3}
Output: 
3 7 13
Explanation: After applying the equation
A * Arr[i] * Arr[i] + B * Arr[i] + C on every
element Arr[i] we get {3, 7, 13} which is 
already sorted.
Your Task:  
You don't need to read input or print anything. Your task is to complete the function sortArray() which takes Arr[], N, A, B and C as input parameters and returns the sorted new list.
Expected Time Complexity: O(N)
Expected Auxiliary Space: O(N)
Constraints:
1 ≤ N ≤ 10^{6}
-10^{5} ≤ arr[i] ≤ 10^{5}

Starter code:
```python
#User function Template for python3



class Solution:

	def sortArray(self, arr, n, A, B, C):

		# Code here
```
