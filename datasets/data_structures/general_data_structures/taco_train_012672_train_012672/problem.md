Given an array $\boldsymbol{A\left[\right]}$ of $N$ distinct elements. Let $M_1$ and $M_2$ be the smallest and the next smallest element in the interval $[L,R]$ where $1\leq L<R\leq N$.  

$S_i=(((M_1\wedge M_2)\oplus(M_1\vee M_2))\wedge(M_1\oplus M_2))$.  

where $\Lambda,V,\oplus$, are the bitwise operators $\textit{AND}$, $\mbox{OR}$ and $XOR$ respectively. 

Your task is to find the maximum possible value of $S_i$.

Input Format

First line contains integer $N$. 

Second line contains $N$ integers, representing elements of the array $\boldsymbol{A\left[\right]}$.  

Constraints 

$1<N\leq10^6$ 

$1\leq A_i\leq10^9$  

Output Format

Print the value of maximum possible value of $S_i$.   

Sample Input
5
9 6 3 5 2

Sample Output
15

Explanation

Consider the interval $[1,2]$ the result will be maximum. 

$(((9\land6)\oplus(9\lor\textbf{6}))\land(9\oplus\textbf{6}))=15$
