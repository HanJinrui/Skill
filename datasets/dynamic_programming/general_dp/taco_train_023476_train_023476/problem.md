Alex has two arrays defined as $A=[a_0,a_1,...,a_{n-1}]$ and $B=[b_0,b_1,\ldots,b_{m-1}]$. He created an $n\times m$ matrix, $\mbox{M}$, where $M_{i,j}=gcd(a_i,b_j)$ for each $i,j$ in $\mbox{M}$. Recall that ${gcd}(a,b)$ is the greatest common divisor of $a$ and $\boldsymbol{b}$. 

For example, if $A=[2,3]$ and $B=[5,6]$, he builds $M=[[1,2],[1,3]]$ like so:
  $\begin{array}{|l|c|c|}
(i, j) & 0 & 1 \\
 0 & gcd(2,5)=1 &gcd(2,6)=2 \\
 1 & gcd(3,5)=1 &gcd(3,6)=3 
\end{array}$

Alex's friend Kiara loves matrices, so he gives her $\textit{q}$ questions about matrix $\mbox{M}$ where each question is in the form of some submatrix of $\mbox{M}$ with its upper-left corner at $M_{r_1,c_1}$ and its bottom-right corner at $M_{r_2,c_2}$. For each question, find and print the number of distinct integers in the given submatrix on a new line.

Input Format

The first line contains three space-separated integers describing the respective values of $n$ (the size of array $\mbox{A}$), $m$ (the size of array $\mbox{B}$), and $\textit{q}$ (Alex's number of questions). 

The second line contains $n$ space-separated integers describing $a_0,a_1,\ldots,a_{n-1}$. 

The third line contains $m$ space-separated integers describing $b_0,b_1,\ldots,b_{m-1}$. 

Each line $\boldsymbol{i}$ of the $\textit{q}$ subsequent lines contains four space-separated integers describing the respective values of $r_1$, $\mathbf{c}_{1}$, $r_2$, and $c_2$ for the $i^{\mbox{th}}$ question (i.e., defining a submatrix with upper-left corner $(r_1,c_1)$ and bottom-right corner $(r_2,c_2)$).

Constraints

$1\leq n,m\leq10^5$  
$1\leq a_i,b_i\leq10^5$  
$1\leq q\leq10$  
$0\leq r_{1},r_{2}<n$  
$0\leq c_1,c_2\lt m$  

Scoring  

$1\leq n,m\leq1000$ for $25\%$ of score.  
$1\leq n,m\leq10^5$ for $\textbf{100\%}$ of score.  

Output Format

For each of Alex's questions, print the number of distinct integers in the given submatrix on a new line.

Sample Input 0
3 3 3
1 2 3
2 4 6
0 0 1 1
0 0 2 2
1 1 2 2

Sample Output 0
2
3
3

Explanation 0

Given $A=[1,2,3]$ and $B=[2,4,6]$, we build the following $\mbox{M}$:

  $\begin{array}{|l|c|c|c|}
(i, j) & 0 & 1 & 2 \\
 0 & gcd(1,2)=1 &gcd(1,4)=1 &gcd(1,6)=1 \\
 1 & gcd(2,2)=2 &gcd(2,4)=2 &gcd(2,6)=2 \\
 2 & gcd(3,2)=1 &gcd(3,4)=1 &gcd(3,6)=3 
\end{array}$

The diagram below depicts the submatrices for each of the $q=3$ questions in green:

For the submatrix between $M_{0,0}$ and $M_{1,1}$, the set of integers is $\{1,2\}$. The number of distinct integers is $2$.
For the submatrix between $M_{0,0}$ and $M_{2,2}$, the set of integers is $\{1,2,3\}$. The number of distinct integers is $3$.
For the submatrix between $M_{1,1}$ and $M_{2,2}$, the set of integers is $\{1,2,3\}$. The number of distinct integers is $3$.
