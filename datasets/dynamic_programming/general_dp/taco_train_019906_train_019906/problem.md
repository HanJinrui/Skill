Lukas is a Civil Engineer who loves designing road networks to connect $n$ cities numbered from $1$ to $n$. He can build any number of bidirectional roads as long as the resultant network satisfies these constraints:

It must be possible to reach any city from any other city by traveling along the network of roads.  
No two roads can directly connect the same two cities.   
A road cannot directly connect a city to itself.  

In other words, the roads and cities must form a simple connected labeled graph.

You must answer $\textit{q}$ queries, where each query consists of some $n$ denoting the number of cities Lukas wants to design a bidirectional network of roads for. For each query, find and print the number of ways he can build roads connecting $n$ cities on a new line; as the number of ways can be quite large, print it modulo $663224321$.

Input Format

The first line contains an integer, $\textit{q}$, denoting the number of queries. 

Each of the $\textit{q}$ subsequent lines contains an integer denoting the value of $n$ for a query.

Constraints

$1\leq q,n\leq10^5$

Output Format

For each of the $\textit{q}$ queries, print the number of ways Lukas can build a network of bidirectional roads connecting $n$ cities, modulo $663224321$, on a new line.

Sample Input 0
3
1
3
10

Sample Output 0
1
4
201986643

Explanation 0

We answer the first two queries like this:

When $n=1$, the only option satisfying Lukas' three constraints is to not build any roads at all. Thus, we print the result of $1~\text{mod}~663224321=1$ on a new line.  

When $n=3$, there are four ways for Lukas to build roads that satisfy his three constraints:

Thus, we print the result of $4~\text{mod}~663224321=4$ on a new line.
