You are given an array, $\mbox{A}$, consisting of $N$ integers.

A segment, $[l,r]$, is beautiful if and only if the bitwise AND of all numbers in $\mbox{A}$ with indices in the inclusive range of $[l,r]$ is not greater than $\mbox{X}$. In other words, segment $[l,r]$ is beautiful if $(A_l\land A_{l+1}\land\ldots\land A_r)\leq X$.

You must answer $\mbox{Q}$ queries. Each query, $Q_j$, consists of $3$ integers: $I_j$, $R_j$, and $X_j$. The answer for each $Q_j$ is the number of beautiful segments $[l,r]$ such that $L_j\leq l\leq r\leq R_j$ and $X=X_j$.

Input Format

The first line contains two space-separated integers, $N$ (the number of integers in $\mbox{A}$) and $\mbox{Q}$ (the number of queries).

The second line contains $N$ space-separated integers, where the $i^{\mbox{th}}$ integer denotes the $i^{\mbox{th}}$ element of array $\mbox{A}$.

Each line $j$ of the $\mbox{Q}$ subsequent lines contains $3$ space-separated integers, $I_j$, $R_j$, and $X_j$, respectively, describing query $Q_j$.

Constraints

$1\leq N\leq4\times10^4$
$1\leq Q\leq10^5$
$1\leq L_j\leq R_j\leq N$
$0\leq X_j\leq2^{17}$
$0\leq A_i<2^{17}$
$1\leq N,Q\leq2000$ holds for test cases worth at least $\textbf{10\%}$ of the problem's score.
$0\leq A_i<2^{11}$ holds for test cases worth at least $\textbf{40\%}$ of the problem's score. 

Output Format

Print $\mbox{Q}$ lines, where the $j^{th}$ line contains the number of beautiful segments for query $Q_j$.

Sample Input
5 3
1 2 7 3 4
1 5 3
2 4 6
3 5 2

Sample Output
13
5
2

Explanation

The beautiful segments for all queries are listed below.

Query 0: The beautiful segments are $[1,\textbf{1}],[\textbf{1},\textbf{2}],[\textbf{1},\textbf{3}],[\textbf{1},\textbf{4}],[\textbf{1},\textbf{5}],[\textbf{2},\textbf{2}],[\textbf{2},\textbf{3}],[\textbf{2},\textbf{4}],[\textbf{2},\textbf{5}],[\textbf{3},\textbf{4}],[\textbf{3},\textbf{5}],[\textbf{4},\textbf{4}],[\textbf{4},\textbf{5}],$.

Query 1: The beautiful segments are $[2,2],[2,3],[2,4],[3,4],[4,4]$.

Query 2: The beautiful segments are $[3,5],[4,5]$.
