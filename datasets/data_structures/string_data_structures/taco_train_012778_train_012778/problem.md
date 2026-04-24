Given an array arr[] of N elements containing first N positive integers. You have to sort the integers in ascending order by the following operation. Operation is to pick an integer and place it at end or at start. Every such operation increases cost by one. The task is to sort the array in the minimum cost
Example 1:
Input: N = 3
arr = {2, 1, 3}
Output: 1
Explaination: Place 1 at start.
Example 2:
Input: N = 4
arr = {4, 3, 1, 2}
Output: 2
Explaination: First place 3 at end then 
4 at end.
Your Task:
You do not need to read input or print anything. Your task is to complete the function sortingCost() which takes the value N and arr as input parameters and returns the minimum cost of sorting.
Expected Time Complexity: O(N)
Expected Auxiliary Space: O(N)
Constraints:
1 ≤ N ≤ 10^{5}
1 ≤ arr[i] ≤ 10^{5}

Starter code:
```python
#User function Template for python3



class Solution:

    def sortingCost(self, N, arr):

        # code here
```
