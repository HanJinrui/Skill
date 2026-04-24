Given an integer $n$, find each $\boldsymbol{x}$ such that:

$0\leq x\leq n$
$n+x=n\oplus x$

where $\oplus$ denotes the bitwise XOR operator. Return the number of $\boldsymbol{x}$'s satisfying the criteria.

Example 

$n=4$   

There are four values that meet the criteria:  

$4+0=4\oplus0=4$
$4+1=4\oplus1=5$
$4+2=4\oplus2=6$
$4+3=4\oplus3=7$    

Return $4$.  

Function Description

Complete the sumXor function in the editor below.  

sumXor has the following parameter(s): 

- int n: an integer   

Returns 

- int: the number of values found   

Input Format

A single integer, $n$.

Constraints

$0\leq n\leq10^{15}$

Subtasks

$0\leq n\leq100$ for $\textbf{60\%}$ of the maximum score.

Output Format

Sample Input 0

5

Sample Output 0

2

Explanation 0

For $n=5$, the $\boldsymbol{x}$ values $\mbox{0}$ and $2$ satisfy the conditions:

$5+0=5,\:\:5\oplus0=5$
$5+2=7,\:\:5\oplus2=7$

Sample Input 1

10

Sample Output 1

4

Explanation 1

For $n=10$, the $\boldsymbol{x}$ values $\mbox{0}$, $\mbox{1}$, $4$, and $5$ satisfy the conditions:

$10+0=10,~~10\oplus0=10$
$10+1=11,~~10\oplus1=11$
$10+4=14,~~10\oplus4=14$
$10+5=15,~~10\oplus5=15$
