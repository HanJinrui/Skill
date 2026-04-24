An XOR operation on a list is defined here as the xor ($\oplus$) of all its elements (e.g.: $XOR(\{A,B,C\})=A\oplus B\oplus C$). 

The $\textit{XorSum}$ of set $\textbf{arr}$ is defined here as the sum of the $XOR$s of all non-empty subsets of $\textbf{arr}$ known as $ar r'$. The set $ar r'$ can be expressed as:

$\textit{Xor}\textit{Sum}(ar\textbf{r})=\sum\limits_{i=1}^{2^n-1}XOR(ar\textbf{r}_i^{\prime})=XOR(ar\textbf{r}_1^{\prime})+XOR(ar\textbf{r}_2^{\prime})+\cdots+XOR(ar\textbf{r}_{2^n-2}^{\prime})+XOB(ar\textbf{r}_{2^n-1}^{\prime})$     

For example: Given set $arr=\{n_1,n_2,n_3\}$

The set of possible non-empty subsets is: $ar r'=\{\{n_1\},\{n_2\},\{n_3\},\{n_1,n_2\},\{n_1,n_3\},\{n_2,n_3\},\{n_1,n_2,n_3\}\}$     

The $\textit{XorSum}$ of these non-empty subsets is then calculated as follows: 

$\textit{XorSum(arr)}$ = $n_1+n_2+n_3+(n_1\oplus n_2)+(n_1\oplus n_3)+(n_2\oplus n_3)+(n_1\oplus n_2\oplus n_3)$

Given a list of $n$ space-separated integers, determine and print $XorSum\%(10^9+7)$.    

For example, $arr=\{3,4\}$.  There are three possible subsets, $ar r'=\{\{3\},\{4\},\{3,4\}\}$.  The XOR of $ar r'[1]=3$, of $ar r'[2]=4$ and of $ar r[3]=3\oplus4=7$.  The XorSum is the sum of these: $3+4+7=14$ and $14\%(10^9+7)=14$.  

Note: The cardinality of powerset$\left(n\right)$ is $2^{n}$, so the set of non-empty subsets of set $\textbf{arr}$ of size $n$ contains $2^n-1$ subsets.

Function Description  

Complete the xoringNinja function in the editor below.  It should return an integer that represents the XorSum of the input array, modulo $(10^9+7)$.  

xoringNinja has the following parameter(s):  

arr: an integer array

Input Format

The first line contains an integer $\mathbf{T}$, the number of test cases.       

Each test case consists of two lines: 

-  The first line contains an integer $n$, the size of the set $\textbf{arr}$. 

-  The second line contains $n$ space-separated integers $arr\left[i\right]$.  

Constraints

$1\leq T\leq5$ 

$1\leq n\leq10^5$ 

$0\leq\textit{arr}[i]\leq10^9,\ 1\leq i\leq n$  

Output Format

For each test case, print its $XorSum\%(10^9+7)$ on a new line.  The $i^{\mbox{th}}$ line should contain the output for the $i^{\mbox{th}}$ test case.

Sample Input 0
1
3
1 2 3

Sample Output 0
12

Explanation 0

The input set, $S=\{1,2,3\}$, has $7$ possible non-empty subsets: $S'=\{\{1\},\{2\},\{3\},\{1,2\},\{2,3\},\{1,3\},\{1,2,3\}\}$.

We then determine the $XOR$ of each subset in $S^{\prime}$: 

$XOR(\{1\})=1$ 

$XOR(\{2\})=2$ 

$XOR(\{3\})=3$ 

$XOR(\{1,2\})=1\oplus2=3$ 

$XOR(\{2,3\})=2\oplus3=1$ 

$XOR(\{1,3\}=1\oplus3=2$ 

$XOR(\text{{1,2,3}}=1\oplus2\oplus3=0$  

Then sum the results of the $XOR$ of each individual subset in $S^{\prime}$, resulting in $\textit{XorSum}=12$ and $12\%(10^9+7)=12$.

Sample Input 1
2
4
1 2 4 8
5
1 2 3 5 100

Sample Output 1
120
1648
