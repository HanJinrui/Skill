You have an array a consisting of n distinct positive integers, numbered from 1 to n. Define p_k as $$$p_k = ∑_{1 ≤ i, j ≤ k} a_i mod a_j, where x \bmod y denotes the remainder when x is divided by y. You have to find and print p_1, p_2, \ldots, p_n$$$. 

Input

The first line contains n — the length of the array (2 ≤ n ≤ 2 ⋅ 10^5).

The second line contains n space-separated distinct integers a_1, …, a_n (1 ≤ a_i ≤ 3 ⋅ 10^5, a_i ≠ a_j if i ≠ j). 

Output

Print n integers p_1, p_2, …, p_n. 

Examples

Input


4
6 2 7 3


Output


0 2 12 22


Input


3
3 2 1


Output


0 3 5
