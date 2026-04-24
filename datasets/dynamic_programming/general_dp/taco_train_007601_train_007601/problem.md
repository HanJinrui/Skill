There are $n$ bulbs in a straight line, numbered from $\mbox{0}$ to $n-1$. 
Each bulb $\boldsymbol{i}$ has a button associated with it, and there is a cost, $c_i$, for pressing this button. When some button $\boldsymbol{i}$ is pressed, all the bulbs at a distance $\leq k$ from bulb $\boldsymbol{i}$ will be toggled(off->on, on->off). 

Given $n$, $\boldsymbol{\mbox{k}}$, and the costs for each button, find and print the minimum cost of turning off all $n$ bulbs if they're all on initially.

Input Format

The first line contains two space-separated integers describing the respective values of $n$ and $\boldsymbol{\mbox{k}}$. 

The second line contains $n$ space-separated integers describing the respective costs of each bulb (i.e., $c_0,c_1,\ldots,c_{n-1}$).

Constraints

$3\leq n\leq10^4$
$0\leq k\leq1000$
$0\leq c_i\leq10^9$

Output Format

Print a long integer denoting the minimum cost of turning off all $n$ bulbs.

Sample Input
3 1
1 1 1

Sample Output
1

Explanation

If we press the middle switch, the middle bulb and the $k=1$ closest adjacent bulbs (i.e., the first and third) will turn off. Because all bulbs will be off in one button press, this cost is minimal. Thus, we print $1$ as our answer.
