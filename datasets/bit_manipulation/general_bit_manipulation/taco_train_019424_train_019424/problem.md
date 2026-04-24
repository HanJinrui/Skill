Louise and Richard have developed a numbers game.  They pick a number and check to see if it is a power of $2$.  If it is, they divide it by $2$.  If not, they reduce it by the next lower number which is a power of $2$.  Whoever reduces the number to $1$ wins the game.  Louise always starts.

Given an initial value, determine who wins the game.

Example 

$n=132$   

It's Louise's turn first.  She determines that $132$ is not a power of $2$.  The next lower power of $2$ is $\textbf{128}$, so she subtracts that from $132$ and passes $4$ to Richard.  $4$ is a power of $2$, so Richard divides it by $2$ and passes $2$ to Louise.  Likewise, $2$ is a power so she divides it by $2$ and reaches $1$.  She wins the game.

Update If they initially set counter to $1$, Richard wins.  Louise cannot make a move so she loses.

Function Description  

Complete the counterGame function in the editor below.  

counterGame has the following parameter(s):  

int n: the initial game counter value  

Returns   

string: either Richard or Louise

Input Format

The first line contains an integer $\boldsymbol{\boldsymbol{t}}$, the number of testcases. 

Each of the next $\boldsymbol{\boldsymbol{t}}$ lines contains an integer $n$, the initial value for each game.  

Constraints

$1\leq t\leq10$
$1\leq n\leq2^{64}-1$

Sample Input 0
1
6

Sample Output 0
Richard

Explanation 0

$\boldsymbol{6}$ is not a power of $2$ so Louise reduces it by the largest power of $2$ less than $\boldsymbol{6}$:$6-4=2$.  
$2$ is a power of $2$ so Richard divides by $2$ to get $1$ and wins the game.
