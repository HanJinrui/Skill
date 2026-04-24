Taylor loves trees, and this new challenge has him stumped!

Consider a tree, $\boldsymbol{\boldsymbol{t}}$, consisting of $n$ nodes. Each node is numbered from $1$ to $n$, and each node $\boldsymbol{i}$ has an integer, $c_i$, attached to it. 

A query on tree $\boldsymbol{\boldsymbol{t}}$ takes the form w x y z. To process a query, you must print the count of ordered pairs of integers $(i,j)$ such that the following four conditions are all satisfied: 

$i\neq j$
$\mbox{i}\in$ the path from node $\boldsymbol{w}$ to node $\boldsymbol{x}$.
$j\in$ path from node $y$ to node $z$.
$c_i=c_j$  

Given $\boldsymbol{\boldsymbol{t}}$ and $\textit{q}$ queries, process each query in order, printing the pair count for each query on a new line.

Input Format

The first line contains two space-separated integers describing the respective values of $n$ (the number of nodes) and $\textit{q}$ (the number of queries). 

The second line contains $n$ space-separated integers describing the respective values of each node (i.e., $c_1,c_2,\ldots,c_n$). 

Each of the $n-1$ subsequent lines contains two space-separated integers, $\mbox{u}$ and $\boldsymbol{\nu}$, defining a bidirectional edge between nodes $\mbox{u}$ and $\boldsymbol{\nu}$. 

Each of the $\textit{q}$ subsequent lines contains a w x y z query, defined above.

Constraints

$1\leq n\leq10^5$  
$1\leq q\leq50000$  
$1\leq c_i\leq10^9$  
$1\le u,v,w,x,y,z\le n$  

Scoring for this problem is Binary, that means you have to pass all the test cases to get a positive score.

Output Format

For each query, print the count of ordered pairs of integers satisfying the four given conditions on a new line.

Sample Input
10 5
10 2 3 5 10 5 3 6 2 1
1 2
1 3
3 4
3 5
3 6
4 7
5 8
7 9
2 10
8 5 2 10
3 8 4 9
1 9 5 9
4 6 4 6
5 8 5 8

Sample Output
0
1
3
2
0

Explanation

We perform $q=5$ queries on the following tree:

Find the number of valid ordered pairs where $\boldsymbol{i}$ is in the path from node $8$ to node $5$ and $j$ is in the path from node $2$ to node $10$. No such pair exists, so we print $0$.
Find the number of valid ordered pairs where $\boldsymbol{i}$ is in the path from node $3$ to node $8$ and $j$ is in the path from node $\begin{array}{c}4\end{array}$ to node $\mbox{9}$. One such pair, $(3,7)$, exists, so we print $1$.
Find the number of valid ordered pairs where $\boldsymbol{i}$ is in the path from node $1$ to node $\mbox{9}$ and $j$ is in the path from node $5$ to node $\mbox{9}$. Three such pairs, $(1,5)$, $(3,7)$, and $(7,3)$ exist, so we print $3$.
Find the number of valid ordered pairs where $\boldsymbol{i}$ is in the path from node $\begin{array}{c}4\end{array}$ to node $\boldsymbol{6}$ and $j$ is in the path from node $\begin{array}{c}4\end{array}$ to node $\boldsymbol{6}$. Two such pairs, $(4,6)$ and $(6,4)$, exist, so we print $2$.  
Find the number of valid ordered pairs where $\boldsymbol{i}$ is in the path from node $5$ to node $8$ and $j$ is in the path from node $5$ to node $8$. No such pair exists, so we print $0$.
