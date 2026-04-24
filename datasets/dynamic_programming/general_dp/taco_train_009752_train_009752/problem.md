Given an array arr of size N, the task is to make strictly increasing and strictly decreasing subsequences from the array such that each array element belongs to increasing subsequence or decreasing subsequence, but not both, or can be part of none of the subsequence. Minimize the number of elements that are not part of any of the subsequences and find the count of such elements.
Example 1:
Input: N = 12, arr[] = {7, 8, 1, 2, 4,
                 6, 3, 5, 2, 1, 8, 7}
Output: 2
Explanation: 
Increasing sequence can be :
           {1, 2, 4, 5, 8}.
Decreasing sequence can be :
           {7, 6, 3, 2, 1}.
So, only 2 (8, 7) elements are left 
which are not part of either of 
the subsequences.
Example 2:
Input: N = 7, arr[] = {1, 4, 2, 3, 
                       3, 2, 4}
Output: 0
Explanation: 
Increasing sequence can be :
            {1, 2, 3, 4}. 
Decreasing sequence can be :
             {4, 3, 2}.
Your Task:  
You don't need to read input or print anything. Complete the function minCount() which takes N and array arr as input parameters and returns the integer value
Expected Time Complexity: O(N^{3})
Expected Auxiliary Space: O(N^{3})
Constraints:
1 ≤ N ≤ 10^{2}

Starter code:
```python
#User function Template for python3
class Solution:
	def minCount(self, arr, n):
		# code here
```
