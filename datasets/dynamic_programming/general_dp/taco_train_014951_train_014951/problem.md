Zurikela is creating a graph with a special graph maker. At the begining, it is empty and has no nodes or edges. He can perform $3$ types of operations:    

$\mbox{A}$ $\boldsymbol{x}$: Create a set of $\boldsymbol{x}$ new nodes and name it $\boldsymbol{set}$-$\mbox{K}$.    
$\mbox{B}$ $\boldsymbol{x}$ $y$: Create edges between nodes of $\boldsymbol{set}$-$\boldsymbol{x}$ and $\boldsymbol{set}$-$y$.      
$\mbox{C}$ $\boldsymbol{x}$: Create a set composed of nodes from $\boldsymbol{set}$-$\boldsymbol{x}$ and its directly and indirectly connected nodes, called $\boldsymbol{set}$-$\mbox{K}$. Note that each node can only exist in one set, so other sets become empty.     

The first $\boldsymbol{set}$'s name will be $\boldsymbol{set}$-$\mbox{1}$. In first and third operation $\mbox{K}$ is referring to the index of new set:

K = [index of last created set] + 1

Create the graph by completing the $\mbox{Q}$ operations specified during input. Then calculate the maximum number of independent nodes (i.e.:how many nodes in the final graph which don't have direct edge between them).

Input Format

The first line contains $\mbox{Q}$. 

The $\mbox{Q}$ subsequent lines each contain an operation to be performed.

Constraints 

$1\leq Q\leq10^5$.

For the first operation, $1\leq x\leq10^4$. 

For the second operation, $x<y$ and all $y$s are distinct.

For the second and third operation, it's guaranteed that $\boldsymbol{set}$-$\boldsymbol{x}$ and $\boldsymbol{set}$-$y$ exist.     

Output Format

Print maximum number of independent nodes in the final graph (i.e.: nodes which have no direct connection to one another).

Sample Input
8
A 1
A 2
B 1 2
C 1
A 2
A 3
B 3 4
B 4 5

Sample Output
5

Explanation

There are $8$ operations.

After first operation$\left({A\mbox{1}}\right)$:

After second operation$\left({A\mbox{2}}\right)$:

After third operation$(B\:1\:2)$:

After fourth operation$\left({C1}\right)$:

After fifth and sixth operation $\left({A\mbox{2}}\right)$ and $(A3)$:

After seventh operation$\left({B\:\:3\:\:4}\right)$:

After eigth operation$\left(B\:4\:5\right)$:

There are $2$ independent nodes in $\boldsymbol{set}$-$3$ and $3$ independent nodes in $\boldsymbol{set}$-$5$, so we print their sum ($5$) as our answer.
