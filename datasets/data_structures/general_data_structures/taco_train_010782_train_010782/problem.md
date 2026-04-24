White Falcon has a tree with $N$ nodes. Each node contains a linear function. Let's denote by $f_u(x)$ the linear function contained in the node $\mbox{u}$.  

Let's denote the path from node $\mbox{u}$ to node $\boldsymbol{\nu}$ like this: $p_1,p_2,p_3,\ldots,p_k$, where $p_1=u$ and $p_k=v$, and $p_i$ and ${p}_{i+1}$ are connected.  

White Falcon also has $\mbox{Q}$ queries. They are in the following format:  

$\mbox{1}$ $\mbox{u}$ $\boldsymbol{\nu}$ $\boldsymbol{a}$ $\boldsymbol{b}$. Assign $ax+b$ as the function of all the nodes on the path from $\mbox{u}$ to $\boldsymbol{\nu}$, i.e., $f_{p_i}(x)$ is changed to $ax+b$ where $p_1,p_2,p_3,\ldots,p_k$ is the path from $\mbox{u}$ to $\boldsymbol{\nu}$.

$2$ $\mbox{u}$ $\boldsymbol{\nu}$ $\boldsymbol{x}$. Calculate $f_{p_k}(f_{p_{k-1}}(f_{p_{k-2}}(...f_{p_1}(x)))$ modulo $(10^9+7)$

Input Format

The first line contains $N$, the number of nodes. The following $N$ lines each contain two integers $\boldsymbol{a}$ and $\boldsymbol{b}$ that describe the function $ax+b$.  

Following $N-1$ lines contain edges of the tree. 

The next line contains $\mbox{Q}$, the number of queries. Each subsequent line contains one of the queries described above.

Output Format

For every query of the second kind, print one line containing an integer, the answer for that query.  

Constraints 

$1\leq N\leq50000$ (Number of nodes) 

$1\leq Q\leq50000$ (Number of queries) 

$0\leq a,b,x<10^9+7$

Sample Input
2
1 1
1 2
1 2
2
1 2 2 1 1
2 1 2 1

Sample Output
3

Explanation

$f_1(1)=2$ 

$f_2(2)=3$
