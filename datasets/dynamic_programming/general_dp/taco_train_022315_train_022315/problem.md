You have a rectangular grid mat of dimension 2 x N. You need to find out the maximum sum such that no two chosen numbers are adjacent, vertically, diagonally or horizontally.
Example 1:
Input: N = 3
mat = {{1, 4, 5}, 
       {2, 0, 0}}
Output: 7
Explaination: Optimal choice is (2, 5).
Example 2:
Input: N = 2
mat = {{1, 2}, 
       {3, 4}}
Output: 4
Explaination: Optimal choice is (4).
Your Task:
You do not need to read input or print anything. Your task is to complete the function maxSum() which takes the value N and grid mat as input parameters and returns the maximum sum.
Expected Time Complexity: O(N)
Expected Auxiliary Space: O(N)
Constraints:
1 ≤ N ≤ 10000
1 ≤ mat[i][j] ≤ 70

Starter code:
```python
#User function Template for python3

class Solution:
    def maxSum(self, N, mat):
        # code here
```
