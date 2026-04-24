Chef invented a modified wordle.

There is a hidden word S and a guess word T, both of length 5.

Chef defines a string M to determine the correctness of the guess word. For the i^{th} index:
If the guess at the i^{th} index is correct, the i^{th} character of M is \texttt{G}.
If the guess at the i^{th} index is wrong, the i^{th} character of M is \texttt{B}.

Given the hidden word S and guess T, determine string M.

------ Input Format ------ 

- First line will contain T, number of test cases. Then the test cases follow.
- Each test case contains of two lines of input.
- First line contains the string S - the hidden word.
- Second line contains the string T - the guess word.

------ Output Format ------ 

For each test case, print the value of string M.

You may print each character of the string in uppercase or lowercase (for example, the strings \texttt{BgBgB}, \texttt{BGBGB}, \texttt{bgbGB} and \texttt{bgbgb} will all be treated as identical).

------ Constraints ------ 

$1 ≤ T ≤ 1000$
$|S| = |T| = 5$
$S, T$ contain uppercase english alphabets only.

----- Sample Input 1 ------ 
3
ABCDE
EDCBA
ROUND
RINGS
START
STUNT

----- Sample Output 1 ------ 
BBGBB
GBBBB
GGBBG

----- explanation 1 ------ 
Test Case $1$: Given string $S = \texttt{ABCDE}$ and $T = \texttt{EDCBA}$. The string $M$ is:
- Comparing the first indices, $\texttt{A} \neq \texttt{E}$, thus, $M[1] = \texttt{B}$.
- Comparing the second indices, $\texttt{B} \neq \texttt{D}$, thus, $M[2] = \texttt{B}$.
- Comparing the third indices, $\texttt{C} = \texttt{C}$, thus, $M[3] = \texttt{G}$.
- Comparing the fourth indices, $\texttt{D} \neq \texttt{B}$, thus, $M[4] = \texttt{B}$.
- Comparing the fifth indices, $\texttt{E} \neq \texttt{A}$, thus, $M[5] = \texttt{B}$.  
Thus, $M = \texttt{BBGBB}$.

Test Case $2$: Given string $S = \texttt{ROUND}$ and $T = \texttt{RINGS}$. The string $M$ is:
- Comparing the first indices, $\texttt{R} = \texttt{R}$, thus, $M[1] = \texttt{G}$.
- Comparing the second indices, $\texttt{O} \neq \texttt{I}$, thus, $M[2] = \texttt{B}$.
- Comparing the third indices, $\texttt{U} \neq \texttt{N}$, thus, $M[3] = \texttt{B}$.
- Comparing the fourth indices, $\texttt{N} \neq \texttt{G}$, thus, $M[4] = \texttt{B}$.
- Comparing the fifth indices, $\texttt{D} \neq \texttt{S}$, thus, $M[5] = \texttt{B}$.  
Thus, $M = \texttt{GBBBB}$.
