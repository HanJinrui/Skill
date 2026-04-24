You are situated in an $n$ dimensional grid at position $\left(x[1],x[2],\ldots,x[n]\right)$. The dimensions of the grid are $(D[1],D[2],...D[n])$. In one step, you can walk one step ahead or behind in any one of the $n$ dimensions. This implies that there are always $2\times n$ possible moves if movements are unconstrained by grid boundaries. How many ways can you take $m$ steps without leaving the grid at any point? You leave the grid if at any point $x[i]$, either $x[i]\leq0$ or $x[i]>D[i]$.

For example, you start off in a 3 dimensional grid at position $x=[2,2,2]$.  The dimensions of the grid are $D=[3,3,3]$, so each of your axes will be numbered from $1$ to $3$.  If you want to move $m=1$ step, you can move to the following coordinates: $\{[1,2,2],[2,1,2],[2,2,1],[3,2,2],[2,3,2],[2,2,3]\}$.    

If we started at $x=[1,1,1]$ in the same grid, our new paths would lead to $\{[1,1,2],[1,2,1],[2,1,1]\}$.  Other moves are constrained by $x[i]\not\leq0$.

Function Description

Complete the gridWalking function in the editor below.  It should return an integer that represents the number of possible moves, modulo $(10^9+7)$.

gridWalking has the following parameter(s):

m: an integer that represents the number of steps  
x: an integer array where each $x[i]$ represents a coordinate in the $i^{\mbox{th}}$ dimension where $1\leq i\leq n$
D: an integer array where each $D[i]$ represents the upper limit of the axis in the $i^{\mbox{th}}$ dimension  

Input Format

The first line contains an integer $\boldsymbol{\boldsymbol{t}}$, the number of test cases.

Each of the next $\boldsymbol{\boldsymbol{t}}$ sets of lines is as follows:

The first line contains two space-separated integers, $n$ and $m$.  
The next line contains $n$ space-separated integers $x[i]$.  
The third line of each test contains $n$ space-separated integers $D[i]$.  

Constraints

$1\leq t\leq10$
$1\leq n\leq10$  
$1\leq m\leq300$  
$1\leq D[i]\leq100$  
$1\leq x[i]\leq D[i]$  

Output Format

Output one line for each test case. Since the answer can be really huge, output it modulo $10^9+7$.  

Sample Input
1
2 3
1 1
2 3

Sample Output
12

Explanation

We are starting from (1, 1) in a $2\times3$ 2-D grid, and need to count the number of possible paths with length equal to $3$. 

Here are the $12$ paths:

$(1,1)\rightarrow(1,2)\rightarrow(1,1)\rightarrow(1,2)$ 

$(1,1)\to(1,2)\to(1,1)\to(2,1)$ 

$(1,1)\rightarrow(1,2)\rightarrow(1,3)\rightarrow(1,2)$ 

$(1,1)\rightarrow(1,2)\rightarrow(1,3)\rightarrow(2,3)$ 

$(1,1)\rightarrow(1,2)\rightarrow(2,2)\rightarrow(1,2)$ 

$(1,1)\to(1,2)\to(2,2)\to(2,1)$ 

$(1,1)\rightarrow(1,2)\rightarrow(2,2)\rightarrow(2,3)$ 

$(1,1)\rightarrow(2,1)\rightarrow(1,1)\rightarrow(1,2)$ 

$(1,1)\rightarrow(2,1)\rightarrow(1,1)\rightarrow(2,1)$ 

$(1,1)\rightarrow(2,1)\rightarrow(2,2)\rightarrow(2,1)$ 

$(1,1)\rightarrow(2,1)\rightarrow(2,2)\rightarrow(1,2)$ 

$(1,1)\rightarrow(2,1)\rightarrow(2,2)\rightarrow(2,3)$  

$12\mod(10^9+7)=12$
