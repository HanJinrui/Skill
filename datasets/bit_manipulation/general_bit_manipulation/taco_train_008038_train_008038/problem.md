Given two integers, $\boldsymbol{l}$ and $\textbf{r}$, find the maximal value of $\boldsymbol{a}$ xor $\boldsymbol{b}$, written $a\oplus b$, where $\boldsymbol{a}$ and $\boldsymbol{b}$ satisfy the following condition:

$l\leq a\leq b\leq r$  

For example, if $l=11$ and $r=12$, then 

$\textbf{11}\oplus11=\textbf{0}$ 

$\textbf{11}\oplus12=7$ 

$12\oplus12=0$  

Our maximum value is $7$.  

Function Description

Complete the maximizingXor function in the editor below.  It must return an integer representing the maximum value calculated.  

maximizingXor has the following parameter(s):

l: an integer, the lower bound, inclusive  
r: an integer, the upper bound, inclusive  

Input Format

The first line contains the integer $\boldsymbol{l}$. 

The second line contains the integer $\textbf{r}$.    

Constraints

$1\leq l\leq r\leq10$^{3}  

Output Format

Return the maximal value of the xor operations for all permutations of the integers from $\boldsymbol{l}$ to $\textbf{r}$, inclusive.

Sample Input 0
10
15

Sample Output 0
7

Explanation 0

Here $l=10$ and $r=15$. Testing all pairs:   

$10\oplus10=0$ 

$10\oplus11=1$ 

$\textbf{10}\oplus12=\textbf{6}$ 

$\textbf{10}\oplus13=7$ 

$\textbf{10}\oplus\textbf{14}=4$ 

$10\oplus15=5$ 

$\textbf{11}\oplus11=\textbf{0}$ 

$\textbf{11}\oplus12=7$ 

$11\oplus13=6$ 

$11\oplus14=5$ 

$11\oplus15=4$ 

$12\oplus12=0$ 

$12\oplus13=1$ 

$\textbf{12}\oplus\textbf{14}=2$ 

$12\oplus15=3$ 

$13\oplus13=0$ 

$13\oplus14=3$ 

$13\oplus15=2$ 

$14\oplus14=0$ 

$14\oplus15=1$ 

$15\oplus15=0$  

Two pairs, (10, 13) and (11, 12) have the xor value 7, and this is maximal. 

Sample Input 1
11
100

Sample Output 1
127
