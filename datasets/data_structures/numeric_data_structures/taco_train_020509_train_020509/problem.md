Given an array of N numbers. the task is to find minimum positive integer which can be assigned to every array element such that product of all elements of this new array is strictly greater than product of all elements of the initial array.
Example 1:
Input : Arr[] = {4, 2, 1, 10, 6}
Output : 4
Explanation:
Here we have an array [3, 2, 1, 4]
Product of elements of initial
array 3*2*1*4 = 24.
If x = 3 then 3*3*3*3 = 81, if x = 2 
then 2*2*2*2 =16. So minimal element = 3.
Example 2:
Input : Arr[] = {3, 2, 1, 4}
Output : 3
 
Your Task:
This is a function problem. The input is already taken care of by the driver code. You only need to complete the function findMin() that takes an array (arr), sizeOfArray (n), and return the minimum required element. The driver code takes care of the printing.
Expected Time Complexity: O(n * log(logn))
Expected Auxiliary Space: O(1).
Constraints:
2 ≤ N ≤ 10^{6}
1 ≤ A[i] ≤ 10^{6}

Starter code:
```python
#User function Template for python3

import math as m 
class Solution:
    # function to find the minimum element 
    def findMin(self, a, n): 
          
       #Complete the function
```
