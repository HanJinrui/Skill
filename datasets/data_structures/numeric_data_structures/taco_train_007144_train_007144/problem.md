Consider an array with N elements and value of all the elements is zero. We can perform following operations on the array.
         1. Incremental operations: Choose 1 element from the array and increment its value by 1.
         2. Doubling operation: Double the values of all the elements of array.
Given an array arr[] of integers of size N. Print the smallest possible number of operations needed to change the original array containing only zeroes to arr[].
Example 1:
Input:
N = 3
arr[] = {16, 16, 16}
Output: 7
Explanation: First apply an incremental 
operation to each element. Then apply the 
doubling operation four times. 
Total number of operations is 3+4 = 7.
Example 2:
Input:
N = 2
arr[] = {2, 3}
Output: 4
Explanation: To get the target array 
from {0, 0}, we first increment both 
elements by 1 (2 operations), then double 
the array (1 operation). Finally increment 
second element (1 more operation). 
Total number of operations is 2+1+1 = 4.
Your Task:
You don't need to read input or print anything. Your task is to complete the function countMinOperations() which takes arr[] and n as input parameters and returns an integer denoting the answer.
Expected Time Complexity: O(N*log(max(Arr[i])))
Expected Auxiliary Space: O(1)
Constraints:
1 ≤ N ≤ 10^{4}
1 ≤ arr[i] ≤ 5*10^{4}

Starter code:
```python
#User function Template for python3



class Solution:

    def countMinOperations(self, arr, n):

        # code here
```
