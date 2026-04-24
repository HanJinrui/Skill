You have two binary strings A and B, both of length N. You have to merge both the binary strings to form a new binary string C of length 2 \cdot N. The relative order of characters in the original binary strings A and B should not change in the binary string C.

For example, if A = {\color{blue}01011} and B = {\color{red}10100}, one possible way to merge them to form C is: C = {\color{blue}0}{\color{red}1}{\color{red}0}{\color{blue}1}{\color{red}1}{\color{blue}0}{\color{blue}1}{\color{blue}1}{\color{red}0}{\color{red}0}.

Minimize the number of inversions in the merged binary string C.

As a reminder, a pair of indices (i, j) is an inversion for binary string C if and only if 1 ≤ i < j ≤ |C|, C_{i} = 1 and C_{j} = 0.

------ Input Format ------ 

- The first line of input contains a single integer T, denoting the number of test cases. The description of T test cases follows.
- The first line of each test case contains a single integer N — the length of the binary strings A and B.
- The second line of each test case contains the binary string A.
- The third line of each test case contains the binary string B.

------ Output Format ------ 

For each test case, output a single line containing the minimum number of inversions in the merged binary string C.

------ Constraints ------ 

$1 ≤ T ≤ 1000$
$1 ≤ N ≤ 1000$
- It is guaranteed that the sum of $N$ over all test cases does not exceed $2000$.
$|A| = |B| = N$
$A$ and $B$ are binary strings, i.e, contain only $0$ and $1$.

----- Sample Input 1 ------ 
3
4
1010
0101
5
10010
11001
5
00001
11110

----- Sample Output 1 ------ 
6
12
4

----- explanation 1 ------ 
Test Case $1$: $A = {\color{blue}1010}$ and $B = {\color{red}0101}$. One optimal $C$ is ${\color{red}0}{\color{blue}1}{\color{blue}0}{\color{red}1}{\color{red}0}{\color{blue}1}{\color{blue}0}{\color{red}1}$. The $6$ inversions in this $C$ are $\{(2, 3), (2, 5), (2, 7), (4, 5), (4, 7), (6, 7)\}$.

Test Case $2$: $A = {\color{blue}10010}$ and $B = {\color{red}11001}$. One optimal $C$ is ${\color{blue}1}{\color{blue}0}{\color{blue}0}{\color{red}1}{\color{red}1}{\color{red}0}{\color{red}0}{\color{blue}1}{\color{blue}0}{\color{red}1}$.

Test Case $3$: $A = {\color{blue}00001}$ and $B = {\color{red}11110}$. One optimal $C$ is ${\color{blue}0}{\color{blue}0}{\color{blue}0}{\color{blue}0}{\color{red}1}{\color{red}1}{\color{red}1}{\color{red}1}{\color{red}0}{\color{blue}1}$.
