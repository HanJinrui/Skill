Given a set of $n$ intervals, find the size of its largest possible subset of intervals such that no three intervals in the subset share a common point.

Input Format

The first line contains an integer, $\boldsymbol{\mathrm{~S~}}$, denoting the number of interval sets you must find answers for. The $s\cdot(n+1)$ subsequent lines describe each of the $\boldsymbol{\mathrm{~S~}}$ interval sets as follows:

The first line contains an integer, $n$, denoting the number of intervals in the list. 
Each line $\boldsymbol{i}$ of the $n$ subsequent lines contains two space-separated integers describing the respective starting ($a_i$) and ending ($b_i$) boundaries of an interval.

Constraints

$1\leq s\leq100$
$2\leq n\leq1000$  
$1\leq a_i\leq b_i\leq10^9$

Output Format

For each of the $\boldsymbol{\mathrm{~S~}}$ interval sets, print an integer denoting the size of the largest possible subset of intervals in the given set such that no three points in the subset overlap.

Sample Input
4
3
1 2
2 3
2 4
3
1 5
1 5
1 5
4
1 10
1 3
4 6
7 10
4
1 10
1 3
3 6
7 10

Sample Output
2
2
4
3

Explanation

For set $\boldsymbol{s_{0}}$, all three intervals fall on point $2$ so we can only choose any $2$ of the intervals. Thus, we print $2$ on a new line.

For set $\boldsymbol{S_{1}}$, all three intervals span the range from $\mbox{1}$ to $5$ so we can only choose any $2$ of them. Thus, we print $2$ on a new line.

For set $s_2$, we can choose all $\begin{array}{c}4\end{array}$ intervals without having more than two of them overlap at any given point. Thus, we print $\begin{array}{c}4\end{array}$ on a new line.

For set $s_3$, the intervals $[1,10]$, $[1,3]$, and $[3,6]$ all overlap at point $3$, so we must only choose $2$ of these intervals to combine with the last interval, $[7,10]$, for a total of $3$ qualifying intervals. Thus, we print $3$ on a new line.
