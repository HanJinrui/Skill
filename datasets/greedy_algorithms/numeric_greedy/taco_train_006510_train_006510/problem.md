Read problem statements in [Hindi], [Bengali], [Mandarin Chinese], [Russian], and [Vietnamese] as well.

You are given a sequence $A_{1}, A_{2}, \ldots, A_{N}$. Find the maximum value of the expression $|A_{x}-A_{y}| + |A_{y}-A_{z}| + |A_{z}-A_{x}|$ over all triples of pairwise distinct valid indices $(x, y, z)$.

------  Input ------
The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
The first line of each test case contains a single integer $N$.
The second line contains $N$ space-separated integers $A_{1}, A_{2}, \ldots, A_{N}$.

------  Output ------
For each test case, print a single line containing one integer ― the maximum value of $|A_{x}-A_{y}| + |A_{y}-A_{z}| + |A_{z}-A_{x}|$.

------  Constraints ------
$1 ≤ T ≤ 5$
$3 ≤ N ≤ 10^{5}$
$|A_{i}| ≤ 10^{9}$ for each valid $i$

------  Subtasks ------
Subtask #1 (30 points): $N ≤ 500$

Subtask #2 (70 points): original constraints

----- Sample Input 1 ------ 
3

3

2 7 5

3

3 3 3

5

2 2 2 2 5
----- Sample Output 1 ------ 
10

0

6
----- explanation 1 ------ 
Example case 1: The value of the expression is always $10$. For example, let $x = 1$, $y = 2$ and $z = 3$, then it is $|2 - 7| + |7 - 5| + |5 - 2| = 5 + 2 + 3 = 10$.

Example case 2: Since all values in the sequence are the same, the value of the expression is always $0$.

Example case 3: One optimal solution is $x = 1$, $y=2$ and $z = 5$, which gives $|2 - 2| + |2 - 5| + |5 - 2| = 0 + 3 + 3 = 6$.
