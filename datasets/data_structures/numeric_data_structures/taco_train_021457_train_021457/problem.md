Read problems statements in Mandarin chinese, Russian and Vietnamese as well. 

You are given an integer sequence $A$ with length $N$.

Find the number of (unordered) pairs of elements such that the average of these two elements is also present in the sequence. Formally, find the number of pairs $(i,j)$ such that $1 ≤ i < j ≤ N$ and there is an index $k$ ($1 ≤ k ≤ N$) for which $2A_{k} = A_{i}+A_{j}$ holds.

------  Input ------
The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
The first line of each test case contains a single integer $N$.
The second line contains $N$ space-separated integers $A_{1}, A_{2}, \dots, A_{N}$.

------  Output ------
For each test case, print a single line containing one integer — the number of valid pairs $(i,j)$.

------  Constraints  ------
$1 ≤ T ≤ 10$
$1 ≤ N ≤ 10^{5}$
$|A_{i}| ≤ 10^{3}$ for each valid $i$

------  Subtasks ------

Subtask #1 (30 points): $1 ≤ N ≤ 10^{3}$

Subtask #2 (70 points): $1 ≤ N ≤ 10^{5}$

----- Sample Input 1 ------ 
3
2
2 2
3
2 1 3
6
4 2 5 1 3 5
----- Sample Output 1 ------ 
1
1
7
----- explanation 1 ------ 
Example case 1: We can take $k$ for $A_{k}$ to be either 1 or 2, since $A_{k}=2$ either way. Since the problem asks for unordered pairs, $(1,2)$ is the only possible valid pair (the same as $(2,1)$). Hence, the answer is 1.

Example case 2: We see that $A_{1} = 2 = (1+3)/2$. No other valid pair exists.
