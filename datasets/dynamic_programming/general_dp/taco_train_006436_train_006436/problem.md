You are given an array A = [A_{1}, A_{2}, \ldots, A_{N}] containing distinct positive integers.

Let B be a [permutation] of A. Define the *value* of B to be
\sum_{i=1}^N (B_{i} \bmod{B_{i+1}})

where B_{N+1} is treated to be B_{1}.

Find the maximum *value* across all permutations of A.

------ Input Format ------ 

- The first line of input contains a single integer T, denoting the number of test cases. The description of T test cases follows.
- Each test case consists of two lines of input.
- The first line of each test case contains an integer N — the size of A.
- The second line of each test case contains N space-separated integers — the elements of A.

------ Output Format ------ 

- For each test case, output a new line containing the answer — the maximum possible value across all permutations of A.

------ Constraints ------ 

$1 ≤ T ≤ 10^{3}$
$2 ≤ N ≤ 2\cdot 10^{3}$
$1 ≤ A_{i} ≤ 10^{15}$
$A_{i} \neq A_{j}$ for $i \neq j$
- The sum of $N$ across all test cases won't exceed $2\cdot 10^{3}$.

----- Sample Input 1 ------ 
2
2
5 13
4
11 5 14869010166 19007432007

----- Sample Output 1 ------ 
8
14869010184

----- explanation 1 ------ 
Test case $1$: The value of any permutation is $(5 \bmod 13) + (13 \bmod 5) = 5 + 3 = 8$.

Test case $2$: The $6$ cyclic permutations of the given array and their corresponding values are:
- $[5, 11, 14869010166, 19007432007]$ with value $14869010184$
- $[5, 14869010166, 11, 19007432007]$ with value $28$
- $[11, 5, 14869010166, 19007432007]$ with value $14869010175$
- $[11, 14869010166, 5, 19007432007]$ with value $20$
- $[14869010166, 5, 11, 19007432007]$ with value $4138421858$
- $[14869010166, 11, 5, 19007432007]$ with value $4138421857$

Among these, the highest value is $14869010184$.
