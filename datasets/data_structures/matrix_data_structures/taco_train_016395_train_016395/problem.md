Given two square matrices Grid1 and Grid2 with the same dimensions(NxN).Check whether they are identical or not.
Example 1:
Input:
N=2
Grid1=[[1,2],[3,4]]
Grid2=[[1,2],[3,4]]
Output:
1
Explanation:
Both the matrices are identical,
so the answer is 1.
Example 2:
Input:
N=2
Grid1=[[1,2][3,4]]
Grid2=[[1,2][3,2]]
Output:
0
Explanation:
Both the matrices are not identical,
So, answer is 0.
Your Task:
You don't need to read input or print anything.Your task is to complete the function areMatricesIdentical() which takes the integer N and two 2D arrays Grid1 and Grid2 as input parameters and returns 1 if the matrices are identical.Otherwise,it returns 0.
Expected Time Complexity:O(N^{2})
Expected Auxillary Space:O(1)
Constraints:
1<=N<=1000
-1000<=Grid1[i][j],Grid2[i][j]<=1000,for 0<=i,j

Starter code:
```python
#User function Template for python3

class Solution:
    def areMatricesidentical(self,N,Grid1,Grid2):
        #code here
```
