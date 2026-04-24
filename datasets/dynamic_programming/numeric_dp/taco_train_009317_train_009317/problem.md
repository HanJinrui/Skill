Given two positive integer N and M. The task is to find the number of arrays of size N that can be formed such that:
1. Each element is in the range [1, M].
2. All adjacent element are such that one of them divide the another i.e element A_{i} divides A_{i + 1 }or A_{i+1} divides A_{i}.
Example 1:
Input: 
N = 3
M = 3
Output : 
17
Explanation:
{1,1,1}, {1,1,2}, {1,1,3}, {1,2,1}, 
{1,2,2}, {1,3,1}, {1,3,3}, {2,1,1},
{2,1,2}, {2,1,3}, {2,2,1}, {2,2,2},
{3,1,1}, {3,1,2}, {3,1,3}, {3,3,1}, 
{3,3,3} are possible arrays.
Example 2:
Input: 
N = 1
M = 10 
Output: 
10
Explanation: 
{1}, {2}, {3}, {4}, {5}, 
{6}, {7}, {8}, {9}, {10}
are possible arrays.
Your Task:
You don't need to read input or print anything. Your task is to complete the function count() which take integers N and M as input parameter and returns the total the number of arrays of size N that can be formed with given constraints. The return value may long so take modulo 10^{9}+7. 
Expected Time Complexity: O(N*M*Log M) 
Expected Space Complexity: O(N*M) 
Constraints:
1<=N,M<=100

Starter code:
```python
#User function Template for python3

class Solution:
    def count(self,N, M):
        # code here
```
