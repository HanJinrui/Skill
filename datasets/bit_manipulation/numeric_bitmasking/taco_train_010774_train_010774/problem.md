Read problem statements in [Bengali], [Mandarin Chinese], [Russian], and [Vietnamese] as well.

Given an array A_{1}, A_{2} \ldots A_{N}, find the minimum number of operations (possibly zero) required to convert all integers in A to 0.

In one operation, you
choose a non-negative integer p (p ≥ 0),
select at most K indices in the array A, and
for each selected index i, replace A_{i} with A_{i}\oplus 2^{p}. Here, \oplus denotes bitwise XOR.

------  Subtasks ------
Subtask #1 (100 points): Original Constraints

------ Input Format ------ 

- The first line contains an integer T - the number of test cases. Then T test cases follow.
- The first line of each test case contains two integers N, K - the size of the array and the maximum number of elements you can select in an operation.
- The second line of each test case contains N integers A_{1}, A_{2} \ldots A_{N}.

------ Output Format ------ 

For each test case, output the minimum number of operations to make all elements of the array 0.

------ Constraints ------ 

$1 ≤ T ≤ 10^{5}$
$1 ≤ N, K ≤ 10^{5}$
$0 ≤ A_{i} ≤ 10^{9}$
- The sum of $N$ over all test cases does not exceed $2\cdot 10^{5}$

----- Sample Input 1 ------ 
1
3 2
3 6 10

----- Sample Output 1 ------ 
5
----- explanation 1 ------ 
Here is one way to achieve $[0, 0, 0]$ from $[3, 6, 10]$ in $5$ operations:
1. Choose $p = 0$ and indices $\{1\}$. Now $A$ becomes $[2, 6, 10]$.
2. Choose $p = 1$ and indices $\{1,2\}$. Now $A$ becomes $[0, 4, 10]$.
3. Choose $p = 1$ and indices $\{3\}$. Now $A$ becomes $[0, 4, 8]$.
4. Choose $p = 2$ and indices $\{2\}$. Now $A$ becomes $[0, 0, 8]$.
5. Choose $p = 3$ and indices $\{3\}$. Now $A$ becomes $[0, 0, 0]$.

It can be shown that at least $5$ operations are required.
