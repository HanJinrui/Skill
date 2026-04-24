Consider an array $A=[a_0,a_1,...,a_{n-1}]$ of $n$ integers. We perform $\textit{q}$ queries of the following type on $\mbox{A}$:

Sort all the elements in the subsegment $a_{l_i},a_{l_i+1},\ldots,a_{r_i}$.

Given $\mbox{A}$, can you find and print the value at index $\boldsymbol{\mbox{k}}$ (where $0\leq k<n$) after performing $\textit{q}$ queries?

Input Format

The first line contains three positive space-separated integers describing the respective values of $n$ (the number of integers in $\mbox{A}$), $\textit{q}$ (the number of queries), and $\boldsymbol{\mbox{k}}$ (an index in $\mbox{A}$). 

The next line contains $n$ space-separated integers describing the respective values of $a_0,a_1,\ldots,a_{n-1}$. 

Each line $j$ of the $\textit{q}$ subsequent lines contain two space-separated integers describing the respective $l_{j}$ and $r_j$ values for query $j$.

Constraints

$1\leq n,q\leq75000$
$0\leq k\leq n-1$
$-10^9\leq a_i\leq10^9$
$0\leq l_i\leq r_i<n$

Output Format

Print a single integer denoting the value of $a_{k}$ after processing all $\textit{q}$ queries.

Sample Input 0

3 1 1
3 2 1
0 1

Sample Output 0

3

Explanation 0

$A=[3,2,1]$ 

There is only one query to perform. When we sort the subarray ranging from index $\mbox{0}$ to index $\mbox{1}$, we get $A'=[2,3,1]$. We then print the element at index $\mbox{1}$, which is $3$. 

Sample Input 1

4 2 0
4 3 2 1
0 2
1 3

Sample Output 1

2 

Explanation 1       

$A=[4,3,2,1]$ 

There are $q=2$ queries:

When we sort the subarray ranging from index $\mbox{0}$ to index $2$, we get $A'=[2,3,4,1]$. 
When we sort the subarray of $\mbox{A'}$ from index $\mbox{1}$ to index $3$, we get $A''=[2,1,3,4]$.

Having performed all of the queries, we print the element at index $\mbox{0}$, which is $2$.
