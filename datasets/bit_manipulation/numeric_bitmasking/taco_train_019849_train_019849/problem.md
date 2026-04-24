Chef has two non negative integers N and X. He now wants to find the number of integers K such that 0 ≤ K < N, and (N \oplus K) \And X = 0. 

Note that \oplus denotes the bitwise XOR operator and \And denotes the bitwise AND operator.

Help Chef in finding the total required count.

------ Input Format ------ 

- The first line of input will contain a single integer T, denoting the number of test cases.
- Each test case consists of a single line of input containing N and X denoting the two integers as described in the statement.

------ Output Format ------ 

For each test case, output the total number of integers K which satisfy the requirements mentioned.

------ Constraints ------ 

$1 ≤ T ≤ 10^{5}$
$1 ≤ N, X ≤ 2^{30} - 1$

------ subtasks ------ 

Subtask 1 (10 points): $1 ≤ M ≤ 10$
Subtask 2 (20 points): The sum of $N$ across all test cases won't exceed $20$.
Subtask 3 (70 points): No further constraints.

----- Sample Input 1 ------ 
3
4 5
8 4
1 2

----- Sample Output 1 ------ 
0
4
1

----- explanation 1 ------ 
Testcase 1: $N = 4, X = 5$. So we need to find the number of $K$, which satisfy $0 ≤ K 
< 4$, and $(4 \oplus K) \And 5 = 0$.

- $(100_{2} \oplus 000_{2}) \And 101_{2} = 100_{2} \And 101_{2} = 100_{2} \neq 0$
- $(100_{2} \oplus 001_{2}) \And 101_{2} = 101_{2} \And 101_{2} = 101_{2} \neq 0$
- $(100_{2} \oplus 010_{2}) \And 101_{2} = 110_{2} \And 101_{2} = 100_{2} \neq 0$
- $(100_{2} \oplus 011_{2}) \And 101_{2} = 111_{2} \And 101_{2} = 101_{2} \neq 0$

So, we have looked at all values of $K$, and found no value which satisfies the requirements. So the answer is $0$.
