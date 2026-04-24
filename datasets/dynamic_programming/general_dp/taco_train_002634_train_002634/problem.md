HackerRank-city is an acyclic connected graph (or tree). Its not an ordinary place, the construction of the whole tree takes place in $N$ steps. The process is described below:

It initially has $\mbox{1}$ node.
At each step, you must create $3$ duplicates of the current tree, and create $2$ new nodes to connect all $\begin{array}{c}4\end{array}$ copies in the following H shape:

At each $i^{\mbox{th}}$ step, the tree becomes $\begin{array}{c}4\end{array}$ times bigger plus $2$ new nodes, as well as $5$ new edges connecting everything together. The length of the new edges being added at step $\boldsymbol{i}$ is denoted by input $A_i$.

Calculate the sum of distances between each pair of nodes; as these answers may run large, print your answer modulo $\textbf{1000000007}$.

Input Format

The first line contains an integer, $N$ (the number of steps). The second line contains $N$ space-separated integers describing  $\boldsymbol{A_0}$, $A_1,\ldots,A_{N-2},A_{N-1}$.

Constraints

$1\leq N\leq10^6$

$1\leq A_i\leq9$

Subtask 

For $50\%$ score $1\leq N\leq10$

Output Format

Print the sum of distances between each pair of nodes modulo $\textbf{1000000007}$.

Sample Input 0

1
1

Sample Output 0

29

Sample Input 1

2
2 1

Sample Output 1

2641

Explanation

Sample 0

In this example, our tree looks like this:

Let $d(u,v)$ denote the distance between nodes $\mbox{u}$ and $\boldsymbol{\nu}$.

$d(1,2)+d(1,3)+d(1,4)+d(1,5)+d(1,6)$
$+d(2,3)+d(2,4)+d(2,5)+d(2,6)+d(3,4)$
$+d(3,5)+d(3,6)+d(4,5)+d(4,6)+d(5,6)=$
$3+1+2+2+3+2+1+3+2+1+1+2+2+1+3=29$.     

We print the result of $29\{%10000007$ as our answer.

Sample 1

In this example, our tree looks like this:

We calculate and sum the distances between nodes in the same manner as Sample 0 above, and print the result of our $answer\% 10000007}$, which is $2641$.
