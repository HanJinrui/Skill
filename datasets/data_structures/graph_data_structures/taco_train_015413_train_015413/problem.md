Let us define the score of an array B (B_{1}, B_{2}, B_{3},...,B_{k}) as:

\begin{equation}
score(B)=\begin{cases}
\sum_{i=1}^{k}B_{i}, & \text{if } k > 1 \text{ and } Max(B) - SecondMax(B) < X.\\
-\sum_{i=1}^{k}B_{i}, & \text{otherwise}.
\end{cases}
\end{equation}

Here, SecondMax(B) denotes the second element in B if we sort it in non-increasing order.

You are given an array A with N elements. You can partition it into multiple continuous subarrays, aiming to maximize the sum of the scores of each of the subarrays. Note that, in a partition, each element of the array belongs to exactly one subarray.

Additionally, you should perform Q queries. For each given value of X, find the maximum sum of score if you partition the array optimally.

------ Input Format ------ 

- The first line contains T - the number of test cases. Then the test cases follow.
- The first line of each test case contains two integers N and Q - the size of the array A and the number of queries.
- The second line contains N space-separated integers A_{1}, A_{2}, \ldots, A_{N}.
- The third line contains Q space-separated integers X_{1}, X_{2}, \ldots, X_{Q}.

------ Output Format ------ 

For each test case, output Q space-separated integers in a new line, the maximum sum of score you can obtain.

------ Constraints ------ 

$1 ≤ T ≤ 10^{5}$
$2 ≤ N ≤ 3\cdot 10^{5}$
$1 ≤ A_{i},X_{i} ≤ 10^{9}$
- Sum of $N$ over all test cases does not exceed $3\cdot 10^{5}$.
- Sum of $Q$ over all test cases does not exceed $3\cdot 10^{5}$.

----- Sample Input 1 ------ 
2
5 3
1 4 3 6 2
1 4 2
5 2
5 7 10 1 1
2 3
----- Sample Output 1 ------ 
-16 16 0 
-20 4
----- explanation 1 ------ 
Test case $1$: In the third query of the first testcase, an optimal partition is $[1, 4, 3], [6, 2]$. The sum of score is $(1 + 4 + 3) - (6 + 2) = 0$.

Test case $2$: In the second query of the second testcase, an optimal partition is $[5, 7], [10], [1, 1]$. The sum of score is $(5 + 7) - (10) + (1 + 1) = 4$.
