You are given two integers X and Y. You need to construct two different strings S_{1} and S_{2} consisting of only the characters ‘a’ and ‘b’, such that the following conditions are satisfied:

1. Both S_{1} and S_{2} are [palindromes].
2. Both S_{1} and S_{2} should contain exactly X occurrences of \texttt{a} and Y occurrences of \texttt{b}.

If there are multiple possible answers, you may print any of them. If it is not possible to construct two distinct strings satisfying the conditions, print -1 instead.

------ Input Format ------ 

- The first line of input will contain a single integer T, denoting the number of test cases. Then the test cases follow.
- Each test case consists of a single line of input containing two space-separated integers X, Y.

------ Output Format ------ 

For each test case:
- If it is not possible to construct two distinct strings satisfying the conditions, print -1
- Otherwise, print two lines — the first should contain the string S_{1} and the second should contain S_{2}
- If there are multiple possible answers, you may print any of them.

------ Constraints ------ 

$1 ≤ T ≤ 1000$
$1 ≤ X,Y ≤ 10^{3}$

----- Sample Input 1 ------ 
2
2 4
3 3
----- Sample Output 1 ------ 
abbbba
babbab
-1
----- explanation 1 ------ 
Test case $1$: The three palindromes containing $2$ $\texttt{a}$-s and $4$ $\texttt{b}$-s are $\texttt{abbbba}, \texttt{babbab},$ and $\texttt{bbaabb}$. Printing any two of these is a valid answer.

Test case $2$: There are no palindromes containing $3$ each of $\texttt{a}$ and $\texttt{b}$.
