Read problem statements in [Hindi], [Bengali], [Mandarin Chinese], [Russian], and [Vietnamese] as well.

You are given $N$ sets of integers $A_{1}, A_{2}, \ldots, A_{N}$. For each valid $i$, let's denote the elements of the set $A_{i}$ by $\{c_{i,1}, c_{i,2}, \ldots, c_{i,|A_{i}|}\}$.

Find the number of ways to choose a sequence $(a_{1}, a_{2}, \ldots, a_{N})$ such that:
$a_{i} \in A_{i}$ for each valid $i$
$a_{i} \neq a_{i+1}$ for each valid $i$ and $a_{1} \neq a_{N}$

Since this number may be large, compute it modulo $998,244,353$.

------  Input ------
The first line of the input contains a single integer $N$.
$N$ lines follow. For each valid $i$, the $i$-th of these lines contains an integer $|A_{i}|$ followed by a space and $|A_{i}|$ space-separated non-negative integers $c_{i,1}, c_{i,2}, \ldots, c_{i,|A_{i}|}$.

------  Output ------
Print a single line containing one integer ― the number of ways to choose $(a_{1}, a_{2}, \ldots, a_{N})$, modulo $998,244,353$.

------  Constraints  ------
$2 ≤ N ≤ 200,000$
$|A_{i}| ≥ 1$ for each valid $i$
$|A_{1}| + |A_{2}| + \ldots + |A_{N}| ≤ 200,000$
$1 ≤ c_{i,j} ≤ 200000$ for each valid $i, j$

------  Subtasks ------
Subtask #1 (20 points): $N ≤ 100$

Subtask #2 (80 points): original constraints

----- Sample Input 1 ------ 
3

3 1 2 3

2 1 2

2 2 3
----- Sample Output 1 ------ 
3
----- explanation 1 ------ 
There are three possible sequences: $(1, 2, 3)$, $(2, 1, 3)$ and $(3, 1, 2)$.
