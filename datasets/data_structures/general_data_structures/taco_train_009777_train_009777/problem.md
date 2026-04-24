Given an array Arr of length N. Determine if there exists an element in the array such that the sum of the elements on its left is equal to the sum of the elements on its right. If there are no elements to the left/right, then the sum is considered to be zero. 
Formally, find an i, such that, Arr_{1 }+ Arr_{2 }... Arr_{i-1} = Arr_{i+1 }+ Arr_{i+2 }... Arr_{N}.
Example 1:
Input:
N = 4
Arr[] = {1, 2, 3, 3}
Output: YES
Explanation: Consider i = 3, for [1, 2] 
sum is 3 and for [3] sum is also 3.
Example 2:
Input:
N = 2
Arr[] = {1, 5}
Output: NO
Explanation: No such index present.
Your Task:
Complete the function equilibrium() which takes array arr and size n, as input parameters and returns a string representing the answer(YES or NO). You don't to print answer or take inputs.
Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)
Constraints:
1 ≤ N ≤ 10^{5} 
1 ≤ Arr[i] ≤ 10^{6}

Starter code:
```python
#User function Template for python3
class Solution:

	def equilibrium(self,arr, n): 
    	# code here
```
