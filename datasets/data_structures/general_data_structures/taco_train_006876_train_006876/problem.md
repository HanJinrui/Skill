You are given an unrooted tree of $n$ nodes numbered from $\mbox{1}$ to $n$. Each node $\boldsymbol{i}$ has a color, $c_i$. 

Let $d(i,j)$ be the number of different colors in the path between node $\boldsymbol{i}$ and node $j$. For each node $\boldsymbol{i}$, calculate the value of $\textit{sum}_i$, defined as follows:

$sum_{i}=\sum_{j=1}^{n}d(i,j)$

Your task is to print the value of $\textit{sum}_i$ for each node $1\leq i\leq n$.

Input Format

The first line contains a single integer, $n$, denoting the number of nodes. 

The second line contains $n$ space-separated integers, $c_1,c_2,\ldots,c_n$, where each $c_i$ describes the color of node $\boldsymbol{i}$. 

Each of the $n-1$ subsequent lines contains $2$ space-separated integers, $\boldsymbol{a}$ and $\boldsymbol{b}$, defining an undirected edge between nodes $\boldsymbol{a}$ and $\boldsymbol{b}$.

Constraints

$1\leq n\leq10^5$
$1\leq c_i\leq10^5$

Output Format

Print $n$ lines, where the $i^{\mbox{th}}$ line contains a single integer denoting $\textit{sum}_i$.

Sample Input
5
1 2 3 2 3
1 2
2 3
2 4
1 5

Sample Output
10
9
11
9
12

Explanation

The Sample Input defines the following tree:

Each $\textit{sum}_i$ is calculated as follows:

$sum_1=d(1,1)+d(1,2)+d(1,3)+d(1,4)+d(1,5)=1+2+3+2+2=10$
$sum_2=d(2,1)+d(2,2)+d(2,3)+d(2,4)+d(2,5)=2+1+2+1+3=9$
$sum_3=d(3,1)+d(3,2)+d(3,3)+d(3,4)+d(3,5)=3+2+1+2+3=11$
$sum_4=d(4,1)+d(4,2)+d(4,3)+d(4,4)+d(4,5)=2+1+2+1+3=9$
$sum_5=d(5,1)+d(5,2)+d(5,3)+d(5,4)+d(5,5)=2+3+3+3+1=12$
