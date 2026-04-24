Read problem statements in [Mandarin], [Bengali], [Russian], and [Vietnamese] as well.

You are given an undirected graph with N nodes (numbered 1 through N). For each valid i, the i-th node has a weight W_{i}. Also, for each pair of nodes i and j, there is an edge connecting these nodes if j - i \neq W_{j} - W_{i}.

Find the number of connected components in this graph.

------ Input Format ------ 

- The first line of the input contains a single integer T denoting the number of test cases. The description of T test cases follows.
- The first line of each test case contains a single integer N.
- The second line contains N space-separated integers W_{1}, W_{2}, \ldots, W_{N}.

------ Output Format ------ 

For each test case, print a single line containing one integer --- the number of connected components in the graph.

------ Constraints ------ 

$1 ≤T ≤10^{4}$
$1 ≤N ≤10^{5}$
$|W_{i}| ≤10^{9}$ for each valid $i$
- the sum of $N$ over all test cases does not exceed $2 \cdot 10^{5}$

------ subtasks ------ 

Subtask #1 (30 points):
$N ≤10^{3}$
the sum of $N$ over all test cases does not exceed $2 \cdot 10^{3}$

Subtask #2 (70 points): original constraints

----- Sample Input 1 ------ 
2
2
1 2
2
2 1

----- Sample Output 1 ------ 
2
1
----- explanation 1 ------ 
Example case 1: For $i=1$ and $j=2$, we have $2-1 = 2-1$, therefore there are no edges in the graph and there are two connected components.

Example case 2: For $i=1$ and $j=2$, we have $2-1 \neq 1-2$, therefore there is an edge between $1$ and $2$, the graph is connected, so there is only one connected component.
