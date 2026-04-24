Let's define a function, $\mbox{f}$, on a string, $\boldsymbol{p}$, of length $\boldsymbol{l}$ as follows:

$f(p)=(p_1\cdot a^{l-1}+p_2\cdot a^{l-2}+\cdots+p_l\cdot a^0)\ \text{mod}\ m$

where $p_i$ denotes the ASCII value of the $i^{\mbox{th}}$ character in string $\boldsymbol{p}$, $a=1\textbf{0000}1$, and $m=10^9+7$. 

Nikita has a string, $\boldsymbol{\mathrm{~S~}}$, consisting of $n$ lowercase letters that she wants to perform $\textit{q}$ queries on. Each query consists of an integer, $\boldsymbol{\mbox{k}}$, and you have to find the value of $f(w_k)$ where $w_k$ is the $k^{th}$ alphabetically smallest palindromic substring of $\boldsymbol{\mathrm{~S~}}$. If $w_k$ doesn't exist, print $-1$ instead.

Input Format

The first line contains $2$ space-separated integers describing the respective values of $n$ (the length of string $\boldsymbol{\mathrm{~S~}}$) and $\textit{q}$ (the number of queries). 

The second line contains a single string denoting $\boldsymbol{\mathrm{~S~}}$. 

Each of the $\textit{q}$ subsequent lines contains a single integer denoting the value of $\boldsymbol{\mbox{k}}$ for a query. 

Constraints

$1\leq n,q\leq10^5$  
$1\leq k\leq\frac{n\cdot(n+1)}{2}$  
It is guaranteed that string $\boldsymbol{\mathrm{~S~}}$ consists of lowercase English alphabetic letters only (i.e., $\mbox{a}$ to $\textbf{Z}$).
$a=10^5+1$
$m=10^9+7$. 

Scoring

$1\leq n,q\leq10^3$ for $25\%$ of the test cases.
$1\leq n,q\leq10^5$ for $\textbf{100\%}$ of the test cases.

Output Format

For each query, print the value of function $f(w_k)$ where $w_k$ is the $k^{th}$ alphabetically smallest palindromic substring of $\boldsymbol{\mathrm{~S~}}$; if $w_k$ doesn't exist, print $-1$ instead.

Sample Input
5 7
abcba
1
2
3
4
6
7
8       

Sample Output
97
97
696207567
98
29493435
99
-1

Explanation

There are $7$ palindromic substrings of $\textbf{"abcba''}$. Let's list them in lexicographical order and find value of $w_k$:

$w_1=\textbf{”a''}$, $f(w_1)=97$  
$w_2=\textbf{“a''}$, $f(w_2)=97$  
$w_3=\textbf{"abcba"}$, $f(w_3)=696207567$  
$w_4=\textbf{“b''}$, $f(w_4)=98$  
$w_5=\textbf{“b''}$, $f(w_5)=98$  
$w_6=\textbf{"bcb''}$, $f(w_6)=29493435$  
$w_7=\textbf{“c''}$, $f(w_7)=99$  
$w_8=$ doesn't exist, so we print $-1$ for $k=8$.
