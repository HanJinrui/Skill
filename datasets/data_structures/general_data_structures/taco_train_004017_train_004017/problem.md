Given an unsorted array Arr of size N that may contain duplicates. Also given a number K which is smaller than size of array. Find if array contains duplicates within K distance.
Example 1:
Input: 
K = 3, N = 8
Arr[] = {1, 2, 3, 4, 1, 2, 3, 4}
Output: False
Explanation: 
All duplicates are more than k distance
away.
Example 2:
Input: 
K = 3, N = 6
Arr[] = {1, 2, 3, 1, 4, 5}
Output: True
Explanation: 1 is repeated at distance 3.
Your Task:  
You don't need to read input or print anything. Your task is to complete the function checkDuplicatesWithinKÃ¢â¬â¹() which takes the array of integers arr[], n and k as parameters and returns boolean denoting the answer.
Expected Time Complexity: O(N)
Expected Auxiliary Space: O(N)
Constraints:
1 ≤ N ≤ 10^{6}
1 ≤ K ≤ N
1 ≤ Arr[i] ≤ 10^{7}

Starter code:
```python
#User function Template for python3
class Solution:

	def checkDuplicatesWithinK(self,arr, n, k):
		# code here
```
