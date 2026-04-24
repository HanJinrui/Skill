Given an array of distinct integers, write a program to find if there exist two pairs (a, b) and (c, d) such that ab = cd, where a, b, c and d are distinct elements. If such pairs exists then print 1 else -1.
 
Example 1:
Input:
N=7
arr[] = {3, 4, 7, 1, 2, 9, 8} 
Output: 1
Explanation:
Product of 4 and 2 is 8 and also,
the product of 1 and 8 is 8.  
 
Example 2:
Input:
N=6
arr[] = {1, 6, 3, 9, 2, 10} 
Output: 1
Your Task:
Since, this is a function problem. You don't need to take any input, as it is already accomplished by the driver code. You just need to complete the function findPairs() that takes array arr and n  as parameters and return 1 if any such pair is found otherwise return -1. 
 
Expected Time Complexity: O(N^{2}).
Expected Auxiliary Space: O(N^{2}).
 
Constraints:
1 ≤ N ≤ 10^{3}

Starter code:
```python
#User function Template for python3

class Solution:
    def findPairs(self,a,n):
        #code here.
```
