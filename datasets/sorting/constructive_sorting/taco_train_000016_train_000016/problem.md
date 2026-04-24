You are given an array A of N integers A_{1}, A_{2}, \ldots, A_{N}. Determine if there are two [permutations] B and C of this array, for which the following condition is satisfied:

* There doesn't exist a pair of integers (i, j) such that 1 ≤ i ≤ j ≤ N and (i, j) \neq (1, N), for which the subarray B[i:j] is a permutation of subarray C[i:j].

If there exist such permutations, find any of them.

As a reminder, B[i:j] refers to the subarray [B_{i}, B_{i+1}, \ldots, B_{j}]

------ Input Format ------ 

- The first line of the input contains a single integer T, the number of test cases. The description of the test cases follows.
- The first line of each test case contains a single integer N — the number of integers.
- The second line of each test case contains N space-separated integers A_{1}, A_{2}, \ldots, A_{N}.

------ Output Format ------ 

For each test case, if there are no such permutations B and C, output NO.

Otherwise, on the first line output YES. In the next line, output N integers B_{1}, B_{2}, \ldots, B_{N}. In the next line, output N integers C_{1}, C_{2}, \ldots, C_{N}.

You may print each character of YES/NO in either uppercase or lowercase (for example, the strings YES, yeS, YeS, and yEs will all be treated as identical).

------ Constraints ------ 

$1 ≤T ≤100$
$3 ≤N ≤1000$
$0 ≤A_{i} ≤10^{9}$
- The sum of $N$ over all test cases doesn't exceed $2000$.

----- Sample Input 1 ------ 
3
3
1 1 2
4
19 39 19 84
6
1 2 3 1 2 3
----- Sample Output 1 ------ 
NO
YES
19 19 39 84 
39 84 19 19 
YES
1 1 2 2 3 3 
2 3 3 1 1 2 
----- explanation 1 ------ 
Test case $1$: There are $3 \times 3 = 9$ pairs of permutations of the given array. Here's why they're all bad:
- If $B = [1, 1, 2]$ and $C = [1, 1, 2]$, $B[1:1] = C[1:1]$
- If $B = [1, 1, 2]$ and $C = [1, 2, 1]$, $B[1:1] = C[1:1]$
- If $B = [1, 1, 2]$ and $C = [2, 1, 1]$, $B[2:2] = C[2:2]$
- If $B = [1, 2, 1]$ and $C = [1, 1, 2]$, $B[1:1] = C[1:1]$
- If $B = [1, 2, 1]$ and $C = [1, 2, 1]$, $B[1:1] = C[1:1]$
- If $B = [1, 2, 1]$ and $C = [2, 1, 1]$, $B[3:3] = C[3:3]$
- If $B = [2, 1, 1]$ and $C = [1, 1, 2]$, $B[2:2] = C[2:2]$
- If $B = [2, 1, 1]$ and $C = [1, 2, 1]$, $B[3:3] = C[3:3]$
- If $B = [2, 1, 1]$ and $C = [2, 1, 1]$, $B[1:1] = C[1:1]$
