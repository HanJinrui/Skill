You are given a prime number p, n integers a_1, a_2, …, a_n, and an integer k. 

Find the number of pairs of indexes (i, j) (1 ≤ i < j ≤ n) for which (a_i + a_j)(a_i^2 + a_j^2) ≡ k mod p.

Input

The first line contains integers n, p, k (2 ≤ n ≤ 3 ⋅ 10^5, 2 ≤ p ≤ 10^9, 0 ≤ k ≤ p-1). p is guaranteed to be prime.

The second line contains n integers a_1, a_2, …, a_n (0 ≤ a_i ≤ p-1). It is guaranteed that all elements are different.

Output

Output a single integer — answer to the problem.

Examples

Input


3 3 0
0 1 2


Output


1

Input


6 7 2
1 2 3 4 5 6


Output


3

Note

In the first example:

(0+1)(0^2 + 1^2) = 1 ≡ 1 mod 3.

(0+2)(0^2 + 2^2) = 8 ≡ 2 mod 3.

(1+2)(1^2 + 2^2) = 15 ≡ 0 mod 3.

So only 1 pair satisfies the condition.

In the second example, there are 3 such pairs: (1, 5), (2, 3), (4, 6).
