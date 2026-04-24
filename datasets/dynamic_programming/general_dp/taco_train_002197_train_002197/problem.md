King Arthur has a large kingdom that can be represented as a tree, where nodes correspond to cities and edges correspond to the roads between cities. The kingdom has a total of $n$ cities numbered from $\mbox{1}$ to $n$. 

The King wants to divide his kingdom between his two children, Reggie and Betty, by giving each of them $\mbox{0}$ or more cities; however, they don't get along so he must divide the kingdom in such a way that they will not invade each other's cities. The first sibling will invade the second sibling's city if the second sibling has no other cities directly connected to it. For example, consider the kingdom configurations below:

Given a map of the kingdom's $n$ cities, find and print the number of ways King Arthur can divide it between his two children such that they will not invade each other. As this answer can be quite large, it must be modulo $10^9+7$.

Input Format

The first line contains a single integer denoting $n$ (the number of cities in the kingdom). 

Each of the $n-1$ subsequent lines contains two space-separated integers, $\mbox{u}$ and $\boldsymbol{\nu}$, describing a road connecting cities $\mbox{u}$ and $\boldsymbol{\nu}$. 

Constraints

$2\leq n\leq10^5$
$1\leq u,v\leq n$
It is guaranteed that all cities are connected.

Subtasks

$2\leq n\leq20$ for 40% of the maximum score.

Output Format

Print the number of ways to divide the kingdom such that the siblings will not invade each other, modulo $10^9+7$.

Sample Input
5
1 2
1 3
3 4
3 5

Sample Output
4

Explanation

In the diagrams below, red cities are ruled by Betty and blue cities are ruled by Reggie. The diagram below shows a division of the kingdom that results in war between the siblings:

Because cities $5$ and $\begin{array}{c}4\end{array}$ are not connected to any other red cities, blue city $3$ will cut off their supplies and declare war on them. That said, there are four valid ways to divide the kingdom peacefully:

We then print the value of $4\ \text{mod}\ (10^9+7)=4$ as our answer.
