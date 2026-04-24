Let $F(a,d)$ denote an arithmetic progression (AP) with first term $\boldsymbol{\alpha}$ and common difference $\boldsymbol{d}$, i.e. $F(a,d)$ denotes an infinite $AP=>a,a+d,a+2d,a+3d,...$. You are given $n$ APs => $F(a_1,d_1),F(a_2,d_2),F(a_3,d_3),...F(a_n,d_n)$. Let $G(a_1,a_2,\cdots a_n,d_1,d_2,\cdots d_n)$ denote the sequence obtained by multiplying these APs.

Multiplication of two sequences is defined as follows. Let the terms of the first sequence be $A_1,A_2,\cdots A_m$, and terms of the second sequence be $B_1,B_2,\cdots B_m$. The sequence obtained by multiplying these two sequences is 

$A_1\times B_1,A_2\times B_2\text{,}\cdots A_m\times B_m$ 

If $A_1,A_2,\cdots A_m$ are the terms of a sequence, then the terms of the first difference of this sequence are given by $A_1',A_2',\ldots,A_{m-1}'$ calculated as $A_2-A_1,A_3-A_2,\text{}\cdots A_m-A_{(m-1)}$ respectively. Similarly, the second difference is given by $A'_2-A'_1,A'_3-A'_2,A'_{m-1}-A'_{m-2}$, and so on.

We say that the $k^{th}$ difference of a sequence is a constant if all the terms of the $k^{th}$ difference are equal.  

Let $F'(a,d,p)$ be a sequence defined as => $a^p,(a+d)^p,(a+2d)^p,\cdots$ 

Similarly, $G'(a_1,a_2,\cdots a_n,d_1,d_2,\cdots d_n,p_1,p_2,\cdots p_n)$ is defined as => product of $F'(a_1,d_1,p_1),F'(a_2,d_2,p_2),\cdots,F'(a_n,d_n,p_n)$. 

Task: 

Can you find the smallest $\boldsymbol{\mbox{k}}$ for which the $k^{th}$ difference of the sequence $G$ is a constant? You are also required to find this constant value.  

You will be given many operations. Each operation is of one of the two forms:  

1) 0 i j => 0 indicates a query $(1\leq i\leq j\leq n)$. You are required to find the smallest $\boldsymbol{\mbox{k}}$ for which the $k^{th}$ difference of $G'(a_i,a_{i+1},...a_j,d_i,d_{i+1},...d_j,p_i,p_{i+1},...p_j)$ is a constant. You should also output this constant value.  

2) 1 i j v => 1 indicates an update $(1\leq i\leq j\leq n)$. For all $i\leq k\leq j$, we update $p_k=p_k+v$.  

Input Format 

The first line of input contains a single integer $n$, denoting the number of APs. 

Each of the next $n$ lines consists of three integers $a_i,d_i,p_i$ $(1\leq i\leq n)$. 

The next line consists of a single integer $\textit{q}$, denoting the number of operations. Each of the next $\textit{q}$ lines consist of one of the two operations mentioned above.   

Output Format 

For each query, output a single line containing two space-separated integers $\mbox{K}$ and $\mbox{V}$. $\mbox{K}$ is the smallest value for which the $K^{\mbox{th}}$ difference of the required sequence is a constant. $\mbox{V}$ is the value of this constant. Since $\mbox{V}$ might be large, output the value of $\mbox{V}$ modulo 1000003.  

Note: $\mbox{K}$ will always be such that it fits into a signed 64-bit integer. All indices for query and update are 1-based. Do not take modulo 1000003 for $\mbox{K}$.

Constraints 

$1\leq n\leq10^5$ 

$1\leq a_i,d_i,p_i\leq10^4$ 

$1\leq q\leq10^5$ 

For updates of the form 1 i j v, $1\leq v\leq10^4$ 

Sample Input  

2  
1 2 1  
5 3 1  
3  
0 1 2  
1 1 1 1  
0 1 1  

Sample Output  

2 12  
2 8  

Explanation

The first sequence given in the input is => $1,3,5,7,9,\ldots$ 

The second sequence given in the input is => $5,8,11,14,17,\ldots$  

For the first query operation, we have to consider the product of these two sequences: 

=> $1\times5,3\times8,5\times11,7\times14,9\times17,\ldots$ 

=> $5,24,55,98,153,\ldots$

First difference is => $19,31,43,55,\ldots$ 

Second difference is => $12,12,12,\ldots$ This is a constant and hence the output is 2 12.  

After the update operation 1 1 1 1, the first sequence becomes => $1^2,3^2,5^2,7^2,9^2,\ldots$ 

i.e => $1,9,25,49,81,\ldots$ 

For the second query, we consider only the first sequence => $1,9,25,49,81,\ldots$ 

First difference is => $8,16,24,32,\ldots$ 

Second difference is => $8,8,8,\ldots$ This is a constant and hence the output is 2 8
