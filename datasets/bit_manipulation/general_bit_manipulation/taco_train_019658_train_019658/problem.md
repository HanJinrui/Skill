You are given $n$ non-negative integers, $a_0,a_1,\ldots,a_{n-1}$. We define the score for some permutation ($\boldsymbol{p}$) of length $n$ to be the maximum of $a_{p_i}\oplus a_{p_{i+1}}$ for $0\leq i<n-1$. 

Find the permutation with the minimum possible score and print its score.

Note: $\oplus$ is the exclusive-OR (XOR) operator.

Input Format

The first line contains single integer, $n$, denoting the number of integers. 

The second line contains $n$ space-separated integers, $a_0,a_1,\ldots,a_{n-1}$, describing the respective integers.

Constraints

$2\leq n\leq3000$
$0\leq a_i\leq10^9$

Output Format

Print a single integer denoting the minimum possible score.

Sample Input 0

4
1 2 3 4

Sample Output 0

5

Sample Input 1

3
1 2 3

Sample Output 1

2

Explanation

Sample Case 0: 

The permutation with the minimum score is $(3,2,1,4)$: 

$a_0\oplus a_1=3\oplus2=1$ 

$a_1\oplus a_2=2\oplus1=3$ 

$a_2\oplus a_3=1\oplus4=5$      

Because the permutation's score is the maximum of these values, we print $5$ on a new line.

Sample Case 1: 

The permutation with the minimum score is $(1,3,2)$: 

$a_0\oplus a_1=1\oplus3=2$ 

$a_1\oplus a_2=3\oplus2=1$

Because the permutation's score is the maximum of these values, we print $2$ on a new line.
