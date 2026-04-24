Let f(X) denote the number of set bits in X.

Given integers N and K, construct an array A of length N such that:
0 ≤ A_{i} ≤ K for all (1 ≤ i ≤ N);
\sum_{i=1}^{N} A_{i} = K

Over all such possible arrays, find the maximum value of \sum_{i=1}^{N} f(A_{i}).

------ Input Format ------ 

- The first line of input contains a single integer T - the number of test cases. The description of T test cases follow.
- The only line of each test case contains integers N and K- the length of the array and sum of elements respectively.

------ Output Format ------ 

For each test case, output the maximum value of \sum_{i=1}^{N} f(A_{i}).

------ Constraints ------ 

$1 ≤ T ≤ 10^{4}$
$1 ≤ N ≤ 10^{9}$
$0 ≤ K ≤ 10^{9}$

----- Sample Input 1 ------ 
2
1 7
3 6

----- Sample Output 1 ------ 
3
4

----- explanation 1 ------ 
Test case $1$: Only one array is possible that is $A =[7]$. As $7 = (111)_2$, the number of set bits in $7$ is $3$. Thus, $\sum_{i=1}^{N} f(A_{i}) = f(7) = 3$.

Test case $2$: A possible array satisfying all the conditions is $A =[3, 0, 3]$. As $3 = (11)_2$, the number of set bits in $3$ is $2$. Similarly, the number of set bits in $0$ is $0$. Thus, $\sum_{i=1}^{N} f(A_{i}) = f(3) + f(0) + f(3) = 4$. It can be proven that answer never exceeds $4$.
