Given an array A of N elements. The task is to find the greatest number S such that it is product of two elements of given array (S cannot be included in pair. Also, pair must be from different indices). 
Example 1:
Input :  arr[] = {10, 3, 5, 30, 35}
Output:  30
Explanation: 30 is the product of 10 and 3.
Example 2:
Input :  arr[] = {2, 5, 7, 8}
Output:  -1
Explanation: Since, no such element exists.
Example 3:
Input  :  arr[] = {10, 2, 4, 30, 35}
Output:  -1
 
Example 4:
Input :  arr[] = {10, 2, 2, 4, 30, 35}
Output:  4
Example 5:
Input  : arr[] = {17, 2, 1, 35, 30}
Output : 35
Your Task:  
You don't need to read input or print anything. Your task is to complete the function findGreatest() which takes the array arr[] and its size N as inputs and returns the answer. If the answer is not present in the array, return -1.
Expected Time Complexity: O(N. Log(N))
Expected Auxiliary Space: O(N)
Constraints:
1 ≤ N ≤ 10^{6}
1 ≤ A_{i} ≤ 10^{7}

Starter code:
```python
#User function Template for python3

class Solution:
        def findGreatest(self, arr, n):
        # Your code goes here
```
