A new gangster is trying to take control of the city. He makes a list of his $N$ adversaries (e.g. gangster $\mbox{1}$, gangster $2$, ... gangster $N-1$, gangster $N$) and plans to get rid of them.

$\mbox{K}$ mercenaries are willing to do the job. The gangster can use any number of these mercenaries. But he has to honor one condition set by them: they have to be assigned in such a way that they eliminate a consecutive group of gangsters in the list, e.g. gangster $\boldsymbol{i}$, gangster $i+1$, ..., gangster $j-1$, gangster $j$, where the following is true: $1\leq i\leq j\leq N$.

While our new gangster wants to kill all of them, he also wants to pay the least amount of money. All mercenaries charge a different amount to kill different people. So he asks you to help him minimize his expenses.  

Input Format

The first line contains two space-separated integers, $N$  and $\mbox{K}$. Then $\mbox{K}$ lines follow, each containing $N$ integers as follows:

The $j^{th}$ number on the $i^{th}$ line is the amount charged by the $i^{th}$mercenary for killing the $j^{th}$ gangster on the list.

Constraints

$1\leq N\leq20$
$1\leq K\leq10$
$0\leq amount$ $charged\leq10000$

Output Format

Just one line, the minimum cost for killing the $N$ gangsters on the list.

Sample Input
3 2
1 4 1
2 2 2

Sample Output
 5

Explanation

The new gangster can assign mercenary 1 to kill gangster 1, and mercenary 2 to kill gangster 2 and gangster 3.
