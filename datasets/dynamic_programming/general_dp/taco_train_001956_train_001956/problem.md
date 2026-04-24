Implement a modified Fibonacci sequence using the following definition:

Given terms $t\left[i\right]$ and $t[i+1]$ where $i\in(1,\infty)$, term $t[i+2]$ is computed as:
  $t_{i+2}=t_{i}+(t_{i+1})^{2}$      

Given three integers, $\mbox{t1}$, $\mbox{t2}$, and $n$, compute and print the $n^{th}$ term of a modified Fibonacci sequence.

Example 

$t1=0$ 

$t2=1$ 

$n=6$

$t3=0+1^2=1$  
$t4=1+1^2=2$  
$t5=1+2^2=5$  
$t6=2+5^2=27$  

Return $27$.  

Function Description  

Complete the fibonacciModified function in the editor below.  It must return the $n^{th}$ number in the sequence.  

fibonacciModified has the following parameter(s):  

int t1: an integer  
int t2: an integer  
int n: the iteration to report  

Returns  

int: the $n^{th}$ number in the sequence  

Note: The value of $t[n]$ may far exceed the range of a $\mbox{64}$-bit integer. Many submission languages have libraries that can handle such large results but, for those that don't (e.g., C++), you will need to compensate for the size of the result.  

Input Format

A single line of three space-separated integers, the values of $\mbox{t1}$, $\mbox{t2}$, and $n$.

Constraints

$0\leq t1,t2\leq2$
$3\leq n\leq20$  
$t_n$ may far exceed the range of a $\mbox{64}$-bit integer. 

Sample Input
0 1 5

Sample Output
5

Explanation

The first two terms of the sequence are $t1=0$ and $t2=1$, which gives us a modified Fibonacci sequence of $\{0,1,1,2,5,27,\ldots\}$.  The $5^{th}$ term is $5$.
