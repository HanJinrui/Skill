Given an array of integers, we need to find out all possible ways construct non-degenerate triangle using array values as its sides. If no such triangle can be formed then return 0.
 
Example 1:
Input : [5, 4, 3, 1, 2]
Output : 3
Explanation:
Sides of possible triangle are
(2 3 4), (3 4 5) and (2 4 5)
 
Example 2:
Input : [4, 1, 2]
Output : 0 
No triangle is possible from given
array values
Your Task:  
You don't need to read input or print anything. Your task is to complete the function noOfTriangles() which takes the vector v[] and its size N as inputs and returns the count of all possible triangles that can be formed using the values from the array.
Expected Time Complexity: O(N^{2})
Expected Auxiliary Space: O(1)
Constraints:
1 ≤ N ≤ 10^{3}
1 ≤ A[i] ≤ 10^{4}

Starter code:
```python
#User function Template for python3

class Solution:
    def noOfTriangles( self, arr, n):
    # Your code goes here
```
