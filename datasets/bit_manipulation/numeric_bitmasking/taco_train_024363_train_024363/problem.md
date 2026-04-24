Read problem statements in [Hindi], [Bengali], [Mandarin Chinese], [Russian], and [Vietnamese] as well.

You are given a sequence $A_{1}, A_{2}, \ldots, A_{N}$ and you have to perform the following operation exactly $X$ times:
Choose two integers $i$ and $j$ such that $1 ≤ i < j ≤ N$.
Choose a non-negative integer $p$.
Change $A_{i}$ to $A_{i} \oplus 2^{p}$, and change $A_{j}$ to $A_{j} \oplus 2^{p}$, where $\oplus$ denotes [bitwise XOR].

Find the lexicographically smallest sequence which can be obtained by performing this operation exactly $X$ times.

A sequence $B_{1}, B_{2}, \ldots, B_{N}$ is said to be lexicographically smaller than a sequence $C_{1}, C_{2}, \ldots, C_{N}$ if there is an index $i$ such that $B_{i} < C_{i}$ and for each valid $j < i$, $B_{j} = C_{j}$.

------  Input ------
The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
The first line of each test case contains two space-separated integers $N$ and $X$. 
The second line contains $N$ space-separated integers $A_{1}, A_{2}, \ldots, A_{N}$.

------  Output ------
For each test case, print a single line containing $N$ space-separated integers ― the lexicographically smallest obtainable sequence.

------  Constraints ------
$1 ≤ T ≤ 10$
$2 ≤ N ≤ 10^{5}$
$1 ≤ X ≤ 10^{9}$
$1 ≤ A_{i} ≤ 10^{9}$ for each valid $i$

------  Subtasks ------
Subtask #1 (30 points): $N ≤ 100$

Subtask #2 (70 points): original constraints

----- Sample Input 1 ------ 
1

3 3

2 2 3
----- Sample Output 1 ------ 
0 0 3
----- explanation 1 ------ 
Example case 1: The original sequence is $(2, 2, 3)$. Consider the following three operations:
- Choose $i = 1$, $j = 2$ and $p = 1$. Then, $A_{1}$ changes from $2$ to $2 \oplus 2^{1} = 0$ and similarly, $A_{2}$ changes from $2$ to $2 \oplus 2^{1} = 0$. Now the sequence is $(0, 0, 3)$.
- Next, choose $i = 1$, $j = 2$ and $p = 1$. Then, $A_{1}$ changes to $0 \oplus 2^{1} = 2$ and $A_{2}$ changes to $0 \oplus 2^{1} = 2$. The sequence is $(2, 2, 3)$.
- Next, again choose $i = 1$, $j = 2$ and $p = 1$. Then, $A_{1}$ changes to $2 \oplus 2^{1} = 0$ and $A_{2}$ changes to $2 \oplus 2^{1} = 0$. The sequence is $(0, 0, 3)$ again.

We can check that after exactly 3 operations, this is the lexicographically smallest sequence we can obtain.
