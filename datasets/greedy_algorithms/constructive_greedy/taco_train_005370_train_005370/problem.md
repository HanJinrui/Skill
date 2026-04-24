Chef has a binary string S of length N. Chef wants to find two substrings of equal length, such that their [bitwise XOR] is maximised.

Formally, Chef wants to find L_{1}, R_{1}, L_{2}, and R_{2} such that:
1 ≤ L_{1} ≤ R_{1} ≤ N and 1 ≤ L_{2} ≤ R_{2} ≤ N
|R_{1} - L_{1} + 1| = |R_{2} - L_{2} + 1|, that is, the substrings have equal length;
S_{L_{1} \dots R_{1}} \oplus S_{L_{2} \dots R_{2}} is maximised, where \oplus is the bitwise XOR operation.

Output the maximum XOR value in decimal notation. Since the value can be large, output it module 10^{9}+7.

Note that a substring is formed by deleting some (possibly zero) characters from the beginning and some (possibly zero) characters from the end of the string.

------ Input Format ------ 

- The first line of input will contain a single integer T, denoting the number of test cases.
- Each test case consists of multiple lines of input.
- The first line of each test case contains a single integer N denoting the length of string S.
- The second line of each test case contains a binary string S of length N containing 0s and 1s only.

------ Output Format ------ 

For each test case, output the maximum XOR value in decimal notation. Since the value can be large, output it module 10^{9}+7.

------ Constraints ------ 

$1 ≤ T ≤ 10^{5}$
$2 ≤ N ≤ 2 \cdot 10^{6}$
$S$ contains $0$ and $1$ only.
- The sum of $N$ over all test cases won't exceed $2 \cdot 10^{6}$.

----- Sample Input 1 ------ 
3
4
1010
5
11111
3
011

----- Sample Output 1 ------ 
7
0
2

----- explanation 1 ------ 
Test case $1$: We can choose $L_{1} = 1, R_{1} = 3, L_{2} = 2,$ and $R_{2} = 4$. Thus, the chosen substrings are $101$ and $010$. The XOR of these substrings is $111$ whose decimal equivalent is $7$.

Test case $2$: We can choose $L_{1} = 2, R_{1} = 2, L_{2} = 4,$ and $R_{2} = 4$. Thus, the chosen substrings are $1$ and $1$. The XOR of these substrings is $0$ whose decimal equivalent is $0$.

Test case $3$: We can choose $L_{1} = 1, R_{1} = 2, L_{2} = 2,$ and $R_{2} = 3$. Thus, the chosen substrings are $01$ and $11$. The XOR of these substrings is $10$ whose decimal equivalent is $2$.
