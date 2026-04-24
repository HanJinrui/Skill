Given two strings, $a$ and $\boldsymbol{b}$, find and print the total number of ways to insert a character at any position in string $\class{ML__boldsymbol}{\boldsymbol{a}}$ such that the length of the Longest Common Subsequence of characters in the two strings increases by one.

Input Format

The first line contains a single string denoting $\class{ML__boldsymbol}{\boldsymbol{a}}$. 

The second line contains a single string denoting $\boldsymbol{b}$.

Constraints

Scoring     

$1\leq|a|,|b|\leq5000$
Strings $\class{ML__boldsymbol}{\boldsymbol{a}}$ and $\boldsymbol{b}$ are alphanumeric (i.e., consisting of arabic digits and/or upper and lower case English letters).
The new character being inserted must also be alphanumeric (i.e., a digit or upper/lower case English letter).

Subtask     

$1\le|a|,|b|\le1000$ for $\boldsymbol{66.67\%}$ of the maximum score.  

Output Format

Print a single integer denoting the total number of ways to insert a character into string $\class{ML__boldsymbol}{\boldsymbol{a}}$ in such a way that the length of the longest common subsequence of $\class{ML__boldsymbol}{\boldsymbol{a}}$ and $\boldsymbol{b}$ increases by one.

Sample Input
aa
baaa

Sample Output
4

Explanation

The longest common subsequence shared by $a=\text{"a}\textbf{a}$ and $b=\text{"baaa''}$ is aa, which has a length of $2$. There are two ways that the length of the longest common subsequence can be increased to $3$ by adding a single character to $\class{ML__boldsymbol}{\boldsymbol{a}}$:

There are $3$ different positions in string $\class{ML__boldsymbol}{\boldsymbol{a}}$ where we could insert an additional a to create longest common subsequence aaa (i.e., at the beginning, middle, and end of the string). 
We can insert a b at the beginning of the string for a new longest common subsequence of baa.

As we have $3+1=4$ ways to insert an alphanumeric character into $\class{ML__boldsymbol}{\boldsymbol{a}}$ and increase the length of the longest common subsequence by one, we print $\begin{array}{c}4\end{array}$ on a new line.
