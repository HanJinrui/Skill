You are given a string $\mbox{S}$, consisting of $N$ small latin letters 'a' and 'b'. You are also given $\mbox{M}$ queries to process. The queries are as follows:

C $\boldsymbol{l}$ $\textbf{r}$ $\mbox{ch}$: all the symbols in the string, starting at the ${l}^{\mbox{th}}$, ending at the $r^{\mbox{th}}$ become equal to $\mbox{ch}$;  
S $\boldsymbol{l}_{1}$ $r_1$ $l_2$ $r_2$: swap two consecutive fragments of the string, where the first is denoted by a substring starting from $\boldsymbol{l}_{1}$ ending at $r_1$ and the second is denoted by a substring starting at $l_2$ ending at $r_2$;   
R $\boldsymbol{l}$ $\textbf{r}$: reverse the fragment of the string that starts at the ${l}^{\mbox{th}}$ symbol and ends at the $r^{\mbox{th}}$ one;  
W $\boldsymbol{l}$ $\textbf{r}$: output the substring of the string that starts at the ${l}^{\mbox{th}}$ symbol and ends at the $r^{\mbox{th}}$ one;  
H $\boldsymbol{l}_{1}$ $l_2$ $\mbox{len}$: output the Hamming distance between the consecutive substrings that starts at $\boldsymbol{l}_{1}$ and $l_2$ respectively and have the length of $\mbox{len}$.  

Everything is 1-indexed here.

Input Format

The first line of input contains a single integer $N$ $\textbf{-}$ the length of the string. 

The second line contains the initial string $\mbox{S}$ itself. 

The third line of input contains a single integer $\mbox{M}$ $\textbf{-}$ the number of queries. 

Then, there are $\mbox{M}$ lines, each denotes a query of one of the types above.  

Constraints

$1\leq N\leq50000$ 

$1\leq M\leq75000$ 

Total number of characters printed in W-type queries will not exceed $2\cdot10^{6}$ 

For C-type, R-type, W-type queries: $1\leq l\leq r\leq N$; $\mbox{ch}$ equals either a, or b 

For S-type queries: $1\leq l_1\leq r_1<l_2\leq r_2\leq N$ 

For H-type queries: $1\leq l_1,l_2\leq N$; $l_i+len-1\leq N$; $1\leq len\leq N$.  

Output Format

For each query of the type W or the type H output an answer on the separate line of output.

Sample Input 0
10
aabbbabbab
6
R 1 5
W 3 8
C 4 4 a
H 2 1 9
S 5 9 10 10
H 1 2 9

Sample Output 0
baaabb
4
5

Explanation 0

Initial String - aabbbabbab

  Queries
  Updated String
  Output

  R 1 5
  bbbaaabbab
  
  W 3 8
  
  baaabb

  C 4 4 a
  bbbaaabbab
  
  H 2 1 9
  
  4

  S 5 9 10 10
  bbbabaabba
  
  H 1 2 9
  
  5
