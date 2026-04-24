Divide-and-Conquer on a tree is a powerful approach to solving tree problems. 

Imagine a tree, $\boldsymbol{\boldsymbol{t}}$, with $n$ vertices. Let's remove some vertex $\boldsymbol{\nu}$ from tree $\boldsymbol{\boldsymbol{t}}$, splitting $\boldsymbol{\boldsymbol{t}}$ into zero or more connected components, $t_{1},t_{2},\ldots,t_{k}$, with vertices $n_{1},n_{2},\ldots,n_{k}$. We can prove that there is a vertex, $\boldsymbol{\nu}$, such that the size of each formed components is at most $\left\lfloor{\frac{n}{2}}\right\rfloor$.

The Divide-and-Conquer approach can be described as follows:

Initially, there is a tree, $\boldsymbol{\boldsymbol{t}}$, with $n$ vertices.
Find vertex $\boldsymbol{\nu}$ such that, if $\boldsymbol{\nu}$ is removed from the tree, the size of each formed component after removing $\boldsymbol{\nu}$ is at most $\left\lfloor{\frac{n}{2}}\right\rfloor$.
Remove $\boldsymbol{\nu}$ from tree $\boldsymbol{\boldsymbol{t}}$.
Perform this approach recursively for each of the connected components.

We can prove that if we find such a vertex $\boldsymbol{\nu}$ in linear time (e.g., using DFS), the entire approach works in $\mathcal{O}(n\cdot\log n)$. Of course, sometimes there are several such vertices $\boldsymbol{\nu}$ that we can choose on some step, we can take and remove any of them. However, right now we are interested in trees such that at each step there is a unique vertex $\boldsymbol{\nu}$ that we can choose.

Given $n$, count the number of tree $\boldsymbol{\boldsymbol{t}}$'s such that the Divide-and-Conquer approach works determinately on them. As this number can be quite large, your answer must be modulo $m$.

Input Format

A single line of two space-separated positive integers describing the respective values of $n$ (the number of vertices in tree $\boldsymbol{\boldsymbol{t}}$) and $m$ (the modulo value).

Constraints

$1\leq n\leq3000$
$n\lt m\leq10^9$
$m$ is a prime number.

Subtasks

$n\leq9$ for $\textbf{40\%}$ of the maximum score.
$n\leq500$ for $70\%$ of the maximum score. 

Output Format

Print a single integer denoting the number of tree $\boldsymbol{\boldsymbol{t}}$'s such that vertex $\boldsymbol{\nu}$ is unique at each step when applying the Divide-and-Conquer approach, modulo $m$.

Sample Input 0

1 103

Sample Output 0 

1

Explanation 0

For $n=1$, there is only one way to build a tree so we print the value of $1~\text{mod}~103=1$ as our answer.

Sample Input 1

2 103

Sample Output 1

0

Explanation 1

For $n=2$, there is only one way to build a tree:

This tree is not valid because we can choose to remove either node $1$ or node $2$ in the first step. Thus, we print $0$ as no valid tree exists.

Sample Input 2

3 103

Sample Output 2

3 

Explanation 2

For $n=3$, there are $3$ valid trees depicted in the diagram below (the unique vertex removed in the first step is shown in red):

Thus, we print the value of $3\:\text{mod}\:103=3$ as our answer.

Sample Input 3

4 103

Sample Output 3

4

Explanation 3

For $n=4$, there are $\begin{array}{c}4\end{array}$ valid trees depicted in the diagram below (the unique vertex removed in the first step is shown in red):

The figure below shows an invalid tree with $n=4$:

This tree is not valid because we can choose to remove node $2$ or node $3$ in the first step. Because we had four valid trees, we print the value of $4~\text{mod}~103=4$ as our answer.
