Consider an N \times M binary matrix A, i.e. a grid consisting of N rows numbered 1 to N from top to bottom and M columns numbered 1 to M from left to right, whose cells take the value 0 or 1. Let (i, j) denote the cell on the i-th row and j-th column.

The matrix is said to be *special* if for every cell (i, j), the following condition holds simultaneously:
A_{i, j} = 1 if and only if the sum of row i is equal to the sum of column j. More formally, A_{i, j} = 1 iff \displaystyle\sum_{k=1}^{M} A_{i, k} = \sum_{k=1}^{N} A_{k, j}

The *specialty* of a *special* matrix is defined to be the sum of values of all cells in the matrix. Given N and M, find the minimum *specialty* of a *special* matrix among all *special* binary matrices consisting of N rows and M columns.

------ Input Format ------ 

- The first line of input will contain a single integer T, denoting the number of test cases.
- Each test case consists of a single line containing N and M — the number of rows and the number of columns.

------ Output Format ------ 

For each test case, output on a new line the minimum *specialty* of a *special* matrix among all *special* binary matrices consisting of N rows and M columns.

------ Constraints ------ 

$1 ≤ T ≤ 10^{5}$
$1 ≤ N, M ≤ 5000$

----- Sample Input 1 ------ 
2
3 3
4 5
----- Sample Output 1 ------ 
5
10
----- explanation 1 ------ 
Test case 1: One such *special* binary matrix with minimum *specialty* is:

Test case 2: One such *special* binary matrix with minimum *specialty* is:
