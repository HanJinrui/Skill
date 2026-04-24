We define f(x)=\begin{cases} f(x \oplus  reverse(x))+1 & \text{if }  x \neq 0 \\ 0 & \text{otherwise} \end{cases}

Here, \oplus denotes the [bitwise XOR operation] and reverse is a function that takes a postive integer, reverses its binary representation (without any leading zeros) and returns the resulting number. For example reverse(2)=1, reverse(6)=3, reverse(7)=7

Given an integer N, find out the value of \sum^{2^{N}-1}_{i=1}  f(i) modulo 998244353 or claim that there exists a positive integer x < 2^{N} for which f is undefined.

------ Input Format ------ 

- The first line of input contains a single integer T - the number of test cases. The description of T test cases follows.
- The first and only line of each test case contains a single integer N.

------ Output Format ------ 

- For each test case output a single line containing one integer :
- -1 if there exists a positive integer x such that x < 2^{N} and f(x) is undefined   
- \sum^{2^{N}-1}_{i=1}  f(i) modulo 998244353 otherwise

------ Constraints ------ 

$1 ≤ T ≤ 3 \cdot 10^{5}$
$1 ≤ N ≤ 10^{9}$

----- Sample Input 1 ------ 
8
1
2
3
5
8
13
21
34

----- Sample Output 1 ------ 
1
4
10
58
578
20098
5236738
24641495

----- explanation 1 ------ 
Note that: 

- $f(1) = f(1 \oplus 1) + 1 = f(0) + 1 = 1$
- $f(2) = f(2 \oplus 1) + 1 = f(3) + 1 = (f(3 \oplus 3) + 1) + 1 = (f(0) + 1) + 1 = 2$
- $f(3) = f(3 \oplus 3) + 1 = f(0) + 1 = 1$

- Test case-1: $\sum^{2^{1}-1}_{i=1}  f(i) = f(1) = 1$. So answer is $1 \text{ mod } 998244353 = 1$.
- Test case-2: $\sum^{2^{2}-1}_{i=1}  f(i) = f(1) + f(2) + f(3) = 1 + 2 + 1 = 4$. So answer is $4 \text{ mod } 998244353 = 4$.
