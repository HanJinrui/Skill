Read problem statements in [Hindi], [Bengali], [Mandarin Chinese], [Russian], and [Vietnamese] as well.

There is a secret sequence $A_{1}, A_{2}, \ldots, A_{N}$. We do not know the elements of this sequence, but we know another sequence $B_{1}, B_{2}, \ldots, B_{N-1}$ such that $B_{i} = A_{i} + A_{i+1}$ for each valid $i$.

You should process $Q$ queries. In each query, you are given two indices $p$ and $q$; your task is to compute $A_{p} + A_{q}$ or determine that there is not enough information to uniquely determine this sum.

------  Input ------
The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
The first line of each test case contains two space-separated integers $N$ and $Q$.
The second line contains $N-1$ space-separated integers $B_{1}, B_{2}, \ldots, B_{N-1}$.
Each of the following $Q$ lines contains two space-separated integers $p$ and $q$ describing a query.

------  Output ------
For each query, if it is impossible to determine the required sum, print a single line containing the string "UNKNOWN". Otherwise, print a single line containing one integer — the required sum.

------  Constraints ------
$1 ≤ T ≤ 100$
$2 ≤ N ≤ 10^{5}$
$1 ≤ Q ≤ 10^{5}$
$1 ≤ p, q ≤ N$
$1 ≤ B_{i} ≤ 10^{9}$ for each valid $i$
the sum of $N$ over all test cases does not exceed $5 \cdot 10^{5}$
the sum of $Q$ over all test cases does not exceed $5 \cdot 10^{5}$

------  Subtasks ------
Subtask #1 (50 points):
$2 ≤ N ≤ 1,000$
$1 ≤ Q ≤ 1,000$
the sum of $N$ over all test cases does not exceed $5,000$
the sum of $Q$ over all test cases does not exceed $5,000$

Subtask #2 (50 points): original constraints

----- Sample Input 1 ------ 
1
5 3
4 5 6 7
1 2
1 3
4 1
----- Sample Output 1 ------ 
4
UNKNOWN
5
