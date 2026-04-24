Let's play a game!! Given a matrix mat[][] with n x m elements. Your task is to check that matrix is Super Similar or not. To perform this task you have to follow these Rules: Firstly all even index rows to be Rotated left and odd index rows to right, And Rotation is done X times(Index starting from zero). Secondly, After all the Rotations check if the initial and the final Matrix are same Return 1 else 0.
Example 1:
Input: n = 2, m = 2
mat = {{1, 2}, 
       {5, 6}}
x = 1
Output: 0
Explanation: Matrix after rotation:
mat = {{ 2, 1}
       { 6, 5}}
After one rotation mat is 
not same as the previous one.
 
Example 2:
Input: n = 2, m = 4
mat = {{1, 2, 1, 2}, 
       {2, 1, 2, 1}}
x = 2
Output: 1
Explanation: After two rotation mat is 
same as the previous one.
Your Task:
You do not need to read input or print anything. Your task is to complete the function isSuperSimilar() which takes n, m, x and the matrix as input parameter and returns 1 if the initial and the final Matrix are same else returns 0.
Expected Time Complexity: O(n*m)
Expected Auxiliary Space: O(n*m)
Constraints:
1 ≤ n, m ≤ 30
1 ≤ mat[i][j] ≤ 100 
1 ≤ x ≤ 20

Starter code:
```python
#User function Template for python3



class Solution:

    def isSuperSimilar(self, n, m, mat, x):

        # code here
```
