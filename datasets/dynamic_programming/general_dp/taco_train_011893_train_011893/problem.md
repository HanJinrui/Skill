A company needs random numbers for its operation. $N$ random numbers have been generated using $N$ numbers as seeds and the following recurrence formula:

$\begin{aligned}F(K)=&\left(C(1)\times F(K-1)+C(2)\times F(K-2)+\cdots+C(N-1)\times F(K-N+1)+C(N)\times F(K-N)\right)\text{\%}\left(10^9+7\right)\end{aligned}$

The numbers used as seeds are $F(N-1),F(N-2),...,F(1),F(0)$. $F(K)$ is the $K^{\mbox{th}}$ term of the recurrence.

Due to a failure on the servers, the company lost its seed numbers. Now they just have the recurrence formula and the previously generated $N$ random numbers.

The company wants to recover the numbers used as seeds, so they have hired you for doing this task.

Input Format

The first line contains two space-separated integers, $N$ and $\mbox{K}$, respectively. 

The second line contains the space-separated integers describing $F(K),F(K-1),...,F(K-N+2),F(K-N+1)$ (all these numbers are non-negative integers $<10^9$). 

The third line contains the space-separated coefficients of the recurrence formula, $C(1),C(2),...,C(N-1),C(N)$. All of these coefficients are positive integers $<10^9$.

Constraints

$1\leq N\leq50$
$1\leq K\leq10^9$
$0\leq K-N+1$

Output Format

The output must be one line containing the space-separated seeds of the random numbers - $F(N-1),F(N-2),...,F(1),F(0)$.

Sample Input
2 6
13 8
1 1

Sample Output
1 1 

Explanation

This is the classic Fibonacci recurrence. We have the $6^{th}$ and $5^{th}$ terms, and, of course, the seeds are the numbers $1$ and $1$.
