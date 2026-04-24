You are using at most A number of 1s and at most B number of 2s. How many different evaluation results are possible when they are formed in an expression containing only addition + sign and multiplication * sign are allowed?

Note that, multiplication takes precedence over addition.

For example, if A=2 and B=2, then we have the following expressions:

1, 1*1 = 1
2, 1*2, 1*1*2, 1+1 = 2
1+2, 1+1*2 = 3
2+2, 2*2, 1+1+2, 1*2*2, 1*1*2*2, 1*2+1*2, 1*1*2+2, 1*2+2 = 4
1+2+2, 1+1*2+2 = 5
1+1+2+2,  1+1+2*2 = 6

So there are 6 unique results that can be formed if A = 2 and B = 2. 

Input Format

The first line contains the number of test cases T, T testcases follow each in a newline. 

Each testcase contains 2 integers A and B separated by a single space.  

Constraints

1 <= T <= 10^{5} 

0<=A<=1000000000 

0<=B<=1000  

Output Format

Print the number of different evaluations modulo (%) (10^{9}+7.)

Sample Input
4
0 0
2 2
0 2
2 0

Sample Output
0
6
2
2

Explanation

When A = 0, B = 0, there are no expressions, hence 0. 
When A = 2, B = 2, as explained in the problem statement above, expressions leads to 6 possible solutions. 
When A = 0, B = 2, we have 2, 2+2 or 2*2, hence 2. 
When A = 2, B = 0, we have 1 or 1*1, 1+1 hence 2.
