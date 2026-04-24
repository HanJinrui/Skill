You are given a binary string S of length N. You can perform the following operation on it:
Pick any non-empty even-length [subsequence] of the string.
Suppose the subsequence has length 2k. Then, move the first k characters to the beginning of S and the other k to the end of S (without changing their order).

For example, suppose S = 01100101110. Here are some moves you can make (the chosen subsequence is marked in red):
0\textcolor{red}{1}10\textcolor{red}{0}101110 \to \textcolor{red}{1}010101110\textcolor{red}{0}
01\textcolor{red}{10}01\textcolor{red}{0}1\textcolor{red}{1}10 \to \textcolor{red}{10}0101110\textcolor{red}{01}
011\textcolor{red}{00101110} \to \textcolor{red}{0010}011\textcolor{red}{1110}

What is the lexicographically smallest string that can be obtained after performing this operation several (possibly, zero) times?

Note: A binary string A is said to be lexicographically smaller than another binary string B of the same length if there exists an index i such that:
A_{1} = B_{1}, A_{2} = B_{2}, \ldots, A_{i-1} = B_{i-1}
A_{i} = 0 and B_{i} = 1.

------ Input Format ------ 

- The first line of input will contain a single integer T, denoting the number of test cases. The description of the test cases follows.
- Each test case consists of two lines of input.
- The first line of each test case contains a single integer N, the length of string S.
- The second line contains a binary string of length N.

------ Output Format ------ 

For each testcase, output a single line containing the lexicographically shortest binary string that can be obtained by performing the given operation several times.

------ Constraints ------ 

$1 ≤ T ≤ 10^{5}$
$1 ≤ N ≤ 2\cdot 10^{5}$
$S$ is a binary string, i.e, contains only the characters $0$ and $1$.
- The sum of $N$ across all test cases won't exceed $2\cdot 10^{5}$.

----- Sample Input 1 ------ 
4
2
10
4
1001
5
11111
7
0010100

----- Sample Output 1 ------ 
10
0011
11111
0000011

----- explanation 1 ------ 
Test case $1$: There's only one move possible, and it gives back the original string when made. So, $S$ cannot be changed, and the answer is $10$.

Test case $2$: Make the following moves:
- $1\textcolor{red}{0}0\textcolor{red}{1} \to \textcolor{red}{0}10\textcolor{red}{1}$
- $\textcolor{red}{01}01 \to \textcolor{red}{0}01\textcolor{red}{1}$

This is the lexicographically smallest string.

Test case $3$: Performing any move doesn't change the string.

Test case $4$: Make the move $\textcolor{red}{001}0\textcolor{red}{1}00 \to \textcolor{red}{00}000\textcolor{red}{11}$.
