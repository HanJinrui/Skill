We call an quadruple of positive integers, $(W,X,Y,Z)$, beautiful if the following condition is true:

$W\oplus X\oplus Y\oplus Z\neq0$

Note: $\theta$ is the bitwise XOR operator.

Given $\mbox{A}$, $\mbox{B}$, $\mbox{C}$, and $\mbox{D}$, count the number of beautiful quadruples of the form $(W,X,Y,Z)$ where the following constraints hold:

$1\leq W\leq A$
$1\leq X\leq B$
$1\leq Y\leq C$
$1\leq z\leq D$

When you count the number of beautiful quadruples, you should consider two quadruples as same if the following are true:

They contain same integers.
Number of times each integers occur in the quadruple is same.

For example $(1,1,1,2)$ and $(1,1,2,1)$ should be considered as same.

Input Format

A single line with four space-separated integers describing the respective values of $\mbox{A}$, $\mbox{B}$, $\mbox{C}$, and $\mbox{D}$.

Constraints

$1\leq A,B,C,D\leq3000$
For $50\%$ of the maximum score, $1\leq A,B,C,D\leq50$

Output Format

Print the number of beautiful quadruples.

Sample Input
1 2 3 4

Sample Output
11

Explanation

There are $\mbox{11}$ beautiful quadruples for this input:

$(1,1,1,2)$
$(1,1,1,3)$
$(1,1,1,4)$
$(1,1,2,3)$
$(1,1,2,4)$
$(1,1,3,4)$
$(1,2,2,2)$
$(1,2,2,3)$
$(1,2,2,4)$
$(1,2,3,3)$
$(1,2,3,4)$

Thus, we print $\mbox{11}$ as our output.

Note that $(1,1,1,2)$ is same as $(1,1,2,1)$.
