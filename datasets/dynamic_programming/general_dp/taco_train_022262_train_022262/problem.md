Samantha and Sam are playing a numbers game.  Given a number as a string, no leading zeros, determine the sum of all integer values of substrings of the string.   

Given an integer as a string, sum all of its substrings cast as integers.  As the number may become large, return the value modulo $10^9+7$.  

Example 

$n=\text{'}42\text{'}$  

Here $n$ is a string that has $3$ integer substrings: $\begin{array}{c}A\end{array}$, $2$, and $\textbf{42}$.  Their sum is $48$, and $48\ \text{modulo}\ (10^9+7)=48$.

Function Description

Complete the substrings function in the editor below.   

substrings has the following parameter(s):  

string n: the string representation of an integer   

Returns   

int: the sum of the integer values of all substrings in $n$, modulo $10^9+7$

Input Format

A single line containing an integer as a string, without leading zeros.  

Constraints

$1\leq ncastas an integer\leq2\times10^5$

Sample Input 0
16

Sample Output 0
23

Explanation 0

The substrings of 16 are 16, 1 and 6 which sum to 23.

Sample Input 1
123

Sample Output 1
164

Explanation 1

The substrings of 123 are 1, 2, 3, 12, 23, 123 which sum to 164.
