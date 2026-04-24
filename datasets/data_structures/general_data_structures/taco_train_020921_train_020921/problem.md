Given an array arr of size n. The task is to choose k numbers from the array such that the absolute difference between the sum of chosen numbers and the sum of remaining numbers is maximum. 
Example 1:
Input:
n = 5, k = 2
arr[] = {8, 4, 5, 2, 10}
Output: 17
Explanation: If we select 2 and 4,
then abs((2+4) - (8+5+10)) = 17.
Example 2:
Input:
n = 8, k = 3
arr[] = {1, 1, 1, 1, 1, 1, 1, 1}
Output: 2
Explanation:
We can select any 3 1's.
Your Task:
You don't need to read input or print anything. Your task is to complete the function solve() which takes the array of integers arr, n and k as parameters and returns an integer denoting the answer.
Expected Time Complexity: O(n*Logn)
Expected Auxiliary Space: O(1)
Constraints:
1 <= k <= n <=10^{5}
1 <= arr[i] <= 10^{6}

Starter code:
```python
#User function Template for python3







class Solution:

    def solve(self, arr, n, k):

        # code here
```
