Given an array of N elements, find the minimum number of insertions to convert the given array into a co-prime array adjacent pair-wise. 
Example 1:
Input: A[] = {2, 7, 28}
Output: 1
Explanation: Here, 1st pair = {2, 7}
are co-primes( gcd(2, 7) = 1). 2nd pair
= {7, 28} are not co-primes, insert 9
between them. gcd(7, 9) = 1 and
gcd(9, 28) = 1.
Example 2:
Input: A[] = {5, 10, 20}
Output : 2
Explanation: Here, there is no pair
which are co-primes. Insert 7 between
(5, 10) and 1 between (10, 20).
Your Task:
The input is already taken care of by the driver code. You only need to complete the function countCoPrime() that takes an array (arr), sizeOfArray (n), and return the minimum number of insertions. The driver code takes care of the printing.
Expected Time Complexity: O(N).
Expected Auxiliary Space: O(1).
Constraints:
1<=N<=10^{5}
1<=arr<=10^{5}

Starter code:
```python
#User function Template for python3
class Solution:
	def countCoPrime (self,arr,  n):
		#Complete the function
```
