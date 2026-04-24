Nikita just came up with a new array game. The rules are as follows:

Initially, Nikita has an array of integers.

In each move, Nikita must partition the array into $2$ non-empty contiguous parts such that the sum of the elements in the left partition is equal to the sum of the elements in the right partition. If Nikita can make such a move, she gets $1$ point; otherwise, the game ends.

After each successful move, Nikita discards either the left partition or the right partition and continues playing by using the remaining partition as array $\textbf{arr}$.

Nikita loves this game and wants your help getting the best score possible. Given $\textbf{arr}$, can you find and print the maximum number of points she can score?

For example, Nikita starts with the array $arr=[1,2,3,6]$.  She first splits it into $a1=[1,2,3]$ and $a2=[6]$, then discards $a2$.  $arr=a1\rightarrow a1=[1,2],a2=[3]$.  Discard $a2$ leaving $arr=[1,2]$.  This cannot be further split, so Nikita scored $2$.   

Function Description  

Complete the arraySplitting function in the editor below.  It should return an integer that reperesents the number of times Nikita can split the array.  

arraySplitting has the following parameter(s):  

arr: an array of integers  

Input Format

The first line contains an integer $\boldsymbol{\boldsymbol{t}}$, the number of test cases. 

Each of the next $\boldsymbol{\boldsymbol{t}}$ pairs of lines is as follows:  

The first line contains an integer $n$, the size of array $\textbf{arr}$.
The next line contains $n$ space-separated integers $arr\left[i\right]$.  

Constraints

$1\leq t\leq10$
$1\leq n\leq2^{14}$
$0\leq ar r[i]\leq10^9$

Scoring     

$1\leq n\leq2^8$ for $30\%$ of the test data
$1\leq n\leq2^{11}$ for $\textbf{60\%}$ of the test data
$1\leq n\leq2^{14}$ for $\textbf{100\%}$ of the test data

Output Format

For each test case, print Nikita's maximum possible score on a new line.

Sample Input
3
3
3 3 3
4
2 2 2 2
7
4 1 0 1 1 0 1

Sample Output
0
2
3

Explanation

Test Case 0:  

Nikita cannot partition $\mbox{A}$ into $2$ parts having equal sums. Therefore, her maximum possible score is $0$ and we print $0$ on a new line.

Test Case 1:  

Initially, $\mbox{A}$ looks like this: 

She splits the array into $2$ partitions having equal sums, and then discards the left partition:   

She then splits the new array into $2$ partitions having equal sums, and then discards the left partition:      

At this point the array only has $1$ element and can no longer be partitioned, so the game ends. Because Nikita successfully split the array twice, she gets $2$ points and we print $2$ on a new line.

Test Case 2:

array		a1	a2
[4,1,0,1,1,0,1]	[4]	[1,0,1,1,0,1]
[1,0,1,1,0,1]	[1,0,1]	[1,0,1]
[1,0,1]		[1,0]	[1]

The answer is $3$.
