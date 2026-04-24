Read problem statements in [Mandarin], [Russian], and [Vietnamese] as well.

You are given a sequence of integers A_{1}, A_{2}, \ldots, A_{N} and an integer K. Find the number of contiguous subsequences A_{L}, A_{L+1}, \ldots, A_{R} such that R-L+1 ≥ K and the K-th element of the subsequence (A_{L+K-1}) is equal to the maximum of all elements of the entire sequence.

------ Input Format ------ 

- The first line of the input contains a single integer T denoting the number of test cases. The description of T test cases follows.
- The first line of each test case contains two space-separated integers N and K.
- The second line contains N space-separated integers A_{1}, A_{2}, \ldots, A_{N}.

------ Output Format ------ 

For each test case, print a single line containing one integer --- the number of contiguous subsequences satisfying the given conditions.

------ Constraints ------ 

$1 ≤T ≤200$
$1 ≤K ≤N ≤2 \cdot 10^{5}$
$|A_{i}| ≤10^{5}$ for each valid $i$
- the sum of $N$ over all test cases does not exceed $5 \cdot 10^{5}$

------ subtasks ------ 

Subtask #1 (10 points)
$T ≤10$
$N ≤100$

Subtask #2 (90 points) original constraints

----- Sample Input 1 ------ 
1
5 3
1 2 3 4 5
----- Sample Output 1 ------ 
1
----- explanation 1 ------ 
Example case 1: $(3, 4, 5)$ is the only contiguous subsequence such that its $3$-rd element is equal to the maximum of the whole sequence (which is $5$).
