Given a n*m matrix A and a p*q matrix B, their Kronecker product C = A tensor B, also called their matrix direct product, is an (np)*(mq) matrix.
A tensor B
=
|a_{11}B    a_{12}B|            
|a_{21}B    a_{22}B|
=   
|a_{11}b_{11   } a_{11}b_{12   } a_{12}b_{11   } a_{12}b_{12}|
|a_{11}b_{21   } a_{11}b_{22   } a_{12}b_{21   } a_{12}b_{22}|
|a_{11}b_{31   } a_{11}b_{32   } a_{12}b_{31   } a_{12}b_{32}|
|a_{21}b_{11   } a_{21}b_{12   } a_{22}b_{11   } a_{22}b_{12}|
|a_{21}b_{21   } a_{21}b_{22   } a_{22}b_{21   } a_{22}b_{22}|
|a_{21}b_{31   } a_{21}b_{32   } a_{22}b_{31   } a_{22}b_{32}|
 
Example 1:
Input: 
n = 2, m = 2 
p = 2, q = 2
A = {{1, 2}, 
     {3, 4}}
B = {{0, 5}, 
     {6, 7}}
Output: {{0, 5, 0, 10}, 
         {6, 7, 12, 14}, 
         {0, 15, 0, 20}, 
         {18, 21, 24, 28}}
Explaination: If the multiplication process 
is followed then this will be the answer.
 
Your Task:
You do not need to read input or print anything. Your task is to complete the function kroneckerProduct() which takes n, m, p, q and A and B as input parameters and returns the resultant matrix.
 
Expected Time Complexity: O(n*m*p*q)
Expected Auxiliary Space: O(n*m*p*q)
 
Constraints:
1 ≤ n, m, p, q ≤ 20
1 ≤ A[i][j], B[i][j] ≤ 100

Starter code:
```python
#User function Template for python3

class Solution:
    def kroneckerProduct(self, n, m, p, q, A, B):
        # code here
```
