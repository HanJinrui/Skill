Utkarsh has a [permutation] P of \{0, 1, 2, \dots, N-1\}.

He wants to find the number of pairs (L, R) (1 ≤ L < R ≤ N) such that swapping the elements P_{L} and P_{R} does not change the [MEX] of any [subarray].

Formally, find the number of pairs (L, R) (1≤ L < R ≤ N) satisfying the following condition:
Let P' be the permutation defined as follows:
- P'_i = P_{i} for i \in \{1, 2, 3, \ldots, N}\setminus \{L, R\}
- P'_L = P_{R}
- P'_R = P_{L}
mex(\{P_{i}, P_{i+1}, \ldots, P_{j}\}) = mex(\{P'_i, P'_{i+1}, \ldots, P'_j\}) for every 1 ≤ i ≤ j ≤ N

For example, let N = 7 and P = [2, 5, 1, 0, 3, 6, 4]. Then,
Swapping the pair (1, 3), i.e swapping P_{1} = 2 and P_{3} = 1 would give us the permutation P' = [1, 5, 2, 0, 3, 6, 4]. This changes the mex of the subarray [3, 4], because mex(\{P_{3}, P_{4}\}) = mex(\{1, 0\}) = 2 but mex(\{P'_3, P'_4\}) = mex(\{2, 0\}) = 1, so (1, 3) is not a valid swap.
Swapping the pair (4, 7) gives us the permutation P' = [2, 5, 1, 4, 3, 6, 0]. This changes the mex of the subarray [7, 7] — mex(\{P_{7}\}) = mex(\{4\}) = 0 and mex(\{P'_7\}) = mex(\{0\}) = 1. So, (4, 7) is also not a valid pair.
However, it can be verified that the pair (2, 6) is valid — swapping P_{2} and P_{6} gives us the permutation P' = [2, 6, 1, 0, 3, 5, 4], and mex(P[i \ldots j]) = mex(P'[i \ldots j]) for every 1 ≤ i ≤ j ≤ 7.

------ Input Format ------ 

- The first line of input will contain an integer T, the number of test cases. Then the test cases follow.
Description of each test case:
- The first line contains a single integer N, denoting the size of the permutation P.
- The second line contains N space-separated integers P_{1}, P_{2}, \ldots, P_{N}, denoting the permutation P.

------ Output Format ------ 

For each test case, output on a new line the number of pairs (L,R) such that swapping P_{L} and P_{R} does not change the MEX of any subarray.

------ Constraints ------ 

$1 ≤ T ≤ 10^{4}$
$2 ≤ N ≤ 10^{5}$
- Sum of $N$ over all test cases does not exceed $2 \cdot 10^{5}$
- It is guaranteed that $P$ is a permutation of $\{0, 1, 2, \dots, N-1\}$.

----- Sample Input 1 ------ 
2
4
0 1 2 3
7
2 5 1 0 3 6 4

----- Sample Output 1 ------ 
0
1

----- explanation 1 ------ 
Test case $1$: There are no valid pairs.

Test case $2$: There is only one valid pair, $(L,R) = (2,6)$, i.e, swapping $P_{2} = 5$ and $P_{6} = 6$ to obtain the permutation $[2, 6, 1, 0, 3, 5, 4]$.
