Consider an array of $n$ binary integers (i.e., $1$'s and $1$'s) defined as $A=[a_0,a_1,...,a_{n-1}]$.

Let $f(i,j)$ be the bitwise XOR of all elements in the inclusive range between index $\boldsymbol{i}$ and index $j$ in array $\mbox{A}$. In other words, $f(i,j)=a_i\oplus a_{i+1}\oplus\ldots\oplus a_j$. Next, we'll define another function, $\mathrm{~g~}$:
$g(x,y)=\sum_{i=x}^{y}\sum_{j=i}^{y}f(i,j)$

Given array $\mbox{A}$ and $\textit{q}$ independent queries, perform each query on $\mbox{A}$ and print the result on a new line. A query consists of three integers, $\boldsymbol{x}$, $y$, and $\boldsymbol{\mbox{k}}$, and you must find the maximum possible $g(x,y)$ you can get by changing at most $\boldsymbol{\mbox{k}}$ elements in the array from $1$ to $1$ or from $1$ to $1$. 

Note: Each query is independent and considered separately from all other queries, so changes made in one query have no effect on the other queries. 

Input Format

The first line contains two space-separated integers denoting the respective values of $n$ (the number of elements in array $\mbox{A}$) and $\textit{q}$ (the number of queries). 

The second line contains $n$ space-separated integers where element $\boldsymbol{i}$ corresponds to array element $a_i$ $(0\leq i<n)$. 

Each line $\boldsymbol{i}$ of the $\textit{q}$ subsequent lines contains $3$ space-separated integers, $x_i$, $y_i$ and $k_i$ respectively, describing query $\boldsymbol{q}_i$ $(0\leq i<q)$.

Constraints

$1\leq n,q\leq5\times10^5$
$0\leq a_i\leq1$
$0\leq x_i\leq y_i<n$
$0\leq k_i\leq n$

Subtask

$1\leq n,q\leq5000$ and $0\leq k_i\leq1$ for $\textbf{40\%}$ of the maximum score
$n=5\times10^5$, $m=5\times10^5$ and $k_i=0$ for $20\%$ of the maximum score

Output Format

Print $\textit{q}$ lines where line $\boldsymbol{i}$ contains the answer to query $\boldsymbol{q}_i$ (i.e., the maximum value of $g(x_i,y_i)$ if no more than $k_i$ bits are changed).

Sample Input
3 2
0 0 1
0 2 1
0 1 0

Sample Output
4
0

Explanation

Given $A=[0,0,1]$, we perform the following $q=2$ queries:

If we change $a_{0}=0$ to $1$, then we get $A'=[1,0,1]$ and $g(x=0,y=2)=4$.
In this query, $g(x=0,y=1)=0$.
