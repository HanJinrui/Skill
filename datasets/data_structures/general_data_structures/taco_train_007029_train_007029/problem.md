You are given a tree with N nodes and each has a value associated with it. You are given Q queries, each of which is either an update or a retrieval operation. 

Initially all node values are zero.  

The update query is of the format

a1 d1 a2 d2 A B

This means you'd have to add $(a1+z*d1)*(a2+z*d2)*R^z$ in all nodes in the path from A to B where $z$ is the distance between the node and A.

The retrieval query is of the format

i j

You need to return the sum of the node values lying in the path from node i to node j modulo 1000000007. 

Note:   

First all update queries are given and then all retrieval queries.  
Distance between 2 nodes is the shortest path length between them taking each edge weight as 1.  

Input Format  

The first line contains two integers (N and R respectively) separated by a space.  

In the next N-1 lines, the i^{th} line describes the i^{th} edge: a line with two integers x y separated by a single space denotes an edge between nodes x and y.  

The next line contains 2 space separated integers (U and Q respectively) representing the number of Update and Query operations to follow.  

U lines follow. Each of the next U lines contains 6 space separated integers (a1,d1,a2,d2,A and B respectively).

Each of the next Q lines contains 2 space separated integers, i and j respectively. 

Output Format  

It contains exactly Q lines and each line containing the answer of the i^{th} query.

Constraints

2 <= N <= $10^{5} $

2 <= R <= $10^{9} $

1 <= U <= $10^{5} $

1 <= Q <= $10^{5} $

1 <= a1,a2,d1,d2 <= $10^{8} $

1 <= x, y, i, j, A, B  <= N  

Note 

For the update operation, x can be equal to y and for the query operation, i can be equal to j.  

Sample Input  

7 2
1 2
1 3
2 4
2 6
4 5
6 7
1 4
1 1 1 1 4 6
4 5
2 7
4 7
5 3

Sample Output

1
44
45
9

Explanation

The node values after updation becomes :  

0 8 0 1 0 36 0

Answer to Query #1: 1+0 = 1   

Answer to Query #2: 8+36+0 = 44

Answer to Query #3: 1+8+36+0 = 45

Answer to Query #4: 0+1+8+0+0 = 9
