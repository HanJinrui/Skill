Given an array arr[] of length n. Find all possible unique permutations of the array.
Example 1:
Input: 
n = 3
arr[] = {1, 2, 1}
Output: 
1 1 2
1 2 1
2 1 1
Explanation:
These are the only possible unique permutations
for the given array.
Example 2:
Input: 
n = 2
arr[] = {4, 5}
Output: 
4 5
5 4
Your Task:
You don't need to read input or print anything. You only need to complete the function uniquePerms() that takes an integer n, and an array arr of size n as input and returns a sorted list of lists containing all unique permutations of the array.
Expected Time Complexity:  O(n*n!)
Expected Auxilliary Space: O(n*n!)
 
Constraints:
1 ≤ n ≤ 9
1 ≤ arr_{i} ≤ 10

Starter code:
```python
#User function Template for python3

class Solution:
    def uniquePerms(self, arr, n):
        # code here
```
