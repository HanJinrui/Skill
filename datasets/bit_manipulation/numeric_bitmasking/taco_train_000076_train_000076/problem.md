Read problems statements in [Hindi], [Mandarin Chinese], [Russian], [Vietnamese], and [Bengali] as well.

You are given an odd integer $N$ and two integer sequences $A_{1}, A_{2}, \ldots, A_{N}$ and $B_{1}, B_{2}, \ldots, B_{N}$.

Your task is to reorder the elements of $B$, forming a new sequence $C_{1}, C_{2}, \ldots, C_{N}$ (i.e. choose a permutation $P_{1}, P_{2}, \ldots, P_{N}$ of the integers $1$ through $N$, where $C_{i} = B_{P_{i}}$ for each valid $i$), in such a way that the following condition holds: $(A_{1} \oplus C_{1}) = (A_{2} \oplus C_{2}) = \ldots = (A_{N} \oplus C_{N})$, where $\oplus$ denotes bitwise XOR. Find one such reordered sequence or determine that it is impossible.

------  Input ------
The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
The first line of each test case contains a single integer $N$.
The second line contains $N$ space-separated integers $A_{1}, A_{2}, \ldots, A_{N}$.
The third line contains $N$ space-separated integers $B_{1}, B_{2}, \ldots, B_{N}$.

------  Output ------
For each test case:
If there is no valid way to reorder the sequence $B$, print a single line containing the integer $-1$.
Otherwise, print a single line containing $N$ space-separated integers $C_{1}, C_{2}, \ldots, C_{N}$. If there are multiple solutions, you may find any one.

------  Constraints ------
$1 ≤ T ≤ 10$
$1 ≤ N ≤ 10^{5}$
$N$ is odd
$0 ≤ A_{i} ≤ 10^{6}$ for each valid $i$
$0 ≤ B_{i} ≤ 10^{6}$ for each valid $i$

----- Sample Input 1 ------ 
1

5

3 1 2 4 5

2 4 5 1 3
----- Sample Output 1 ------ 
3 1 2 4 5
