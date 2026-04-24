Chef is given two strings A and B of length N containing lowercase English letters.

Chef can rearrange both the strings in any way he wants. He wants to minimize the length of LCS ([Longest Common Subsequence] of both the strings.

Find the minimum length of LCS of A and B if he optimally rearranges both the strings.

------ Input Format ------ 

- The first line of input will contain a single integer T, denoting the number of test cases.
- Each test case consists of multiple lines of input.
- The first line of each test case contains an integer N - denoting the length of A and B.
- The second line of each test case contains a string A.
- The third line of each test case contains a string B.

------ Output Format ------ 

For each test case, output the minimum length of LCS Chef can obtain.

------ Constraints ------ 

$1 ≤ T ≤ 1000$
$1 ≤ N ≤ 10^{5}$
$A$ and $B$ contain lowercase English letters
- The sum of $N$ over all test cases does not exceed $2 \cdot 10^{5}$.

----- Sample Input 1 ------ 
3
4
aaaa
aaab
1
c
z
5
abcde
cdefg

----- Sample Output 1 ------ 
3
0
1

----- explanation 1 ------ 
Test case 1: $\mathrm{LCS}(\texttt{aaaa}, \texttt{aaab}) = \texttt{aaa}$. It can be shown that no other rearrangement of the strings produces a smaller LCS.

Test case 3: $\mathrm{LCS}(\texttt{acbed}, \texttt{gdefc}) = \texttt{c}$. Note that multiple longest common subsequences exist for this arrangement. It can be shown that no other rearrangement of the strings produces a smaller LCS.
