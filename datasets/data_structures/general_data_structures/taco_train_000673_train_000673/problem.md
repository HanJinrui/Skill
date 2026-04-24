Treeland is a country with $n$ cities and $n-1$ roads. There is exactly one path between any two cities.  

The ruler of Treeland wants to implement a self-driving bus system and asks tree-loving Alex to plan the bus routes. Alex decides that each route must contain a subset of connected cities; a subset of cities is connected if the following two conditions are true:

There is a path between every pair of cities which belongs to the subset.
Every city in the path must belong to the subset.

In the figure above, $\{2,3,4,5\}$ is a connected subset, but $\{6,7,9\}$ is not  (for the second condition to be true, $8$ would need to be part of the subset).

Each self-driving bus will operate within a connected segment of Treeland. A connected segment $[L,R]$ where $1\leq L\leq R\leq n$ is defined by the connected subset of cities $S=\{x\ |x\in Z\ \text{and}\ \ L\leq x\leq R\}$. 

In the figure above, $[2,5]$ is a connected segment that represents the subset $\{2,3,4,5\}$. Note that a single city can be a segment too.

Help Alex to find number of connected segments in Treeland.

Input Format

The first line contains a single positive integer, $n$. 
The $n-1$ subsequent lines each contain two positive space-separated integers, $a_i$ and $b_i$, describe an edge connecting two nodes in tree $\mathbf{T}$.

Constraints

$1\leq n\leq2\times10^5$

$1\leq a_i,b_i\leq n$

Subtasks    

For $25\%$ score: $1\leq n\leq2\times10^3$

For $50\%$ score: $1\leq n\leq10^4$

Output Format

Print a single integer: the number of segments $[L,R]$, which are connected in tree $\mathbf{T}$.

Sample Input
3
1 3
3 2

Sample Output
5

Explanation

The connected segments for our test case are: $[1,1]$, $[2,2]$, $[3,3]$, $[2,3]$, and $[1,3]$. These segments can be represented by the respective subsets: $\{1\}$, $\{2\}$, $\{3\}$, $\{2,3\}$, and $\{1,2,3\}$.

Note: $[1,2]$ is not a connected segment. It represents the subset $\{1,2\}$ and the path between $1$ and $2$ goes through $3$ which is not a member of the subset.
