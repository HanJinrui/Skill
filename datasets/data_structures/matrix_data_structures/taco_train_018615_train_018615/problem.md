Given a NxM binary matrix consisting of 0s and 1s. Find if there exists a rectangle/ square within the matrix whose all four corners are 1. 
Example 1:
Input:
N = 4, M = 5
matrix[][] = 
{
{1 0 0 1 0},
{0 0 1 0 1},
{0 0 0 1 0}, 
{1 0 1 0 1}
} 
Output: Yes
Explanation:
Valid corners are at index (1,2), (1,4), (3,2), (3,4) 
Example 2:
Input:
N = 3, M = 3
matrix[][] = 
{{0 0 0},
{0 0 0},
{0 0 0}}
Output: No
Your Task:
You don't need to take input or print anything. Complete the function ValidCorners() that takes the given matrix as input parameter and returns a boolean value.
Constraints:
1 <= R, C <= 200
0 <= A[i] <= 1

Starter code:
```python
#User function Template for python3



class Solution:    

    def ValidCorner(self,matrix): 

        # Your code goes here
```
