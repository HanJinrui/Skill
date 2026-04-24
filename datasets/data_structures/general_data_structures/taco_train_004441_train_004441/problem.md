Given an array of binary integers, suppose these values are kept on the circumference of a circle at an equal distance. The task is to tell whether is it possible to draw a regular polygon using only 1s as its vertices or not.
If yes then print 1 else -1.
 
Example 1:
Input:
N=6
arr[] = { 1, 1, 1, 0, 1, 0 }
Output:  1
Explanation: 
Using 1's at 1st, 3rd and 5th index
we can make a triangle.
 
Example 2:
Input:
N=10
arr[] = { 1, 0, 1, 0, 1, 0, 1, 0, 1, 1 }
Output:  1
Your Task:
Since, this is a function problem. You don't need to take any input, as it is already accomplished by the driver code. You just need to complete the function isPolygonPossible() that takes array arr and integer N as parameters and returns 1 if it is possible to make a regular polygon else -1.
 
Expected Time Complexity: O(N^{5}^{/2}).
Expected Auxiliary Space: O(1).
Constraints:
1 ≤ N ≤ 50

Starter code:
```python
#User function Template for python3

class Solution:
    def isPolygonPossible(self,arr, N) :
        #code here
```
