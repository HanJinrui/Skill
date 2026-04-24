Given an $n\times n\times n$ cube, let $f(x,y,z)$ (where $1\leq x,y,z\leq n$) denote the value stored in cell $(x,y,z)$. 

A $k\times k\times k$ sub-cube (where $1\leq k\leq n$) of an $n\times n\times n$ cube is considered to be special if the maximum value stored in any cell in the sub-cube is equal to $\boldsymbol{\mbox{k}}$.

For each $\boldsymbol{\mbox{k}}$ in the inclusive range $[1,n]$, calculate the number of special sub-cubes. Then print each $\textit{count}_k$ as a single line of space-separated integers (i.e., $\textit{count}_1\ \textit{count}_2\ \textbf{.... count}_n$).

Input Format

The first line contains an integer, $\textit{q}$, denoting the number of queries. The $2\cdot q$ subsequent lines describe each query over two lines:

The first line contains an integer, $n$, denoting the side length of the initial cube.
The second line contains $n^{3}$ space-separated integers describing an array of $n^{3}$ integers in the form $a_0,a_1,\ldots,a_{n^3-1}$. The integer in some cell $(x,y,z)$ is calculated using the formula $a[(x-1)\cdot n^2+(y-1)\cdot n+z]$.

Constraints

$1\leq q\leq5$
$1\leq n\leq50$
$1\leq f(x,y,z)\leq n$ where $1\leq x,y,z\leq n$

Output Format

For each query, print $n$ space-separated integers where the $i^{\mbox{th}}$ integer denotes the number of special sub-cubes for $k=i$.

Sample Input
2
2
2 1 1 1 1 1 1 1
2
1 1 1 1 2 1 1 2

Sample Output
7 1
6 1

Explanation

We must perform the following $q=2$ queries:

We have a cube of size $n=2$ and must calculate the number of special sub-cubes for the following values of $\boldsymbol{\mbox{k}}$:

$k=1$: There are $2^3=8$ sub-cubes of size $1$ and seven of them have a maximum value of $1$ written inside them. So, for $k=1$, the answer is $7$. 
$k=2$: There is only one sub-cube of size $2$ and the maximum number written inside it is $2$. So, for $k=2$, the answer is $1$.    

We then print the respective values for each $\boldsymbol{\mbox{k}}$ as a single line of space-separated integers (i.e., 7 1).

We have a cube of size $n=2$ and must calculate the number of special sub-cubes for the following values of $\boldsymbol{\mbox{k}}$:   

$k=1$: There are $2^3=8$ sub-cubes of size $1$ and six of them have a maximum value of $1$ written inside them. So, for $k=1$, the answer is $\boldsymbol{6}$. 
$k=2$: There is only one sub-cube of size $2$ and the maximum number written inside it is $2$. So, for $k=2$, the answer is $1$.        

We then print the respective values for each $\boldsymbol{\mbox{k}}$ as a single line of space-separated integers (i.e., 6 1).
