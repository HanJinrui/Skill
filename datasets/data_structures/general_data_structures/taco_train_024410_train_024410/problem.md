Chef has an array A of length N.

Let F(A) denote the maximum frequency of any element present in the array.

For example:

If A = [1, 2, 3, 2, 2, 1], then F(A) = 3 since element 2 has the highest frequency  = 3.
If A = [1, 2, 3, 3, 2, 1], then F(A) = 2 since highest frequency of any element is 2.

Chef can perform the following operation at most once:

Choose any [subsequence] S of the array such that every element of S is the same, say x. Then, choose an integer y and replace every element in this subsequence with y.

For example, let A = [1, 2, 2, 1, 2, 2]. A few examples of the operation that Chef can perform are:
[1, \textcolor{red}{2, 2}, 1, 2, 2] \to [1, \textcolor{blue}{5, 5}, 1, 2, 2]
[1, \textcolor{red}{2}, 2, 1, \textcolor{red}{2, 2}] \to [1, \textcolor{blue}{19}, 2, 1, \textcolor{blue}{19, 19}]
[\textcolor{red}{1}, 2, 2, 1, 2, 2] \to [\textcolor{blue}{2}, 2, 2, 1, 2, 2]

Determine the minimum possible value of F(A) Chef can get by performing the given operation at most once.

------ Input Format ------ 

- The first line of input will contain a single integer T, denoting the number of test cases.
- Each test case consists of two lines of input.
- The first line of each test case contains a single integer N denoting the length of array A.
- The second line contains N space-separated integers denoting the array A.

------ Output Format ------ 

For each test case, output the minimum value of F(A) Chef can get if he performs the operation optimally.

------ Constraints ------ 

$1 ≤ T ≤ 5000$
$2 ≤ N ≤ 10^{5}$
$1 ≤ A_{i} ≤ N$
- The sum of $N$ over all test cases won't exceed $2 \cdot 10^{5}$.

----- Sample Input 1 ------ 
3
4
1 2 1 2
5
1 1 1 1 1
6
1 2 2 1 2 2

----- Sample Output 1 ------ 
2
3
2

----- explanation 1 ------ 
Test case $1$: Chef cannot reduce the value of $F(A)$ by performing any operation.

Test case $2$: Chef can perform the operation $[\textcolor{red}{1}, 1, \textcolor{red}{1}, 1, \textcolor{red}{1}] \to [\textcolor{blue}{2}, 1, \textcolor{blue}{2}, 1, \textcolor{blue}{2}]$.
The value of $F(A)$ in this case is $3$, which is the minimum possible.

Test case $3$: Chef can perform the operation $[1, \textcolor{red}{2, 2}, 1, 2, 2] \to [1, \textcolor{blue}{5, 5}, 1, 2, 2]$. The value of $F(A)$ in this case is $2$, which is the minimum possible.
