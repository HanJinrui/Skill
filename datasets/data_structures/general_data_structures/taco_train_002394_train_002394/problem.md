You are given $\mbox{Q}$ queries. Each query consists of a single number $N$. You can perform any of the $2$ operations on $N$ in each move:

1: If we take 2 integers $\class{ML__boldsymbol}{\boldsymbol{a}}$ and $\boldsymbol{b}$ where $N=a\times b$ $(a\neq1$, $b\neq1)$, then we can change $N=max(a,b)$

2: Decrease the value of $N$ by $1$. 

Determine the minimum number of moves required to reduce the value of $N$ to $0$.

Input Format

The first line contains the integer $Q$. 

The next $Q$ lines each contain an integer, $N$.  

Constraints

$1\leq Q\leq10^3$ 

$0\leq N\leq10^6$  

Output Format

Output $Q$ lines. Each line containing the minimum number of moves required to reduce the value of $N$ to $0$.

Sample Input
2
3
4

Sample Output
3
3

Explanation

For test case 1, We only have one option that gives the minimum number of moves. 

Follow $3$ -> $2$ -> $\mbox{1}$ -> $0$. Hence, $3$ moves.

For the case 2, we can either go $\begin{array}{c}4\end{array}$ -> $3$ -> $2$ -> $1$ -> $0$ or $\begin{array}{c}4\end{array}$ -> $2$ -> $1$ -> $0$. The 2nd option is more optimal. Hence, $3$ moves.
