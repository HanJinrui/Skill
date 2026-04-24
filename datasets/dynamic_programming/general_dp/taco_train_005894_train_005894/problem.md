Given an array, an inversion is defined as a pair a[i], a[j] such that a[i] > a[j] and i < j. Given two numbers N and K, the task is to find the count of the number of permutations of first N numbers have exactly K inversion.
Note: Answer can be large, output answer modulo 10^{9} + 7
Example 1:
Input: N = 3, K = 1
Output: 2
Explanation: Total Permutation of first 
3 numbers, 123, 132, 213, 231, 312, 321
Permutation with 1 inversion : 132 and 213
Example 2:
Input: N = 3, K = 3
Output: 0
Explanation: No such permutation
Your Task:  
You don't need to read input or print anything. Complete the function numberOfPermWithKInversion() which takes N and K as input parameters and returns the integer value
Expected Time Complexity: O(N*K)
Expected Auxiliary Space: O(N*K)
Constraints:
1 ≤ N*K ≤ 10^{6}

Starter code:
```python
#User function Template for python3
class Solution:
	def numberOfPermWithKInversion(self, N,K):
		# code here
```
