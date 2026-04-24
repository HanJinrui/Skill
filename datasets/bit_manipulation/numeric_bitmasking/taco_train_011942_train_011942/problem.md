Let's define Score of an array B of length M as \sum_{i=1}^{M} \sum_{j=i}^{M} f(i,j), where f(i,j) = B_{i} | B_{i+1} | \dots | B_{j} (Here | denotes the [bitwise OR operation]

You are given an array A, consisting of N distinct elements.

Find the sum of Score over all N! possible permutations of A.

Since the answer can be large, output it modulo 998244353.

------ Input Format ------ 

- The first line of input contains a single integer T - the number of test cases. The description of T test cases follow.
- The first line of each test case contains an integer N - the length of the array.
- The second line of each test case contains N space-separated distinct integers A_{1},A_{2}, \dots ,A_{n} representing the array A.

------ Output Format ------ 

For each test case, output the sum obtained modulo 998244353.

------ Constraints ------ 

$1 ≤ T ≤ 10^{5}$
$1 ≤ N ≤ 10^{5}$
$0 ≤ A_{i}  < 2^{30}$
- Sum of $N$ does not exceed $5 \cdot 10^{5}$ over all testcases

----- Sample Input 1 ------ 
2
2
2 3
4
343 10 7 47
----- Sample Output 1 ------ 
16
47160

----- explanation 1 ------ 
Test Case 1: Two permutations of $A$ are $[2,3]$ and $[3,2]$. 

- $Score$ of $[2, 3] = f(1, 1) + f(2, 2) + f(1, 2) = 2 + 3 + 2$ $|$ $3 = 8$.
- $Score$ of $[3, 2] = f(1, 1) + f(2, 2) + f(1, 2) = 3 + 2 + 3$ $|$ $2 = 8$. 

So, the required sum is $16$.
