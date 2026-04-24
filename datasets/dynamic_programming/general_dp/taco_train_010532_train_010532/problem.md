You are given a string, $\mbox{S}$, consisting of lowercase English letters.

A string is beautiful with respect to $\mbox{S}$ if it can be derived from $\mbox{S}$ by removing exactly $2$ characters.

Find and print the number of different strings that are beautiful with respect to $\mbox{S}$.

Input Format

A single string of lowercase English letters denoting $\mbox{S}$.

Constraints

$3\leq|S|\leq10^6$
$3\leq|S|\leq20$ holds for test cases worth at least $15\%$ of the problem's score.
$3\leq|S|\leq2000$ holds for test cases worth at least $30\%$ of the problem's score.

Output Format

Print the number of different strings that are beautiful with respect to $\mbox{S}$.

Sample Input
abba

Sample Output
4

Explanation

$S=\{abba\}$ 

The following strings can be derived by removing $2$ characters from $\mbox{S}$: $ab,bb,ba,ab,ba,aa,\text{and}bb$.

This gives us our set of unique beautiful strings, $B=\{ab,ba,aa,bb\}$. As $|B|=4$, we print $4$.
