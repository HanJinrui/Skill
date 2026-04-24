Given an array $A$ of length $N$, we can define rotation as follows. If we rotate $A$ to the right, all elements move to the right one unit, and the last element moves to the beginning. That is, it becomes $[A_{N}, A_{1},A_{2},\ldots,A_{N-1}]$. Similarly if we rotate $A$ to the left, it becomes $[A_{2},A_{3},\ldots,A_{N}, A_{1}]$.

Given an array $A$ and an integer $x$, define $f(A,x)$ to be the array $A$ rotated by the amount $x$. If $x≥ 0$, this means we rotate it right $x$ times. If $x<0$, this means we rotate it left $|x|$ times.

You are given an array $A$ of length $N$. Then $Q$ queries follow. In each query, an integer $x$ is given. To answer the query, you should replace $A$ with $A+f(A,x)$ where $+$ denotes concatenation. After this operation, you must output the sum of all elements of $A$. Since this number can be large, output it modulo $10^{9} + 7$.

Note that the queries are cumulative. When you modify $A$ to answer one query, it starts that way for the next query.

------ Input ------

The first line contains an integer $N$ - the size of the initial array. 
The second line contains $N$ integers $A_{1},\ldots, A_{N}$ - the elements of the initial array.
The third line contains an integer $Q$ - the number of queries.
The fourth line contains $Q$ space-separated integers $x_{1},\ldots, x_{Q}$, where $x_{i}$ is the parameter of the $i$-th query.

------ Output ------
After each query, output in a single line the the sum of all elements of the current array modulo $10^{9}+7$.

------ Constraints  ------
$ 1≤ N≤ 10^{5}$
$ 1≤ Q≤ 10^{5}$
$ -10^{9}≤ A_{i}≤ 10^{9}$ 
$ -10^{5} ≤ x_{i}≤ 10^{5}$ 

------ Subtasks ------

Subtask #1 (100 points): original constraints

----- Sample Input 1 ------ 
2
1 2
2
1 1
----- Sample Output 1 ------ 
6
12
----- explanation 1 ------ 
Initially, the array is $[1,2]$.
After the first query, the array becomes $[1, 2] + f([1, 2], 1) = [1, 2] + [2, 1] = [1, 2, 2, 1]$. The total sum is $6$.
After the second query, the array becomes $[1, 2, 2, 1] + f([1, 2, 2, 1], 1) = [1, 2, 2, 1] + [1, 1, 2, 2] = [1, 2, 2, 1, 1, 1, 2, 2]$. The total sum is $12$.
