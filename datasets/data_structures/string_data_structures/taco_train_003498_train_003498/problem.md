There are N integers given in an array arr. You have to determine if it is possible to divide them in at most K groups, such that any group does not have a single integer more than twice.
Example 1:
Input: N = 5, K = 2
arr = {1, 1, 2, 5, 1}
Output: 1
Explaination: We can divide them in two groups in 
following way (1, 1, 2, 5) and (1).
Example 2:
Input: N = 3, K = 1
arr = {1, 1, 1}
Output: 0
Explaination: There can be only one group and 
three 1's. So it is not possible.
Your Task:
You do not need to read input or print anything. Your Task is to complete the function isPossible() which takes the value N, K and arr as input parameters and returns 1 if grouping is posible. Otherwise returns 0.
Expected Time Complexity: O(N)
Expected Auxiliary Space: O(N)
Constraints:
1 ≤ N ≤ 1000
1 ≤ K ≤ 256
1 ≤ arr[i] ≤ 32

Starter code:
```python
#User function Template for python3

class Solution:
    def isPossible(self, N, arr, K):
        # code here
```
