In this challenge, you will be given an array $\mbox{B}$ and must determine an array $\mbox{A}$.  There is a special rule:  For all $\boldsymbol{i}$, $A[i]\leq B[i]$.  That is, $A[i]$ can be any number you choose such that $1\leq A[i]\leq B[i]$.  Your task is to select a series of $A[i]$ given $B[i]$ such that the sum of the absolute difference of consecutive pairs of $\mbox{A}$ is maximized.  This will be the array's cost, and will be represented by the variable $\mbox{S}$ below. 

The equation can be written:

$S=\sum_{i=2}^{N}|A[i]-A[i-1]|$

For example, if the array $B=[1,2,3]$, we know that $1\leq A[1]\leq1$, $1\leq A[2]\leq2$, and $1\leq A[3]\leq3$.  Arrays meeting those guidelines are:

[1,1,1], [1,1,2], [1,1,3]
[1,2,1], [1,2,2], [1,2,3]

Our calculations for the arrays are as follows:

|1-1| + |1-1| = 0	|1-1| + |2-1| = 1	|1-1| + |3-1| = 2
|2-1| + |1-2| = 2	|2-1| + |2-2| = 1	|2-1| + |3-2| = 2

The maximum value obtained is $2$.

Function Description

Complete the cost function in the editor below.  It should return the maximum value that can be obtained.  

cost has the following parameter(s):  

B: an array of integers  

Input Format

The first line contains the integer $\boldsymbol{\boldsymbol{t}}$, the number of test cases. 

Each of the next $\boldsymbol{\boldsymbol{t}}$ pairs of lines is a test case where: 

- The first line contains an integer $n$, the length of $\mbox{B}$ 

- The next line contains $n$ space-separated integers $B[i]$  

Constraints

$1\leq t\leq20$ 
$1<n\leq10^5$
$1\leq B[i]\leq100$

Output Format

For each test case, print the maximum sum on a separate line.   

Sample Input
1
5
10 1 10 1 10

Sample Output
36

Explanation

The maximum sum occurs when A[1]=A[3]=A[5]=10 and A[2]=A[4]=1.  That is $|1-10|+|10-1|+|1-10|+|10-1|=36$.
