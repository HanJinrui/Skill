Given a sorted array of N positive integers, find the smallest positive integer S such that S cannot be represented as sum of elements of any subset of the given array set.
Example 1:
Input:
N = 3
Arr[] = {1, 2, 3}
Output: 7
Explanation: 7 is the smallest positive number 
for which any subset is not present with sum 7.
Example 2:
Input:
N = 6
Arr[] = {3, 6, 9, 10, 20, 28}
Output: 1
Explanation: 1 is the smallest positive number
for which any subset is not present with sum 1.
Your Task:
You don't need to read input or print anything. Your task is to complete the function findSmallest() which takes the array of integers arr and its size n as input parameters and returns an integer denoting the answer.
 
Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)
Constraints
1 <= N <= 10^{6}
0 <= Arr[i] <= 10^{15}

Starter code:
```python
#User function Template for python3



class Solution:

    def findSmallest(self, arr, n):

        # code here
```
