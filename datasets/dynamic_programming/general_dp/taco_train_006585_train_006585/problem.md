Read problem statements in [Hindi], [Bengali], [Mandarin Chinese], [Russian], and [Vietnamese] as well.

Chef has a sequence $A_{1}, A_{2}, \ldots, A_{N}$. The sequence is circular, i.e. for each valid $i$, elements $A_{i}$ and $A_{i+1}$ are considered adjacent, and elements $A_{1}$ and $A_{N}$ are also considered adjacent. Initially, each element of this sequence is either $1$ or $0$.

You may perform some operations on this sequence. In one operation, you should choose an index $i$ such that $A_{i} = 1$ and move that $1$ to one of its adjacent elements, i.e. change $A_{i}$ to $0$, choose one of the elements adjacent to $A_{i}$ and increment it by $1$.

According to Chef, a sequence is *good* if all its elements are different from $1$. You have to tell Chef the minimum number of operations needed to turn the sequence $A$ into a good sequence or determine that it is impossible.

------  Input ------
The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
The first line of each test case contains a single integer $N$.
The second line contains $N$ space-separated integers $A_{1}, A_{2}, \ldots, A_{N}$.

------  Output ------
For each test case, print a single line containing one integer ― the minimum number of required operations, or $-1$ if it is impossible to make the sequence good.

------  Constraints ------
$1 ≤ T ≤ 10^{4}$
$3 ≤ N ≤ 10^{6}$
$0 ≤ A_{i} ≤ 1$ for each valid $i$
the sum of $N$ over all test cases does not exceed $2 \cdot 10^{6}$

------  Subtasks ------
Subtask #1 (30 points):
$N = 1,000$
the sum of $N$ over all test cases does not exceed $10^{4}$

Subtask #2 (70 points): original constraints

----- Sample Input 1 ------ 
3

3

0 0 0

4

1 0 1 0

5

1 1 0 1 0
----- Sample Output 1 ------ 
0

2

3
----- explanation 1 ------ 
Example case 1: The sequence is already good, so the answer is zero.

Example case 2: We can make the sequence good in two operations, e.g. $[1, 0, 1, 0] \rightarrow [0, 1, 1, 0] \rightarrow [0, 0, 2, 0]$.

Example case 3: We can make the sequence good in three operations, e.g. $[1, 1, 0, 1, 0] \rightarrow [0, 2, 0, 1, 0] \rightarrow [0, 2, 1, 0, 0] \rightarrow [0, 3, 0, 0, 0]$.
