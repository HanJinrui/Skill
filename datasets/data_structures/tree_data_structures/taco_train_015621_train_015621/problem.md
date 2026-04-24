Read problem statements in [Hindi], [Bengali], [Mandarin Chinese], [Russian], and [Vietnamese] as well.

You are given a tree with $N$ nodes (numbered $1$ through $N$). For each valid $i$, node $i$ has a value $A_{i}$.

You should answer $Q$ queries. In each query:
You are given two nodes $a$ and $b$.
Let $S$ denote the set of all nodes on the simple path between the nodes $a$ and $b$ (including these nodes).
Find the minimum value of $|A_{x}-A_{y}|$ over all pairs $x, y \in S$ such that $x \neq y$.

------  Input ------
The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
The first line of each test case contains two space-separated integers $N$ and $Q$.
The second line contains $N$ space-separated integers $A_{1}, A_{2}, \ldots, A_{N}$.
Each of the next $N-1$ lines contains two space-separated integers $u$ and $v$ denoting that nodes $u$ and $v$ are connected by an edge.
Each of the last $Q$ lines contains two space-separated integers $a$ and $b$ describing a query.

------  Output ------
For each query, print a single line containing one integer ― the answer to the query.

------  Constraints ------
$1 ≤ T ≤ 20$
$2 ≤ N ≤ 2 \cdot 10^{5}$
$1 ≤ Q ≤ 2 \cdot 10^{5}$
$1 ≤ A_{i} ≤ 100$ for each valid $i$
$1 ≤ u, v, a, b ≤ N$
$a \neq b$
the sum of $N$ over all test cases does not exceed $5 \cdot 10^{5}$
the sum of $Q$ over all test cases does not exceed $5 \cdot 10^{5}$

------  Subtasks ------
Subtask #1 (30 points): $N, Q ≤ 1,000$

Subtask #2 (70 points): original constraints

----- Sample Input 1 ------ 
1

6 3

10 2 5 6 5 6

1 2

2 3

2 4

1 5

5 6

5 6

3 5

1 4
----- Sample Output 1 ------ 
1

0

4
----- explanation 1 ------ 
Example case 1:
- For the first query, $S=\{5, 6\}$, so the answer is $|A_{5}-A_{6}|=1$.
- For the second query, $S=\{3, 2, 1, 5\}$ and we can see that $|A_{3}-A_{5}|=0$.
- For the third query, $S=\{1, 2, 4\}$.
