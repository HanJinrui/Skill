You are given two arrays A and B, both of length N.

You would like to choose exactly K distinct indices i_{1},i_{2}, \ldots, i_{K} such that \min(A_{i_{1}}+A_{i_{2}}+ \ldots + A_{i_{K}}, B_{i_{1}}+B_{i_{2}}+\ldots + B_{i_{K}}) is maximized. Find this maximum value.

------ Input Format ------ 

- The first line of input contains a single integer T, denoting the number of test cases. The description of T test cases follows.
- Each test case consists of 3 lines of input.
- The first line of each test case contains two space-separated integers N and K.
- The second line contains N space-separated integers A_{1}, A_{2}, \ldots, A_{N} denoting the elements of A.
- The third line contains N space-separated integers B_{1}, B_{2}, \ldots, B_{N} denoting the elements of B.

------ Output Format ------ 

For each test case, output a new line containing one integer — the required maximum value.

------ Constraints ------ 

$1 ≤ T ≤ 20$
$2 ≤ N ≤ 40$
$1 ≤ K ≤ N$
$1 ≤ A_{i}, B_{i} ≤ 40$

----- Sample Input 1 ------ 
3
5 3
4 2 3 1 4
3 2 5 5 1
4 2
1 2 3 4
4 3 2 1
6 3
8 10 3 6 7 2
4 8 4 1 1 6

----- Sample Output 1 ------ 
9
5
18

----- explanation 1 ------ 
Test Case $1$: One optimal choice of indices is $i_{1} = 1, i_{2} = 3, i_{3} = 5$. This gives $A_{1} + A_{3} + A_{5} = 11$ and $B_{1} + B_{3} + B_{5} = 9$.

Test Case $2$: One optimal choice of indices is $i_{1} = 1, i_{2} = 4$.

Test Case $3$: One optimal choice of indices is $i_{1} = 1, i_{2} = 2, i_{3} = 6$.
