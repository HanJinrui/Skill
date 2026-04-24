------Read problems statements in Mandarin chinese
, Russian and Vietnamese as well. ------ 

Tumut, the best programmer in his village Applidz, invented a problem and decided to share it with you:

You are given two integer sequences $S_{1}, S_{2}, \dots, S_{N}$ and $T_{1}, T_{2}, \dots, T_{M}$ and an integer $x$. You are allowed to perform the following operation any number of times:
choose an element of $S$ and an element of $T$ (let's denote them by $S_{i}$ and $T_{j}$ respectively)
decrease both $S_{i}$ and $T_{j}$ by $x$, i.e. replace $S_{i}$ by $S_{i}-x$ and $T_{j}$ by $T_{j}-x$

Let's denote the minimum and maximum value in the sequence $S$ after performing the chosen operations (possibly none) by $minS$ and $maxS$ respectively. Similarly, let's denote the minimum and maximum value in $T$ after performing the chosen operations by $minT$ and $maxT$ respectively. The goal is minimizing the expression $(maxS+maxT) - (minS+minT)$. Compute the minimum value of this expression. 

------  Input ------
The first line of the input contains three space-separated integers $N$, $M$ and $x$.
The second line contains $N$ space-separated integers $S_{1}, S_{2} \dots S_{N}$.
The third line contains $M$ space-separated integers $T_{1}, T_{2} \dots T_{M}$.

------  Output ------
Print a single line containing one integer — the minimum possible value of the expression $(maxS+maxT) - (minS+minT)$.

------  Constraints ------
$1 ≤ N, M ≤ 5\cdot 10^{5}$
$1 ≤ S_{i} ≤ 10^{9}$ for each valid $i$
$1 ≤ T_{i} ≤ 10^{9}$ for each valid $i$
$1 ≤ x ≤ 10^{9}$

------  Subtasks ------
Subtask #1 (20 points):
$N, M ≤ 20$
$S_{i} ≤ 20$ for each valid $i$
$T_{i} ≤ 20$ for each valid $i$

Subtask #2 (30 points):
$N, M ≤ 1,000$
$S_{i} ≤ 1,000$ for each valid $i$
$T_{i} ≤ 1,000$ for each valid $i$

Subtask #3 (50 points): original constraints

----- Sample Input 1 ------ 
2 2 3
1 8
2 3
----- Sample Output 1 ------ 
2
----- explanation 1 ------ 
We can perform these two operations:
1. decrease $S_{2}$ and $T_{1}$ by $x$
2. decrease $S_{2}$ and $T_{2}$ by $x$

Afterwards, the sequence $S$ will be $[1, 2]$ and the sequence $T$ will be $[-1, 0]$. The resulting value of the given expression is $(2+0)-(1+(-1)) = 2$. It is impossible to obtain a smaller value no matter how many operations are performed.
