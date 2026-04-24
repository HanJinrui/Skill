At the time when Pythagoreanism was prevalent, people were also focused on different ways to factorize a number. In one class, Pythagoras asked his disciples to solve one such problem, Reverse Factorization. They were given a set of integer, $A=\{a_1,a_2,\cdots,a_K\}$, and an integer $N$. They need to find the a way to reach $N$, starting from $\mbox{1}$, and at each step multiplying current value by any element of $\mbox{A}$. But soon they realised that there may exist more than one way to reach $N$. So they decided to find a way in which number of states are least. All of sudden they started on this new problem. People solved it and then started shouting their answer. CRAP!!!. There still exists multiple answers. So finally after much consideration, they settled on the lexicographically smallest series among those solutions which contains the least number of states.

For example, if $N=12$ and $A=2,3,4$ then following ways exists  

(a) 1  ->  2  ->  4  ->  12
       x2     x2     x3

(b) 1  ->  4  ->  12
       x4     x3

(c) 1  ->  3  ->  12
       x3     x4

Here (a) is not the minimal state, as it has $\begin{array}{c}4\end{array}$ states in total. While (b) and (c) are contenders for answer, both having 3 states, (c) is lexicographically smaller than (b) so it is the answer. In this case you have to print 1 3 12. If there exists no way to reach $N$ print -1.   

Input Format

Input contains two lines where first line contains two space separated integer, $N$ and $\mbox{K}$, representing the final value to reach and the size of set $\mbox{A}$, respectively. Next line contains K space integers representing the set $A=\{a_1,a_2,\cdots,a_K\}$.

Constraints

$1\leq N\leq10^9$  
$1\leq K\leq20$  
$2\leq a_i\leq20$, where $i\in[1,K]$  
$a_i\neq a_j$, where $1\leq i,j\leq K$ AND $i\neq j$  

Note:  

Lexicographical order: If $list1=[p_1,p_2,\cdots,p_m]$ and $list2=[q_1,q_2,\cdots,q_n]$ are two ordered lists, then $list1$ is lexicographically smaller than $list2$ if any one of the following condition satisfies.  

$p_i=q_i,\forall i\in[1,m]$ AND $m<n$.  
$p_i=q_i,\forall i\in[1,k]$ AND $k<min(m,n)$ AND $p_{k+1}<q_{k+1}$.  

You need to find the lexigraphically smallest series among those solutions which contains the least number of states.  

Output Format

Print the steps to reach $N$ if it exists. Otherwise print -1.

Sample Input 0
12 3
2 3 4

Sample Output 0
1 3 12

Explanation 0

This is the same case which is explaned above.  

Sample Input 1
15 5
2 10 6 9 11

Sample Output 1
-1

Explanation 1

Here no way exists so that we can reach $15$ starting from $\mbox{1}$.  

Sample Input 2
72 9
2 4 6 9 3 7 16 10 5

Sample Output 2
1 2 8 72

Explanation 2

There are multiple ways to reach 72 using these 8 numbers. Out of which following 6 ways consists of minimal states (4).  

States          =>  Multiplication operation
 1   9  18  72  =>      (x9, x2, x4)
 1   4  36  72  =>      (x4, x9, x2)
 1   2   8  72  =>      (x2, x4, x9)
 1   2  18  72  =>      (x2, x9, x4)
 1   4   8  72  =>      (x4, x2, x9)
 1   9  36  72  =>      (x9, x4, x2)

As series 1 2 8 72 is lexicographically smallest, it is the answer.
