Given two integers N, M and a 2D matrix Mat of dimensions NxM, the task is to find the maximum sum of
an hourglass.
An hourglass is made of 7 cells in the following form.
    A B C
      D
    E F G
Example 1:
Input:
N=3,M=3
Mat=[[1,2,3],[4,5,6],[7,8,9]]
Output:
35
Explanation:
There is only one hour glass which is
1 2 3
   5
7 8 9 and its sum is 35.
Example 2:
Input:
N=2,M=3
Mat=[[1,2,3],[4,5,6]]
Output:
-1
Explanation:
There are no hour glasses in this matrix.
Your Task:
You don't need to read input or print anything. Your task is to complete the function findMaxSum() which takes the two integers N, M, and the 2D matrix Mat as input parameters and returns the maximum sum of an hourglass in the matrix. If there are no hourglasses, it returns -1.
Expected Time Complexity:O(N*M)
Expected Auxillary Space:O(1)
Constraints:
1<=N,M,Mat[i][j]<=1000

Starter code:
```python
#User function Template for python3



class Solution:

    def findMaxSum(self,N,M,Mat):

        #code here
```
