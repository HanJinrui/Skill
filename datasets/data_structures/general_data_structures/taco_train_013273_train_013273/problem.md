Given an array Arr[0 … N-1] containing N positive integers, a subarray Arr[i … j] is bitonic if there is a k with i <= k <= j such that A[i] <= Arr[i+1] <= ... <= Arr[k] >= Arr[k+1] >= ... A[j – 1] >= A[j]. Write a function that takes an array and array length as arguments and returns the length of the maximum length bitonic subarray.
For Example: In array {20, 4, 1, 2, 3, 4, 2, 10} the maximum length bitonic subarray is {1, 2, 3, 4, 2} which is of length 5.
Example 1:
Input:
N = 6
Arr[] = {12, 4, 78, 90, 45, 23}
Output: 5
Explanation: In the given array, 
bitonic subarray is 4 <= 78 <= 90
>= 45 >= 23.
Example 2:
Input:
N = 4
Arr[] = {10, 20, 30, 40}
Output: 4
Explanation: In the given array, 
bitonic subarray is 10 <= 20 <=
30 <= 40.
Your Task:
You don't need to read input or print anything. Your task is to complete the function bitonic() which takes the array of integers arr and n as parameters and returns an integer denoting the answer.
Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)
Constraints:
1 ≤ N ≤ 10^{5}
1 ≤ Arr[i] ≤ 10^{6}

Starter code:
```python
#User function Template for python3

class Solution:



	def bitonic(self,arr, n):

		# code here
```
