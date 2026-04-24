Our lazy white falcon finally decided to learn heavy-light decomposition. Her teacher gave an assignment for her to practice this new technique. Please help her by solving this problem. 

You are given a tree with $N$ nodes and each node's value is initially $0$. The problem asks you to operate the following two types of queries:

"1 u x" assign $\boldsymbol{x}$ to the value of the node $\mbox{u}$.
"2 u v" print the maximum value of the nodes on the unique path between $\mbox{u}$ and $\boldsymbol{\nu}$.

Input Format

First line consists of two integers seperated by a space: $N$ and $Q$.

Following $N-1$ lines consisting of two integers denotes the undirectional edges of the tree. 

Following $Q$ lines consist of the queries you are asked to operate. 

Constraints

$1\leq N,Q,x\leq50000$

It is guaranteed that input denotes a connected tree with $N$ nodes. Nodes are enumerated with 0-based indexing.

Output Format

For each second type of query print single integer in a single line, denoting the asked maximum value.

Sample Input
3 3
0 1
1 2
1 0 1
1 1 2
2 0 2

Sample Output
2

Explanation

After the first two updates value of the $0$th node is $1$ and $1$st node is $2$. That is why maxiumum value on the path between $0$ and $2$ is $max(1,2)=2$.
