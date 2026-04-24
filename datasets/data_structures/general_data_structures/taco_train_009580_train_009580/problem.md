You are given a sequence $a_1,a_2,\ldots,a_n$. The task is to perform the following queries on it:

Type 1. Given two integers $\boldsymbol{l}$ and $\textbf{r}$ $(1\leq l\lt r\leq n;r-l+1\ is even)$. Reorder the elements of the sequence in such a way (changed part of the sequence is in brackets):
$a_1,a_2,\ldots,a_n\rightarrow a_1,a_2,\ldots,a_{l-2},a_{l-1},\left[a_{l+1},a_l,a_{l+3},a_{l+2},\ldots,a_{r},a_{r-1}\right],a_{r+1},a_{r+2},\ldots,a_{n}$
That is swap the first two elements of segment $[l,r]$, the second two elements, and so on.

Type 2. Given two integers $\boldsymbol{l}$ and $\textbf{r}$, print the value of sum $\sum\limits_{i=l}^{r}a_{i}$.

Input Format  

The first line contains two integers $n$ and $\textit{q}$. The second line contains $n$ integers $a_1,a_2,\ldots,a_n$, denoting initial sequence.

Each of the next $\textit{q}$ lines contains three integers $tp_i,l_i,r_i$, where $t p_i$ denotes the type of the query, and $l_i,r_i$ are parameters of the query. It's guaranteed that for a first-type query $(r-l+1)$ will be even.  

Constraints 

$2\leq n\leq2\times10^5$ 

$1\leq q\leq2\times10^5$ 

$1\leq a_i\leq10^6$ 

$1\leq t p_i\leq2$ 

$1\leq l_i\leq r_i\leq n$

Output Format

For each query of the second type print the required sum.

Sample Input

6 4
1 2 3 4 5 6
1 2 5
2 2 3
2 3 4
2 4 5

Example Output

5
7
9

Explanation

After the first query the sequence becomes [1, 3, 2, 5, 4, 6].
