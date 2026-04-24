Consider four numbers: $\mbox{A}$, $\mbox{B}$, $\mbox{C}$, and $\mbox{K}$. You must change at most $\mbox{K}$ bits in $\mbox{A}$ and $\mbox{B}$ to form the numbers $\mbox{A'}$ and $B^{\prime}$ satisfying the equation $A'\mid B'=C$. Here, the | symbol denotes the bitwise OR operation.

Given $Q$ sets of the numbers defined above, find and print the respective values of $\mbox{A'}$ and $B^{\prime}$ on new lines; if no such value exists, print $-1$ instead. If there are multiple solutions, make $\mbox{A'}$ as small as possible; if there are still multiple solutions, make $B^{\prime}$ as small as possible. 

Notes: 

$\mbox{A}$, $\mbox{B}$, and $\mbox{C}$ are given in Hexadecimal (base 16), and $\mbox{K}$ is given in decimal (base 10).
If the number of bits changed in $\mbox{A}$ is $k_a$ and the number of bits changed in B is $k_b$, then $k_a+k_b$ must be $\leq K$.

Input Format

The first line contains an integer, $Q$, denoting the number of queries. The subsequent lines describe each respective query as follows:

The first line contains a single integer denoting the value of $\mbox{K}$.
Each of the next $3$ lines contains a Hexadecimal (base 16) number describing the respective values of $\mbox{A}$, $\mbox{B}$, and $\mbox{C}$.

Constraints

$1\leq Q\leq5$
$0\leq K\leq5\times10^5$
$0<A,B,C<16^{5\times10^4}$

Output Format

Print two lines of output for each query:

The first line should contain a Hexadecimal (base 16) number denoting the value of $\mbox{A'}$.
The second line must contain a Hexadecimal (base 16) number denoting the value of $B^{\prime}$. 

If no valid answer exists, you must instead print one line of output with the integer $-1$.

Note: The letters in Hexadecimal numbers must be in uppercase.

Sample Input
3
8
2B
9F
58
5
B9
40
5A
2
91
BE
A8

Sample Output
8
58
18
42
-1

Explanation

Query 0: 

In this query, $K=8$. 

Change $A=(2B)_{16}$ to $A'=(8)_{16}$. $3$ bits are changed.

Change B = $(9F)_{16}$ to $B'=(58)_{16}$. $5$ bits are changed.

$A'\mid B'=(8)_{16}\mid(58)_{16}=(58)_{16}=C$

Query 1: 

In this query, $K=5$. 

Change $A=(B9)_{16}$ to $A'=(18)_{16}$. $3$ bits are changed. 

Change $B=(40)_{16}$ to $B'=(42)_{16}$. Only $1$ bit is changed.

$A'\mid B'=(18)_{16}\mid(42)_{16}=(5A)_{16}=C$

Query 2: 

There is no valid answer, so we print $-1$.
