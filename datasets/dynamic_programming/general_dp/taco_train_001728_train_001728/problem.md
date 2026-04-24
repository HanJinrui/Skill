Penny has an array of $n$ integers, $[a_0,a_1,\ldots,a_{n-1}]$. She wants to find the number of unique multisets she can form using elements from the array such that the bitwise XOR of all the elements of the multiset is a prime number. Recall that a multiset is a set which can contain duplicate elements.

Given $\textit{q}$ queries where each query consists of an array of integers, can you help Penny find and print the number of valid multisets for each array? As these values can be quite large, modulo each answer by $10^9+7$ before printing it on a new line.

Input Format

The first line contains a single integer, $\textit{q}$, denoting the number of queries. The $2\cdot q$ subsequent lines describe each query in the following format:

The first line contains a single integer, $n$, denoting the number of integers in the array.
The second line contains $n$ space-separated integers describing the respective values of $a_0,a_1,\ldots,a_{n-1}$.

Constraints

$1\leq q\leq10$  
$1\leq n\leq1000000$
$3500\leq a_i\leq4500$

Output Format

On a new line for each query, print a single integer denoting the number of unique multisets Penny can construct using numbers from the array such that the bitwise XOR of all the multiset's elements is prime. As this value is quite large, your answer must be modulo $10^9+7$.

Sample Input
1   
3   
3511 3671 4153  

Sample Output
4

Explanation

The valid multisets are:

$\{3511\}\rightarrow3511$ is prime.
$\{3671\}\to3671$ is prime.
$\{4153\}\rightarrow4153$ is prime.
$\{3511,3671,4153\}\to3511\oplus3671\oplus4153\text{=5081}$, which is prime.

Because there are four valid multisets, we print the value of $4\%(10^9+7)=4$ on a new line.
