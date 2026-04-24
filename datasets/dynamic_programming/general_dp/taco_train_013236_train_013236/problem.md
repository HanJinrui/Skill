Given an array arr of size N, the task is to sort this array in a minimum number of steps where in one step you can remove any array element from its position and insert it in any other position.
Example 1:
Input:
N = 7
arr[] = {2, 3, 5, 1, 4, 7, 6}
Output: 3
Explanation: 
We can sort above array in 3 insertion 
steps as shown below,
1 before array value 2
4 before array value 5
6 before array value 7
Example 2:
Input:
N = 4
arr[] = {4, 6, 5, 1}
Output: 2
Explanation: 
We can sort above array in 2 insertion 
steps as shown below, 
1 before array value 4
6 after array value 5 
Your Task:  
You don't need to read input or print anything. Complete the function minInsertions() which takes N and array arr as input parameters and returns the integer value
Expected Time Complexity: O(N^{2})
Expected Auxiliary Space: O(N)
Constraints:
1 ≤ N ≤ 10^{3}

Starter code:
```python
#User function Template for python3
class Solution:
	def minInsertions(self,arr, N):
		# code here
```
