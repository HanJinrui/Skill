Read problem statements in [Hindi], [Bengali], [Mandarin Chinese], [Russian], and [Vietnamese] as well.

Chef has always been fond of girls, but he could not make any girl his friend. In order to finally make one, he was asked to solve the following problem:

You are given a string $S$ with length $N$. Choose an integer $K$ and two non-empty subsequences $A$ and $B$ of characters of this string, each with length $K$, such that:
$A = B$, i.e. for each valid $i$, the $i$-th character in $A$ is the same as the $i$-th character in $B$.
Let's denote the indices of characters used to construct $A$ by $a_{1}, a_{2}, \ldots, a_{K}$, i.e. $A = (S_{a_{1}}, S_{a_{2}}, \ldots, S_{a_{K}})$. Similarly, let's denote the indices of characters used to construct $B$ by $b_{1}, b_{2}, \ldots, b_{K}$.
If we denote the number of common indices in the sequences $a$ and $b$ by $M$, then $M+1 ≤ K$.

Since Chef is busy right now, he asks you to find the maximum value of $K$ such that it is possible to find sequences $A$ and $B$ which satisfy the given conditions or determine that there is no such $K$.

------  Input ------
The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
The first line of each test case contains a single integer $N$.
The second line contains a single string $S$ with length $N$.

------  Output ------
For each test case, print a single line containing one integer ― the maximum $K$, or $0$ if there is no solution.

------  Constraints ------
$1 ≤ T ≤ 100$
$1 ≤ N ≤ 10^{5}$
$S$ contains only lowercase English letters

------  Subtasks ------
Subtask #1 (20 points): $N ≤ 8$

Subtask #2 (80 points): original constraints

----- Sample Input 1 ------ 
1

4

anxa
----- Sample Output 1 ------ 
1
