Read problem statements in [Hindi], [Bengali], [Mandarin Chinese], [Russian], and [Vietnamese] as well.

You are given a permutation $p_{1}, p_{2}, \ldots, p_{N}$ of the integers $1$ through $N$. You may perform up to $K$ operations of the following type:
Choose three pairwise distinct valid indices $i_{1}, i_{2}, i_{3}$. Note that these indices do not have to be chosen in increasing order.
Let's denote the values of $p_{i_{1}}$, $p_{i_{2}}$ and $p_{i_{3}}$ before this operation by $v_{1}$, $v_{2}$ and $v_{3}$ respectively.
Change $p_{i_{2}}$ to $v_{1}$, $p_{i_{3}}$ to $v_{2}$ and $p_{i_{1}}$ to $v_{3}$. In other words, perform a cyclic right shift on the elements $p_{i_{1}}, p_{i_{2}}, p_{i_{3}}$ in this order.

For example, the permutation $(1,4,3,2,5)$ can be changed to the permutation $(1,5,3,4,2)$ in one operation by choosing $i_{1} = 2$, $i_{2} = 4$ and $i_{3} = 5$.

Your task is to sort the permutation in increasing order. Note that you do not have to minimise the number of performed operations.

------  Input ------
The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
The first line of each test case contains two space-separated integers $N$ and $K$.
The second line contains $N$ space-separated integers $p_{1}, p_{2}, \ldots, p_{N}$.

------  Output ------
For each test case:
If it is impossible to sort the given permutation using at most $K$ operations, print a single line containing the integer $-1$.
Otherwise, first, print a line containing a single integer $M$ ($0 ≤ M ≤ K$) ― the number of operations you want to perform.
Then, print $M$ lines describing these operations. For each $i$ ($1 ≤ i ≤ M$), the $i$-th of these lines should contain three space-separated integers $a_{i}$, $b_{i}$ and $c_{i}$ (pairwise distinct; $1 ≤ a_{i}, b_{i}, c_{i} ≤ N$) ― the indices on which the $i$-th operation is performed.

------  Constraints ------
$1 ≤ T ≤ 100$
$3 ≤ N ≤ 2 \cdot 10^{5}$
$1 ≤ p_{i} ≤ N$ for each valid $i$
$p_{1}, p_{2}, \ldots, p_{N}$ are pairwise distinct
the sum of all $N$ over all test cases does not exceed $2 \cdot 10^{5}$

------  Subtasks ------
Subtask #1 (5 points):
$p_{i} = N-i+1$ for each valid $i$
$N ≤ 400$
$K = N^{2}$

Subtask #2 (45 points): $K = \lfloor \frac{2N}{3} \rfloor$

Subtask #3 (50 points): $K = \lfloor \frac{N}{2} \rfloor$

----- Sample Input 1 ------ 
1

4 2

3 2 4 1
----- Sample Output 1 ------ 
1

1 3 4
----- explanation 1 ------ 
Example case 1: We can sort the permutation by performing one cyclic right shift operation on the indices $1$, $3$ and $4$.
