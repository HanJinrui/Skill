Transforming data into some other data is typical of a programming job. This problem is about a particular kind of transformation which we'll call the max transform.

Let $\mbox{A}$ be a zero-indexed array of integers. For $0\leq i\leq j<\text{length}(A)$, let $A_{i\ldots j}$ denote the subarray of $\mbox{A}$ from index $\boldsymbol{i}$ to index $j$, inclusive.

Let's define the max transform of $\mbox{A}$ as the array obtained by the following procedure:

Let $\mbox{B}$ be a list, initially empty.
For $\boldsymbol{\mbox{k}}$ from $0$ to $\text{length}(A)-1$:
For $\boldsymbol{i}$ from $0$ to $\text{length}(A)-k-1$:
Let $j=i+k$.  
Append $\text{max}(A_{i\ldots j})$ to the end of $\mbox{B}$.  
Return $\mbox{B}$.  

The returned array is defined as the max transform of $\mbox{A}$. We denote it by $S(A)$. 

Complete the function solve that takes an integer array $\mbox{A}$ as input.

Given an array $\mbox{A}$, find the sum of the elements of $S(S(A))$, i.e., the max transform of the max transform of $\mbox{A}$. Since the answer may be very large, only find it modulo $10^9+7$.  

Input Format

The first line of input contains a single integer $n$ denoting the length of $\mbox{A}$.  

The second line contains $n$ space-separated integers $A_0,A_1,\ldots,A_{n-1}$ denoting the elements of $\mbox{A}$.  

Constraints

$1\leq n\leq2\cdot10^5$  
$1\leq A_i\leq10^6$  

Subtasks  

For $33.33\%$ of the total score, $1\leq n\leq4000$  

Output Format

Print a single line containing a single integer denoting the answer.  

Sample Input 0
3
3 2 1

Sample Output 0
58

Explanation 0

In the sample case, we have:

$\begin{align}A&=[3,2,1]\\ S(A)&=[3,2,1,3,2,3]\\ S(S(A))&=[3,2,1,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1$

Therefore, the sum of the elements of $S(S(A))$ is $58$.
