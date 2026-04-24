Chef has two binary strings A and B, both having length N. He can perform the following operation on A any number of times (possibly zero):
Select any index i (1 ≤ i ≤ N - 1) and simultaneously set A_{i} := A_{i} \oplus A_{i + 1} and A_{i + 1} := A_{i} \oplus A_{i + 1}. Formally, if initially A_{i} = x and A_{i + 1} = y then set A_{i} := x \oplus y and A_{i + 1} := x \oplus y

Here, \oplus denotes the [bitwise XOR] operation.

Chef wants to determine if it is possible to make A equal to B by applying the above operation any number of times. Can you help Chef?

------ Input Format ------ 

- The first line contains a single integer T — the number of test cases. Then the test cases follow.
- The first line of each test case contains an integer N — the length of the binary string A.
- The second line of each test case contains the binary string A of length N.
- The third line of each test case contains the binary string B of length N.

------ Output Format ------ 

For each test case, output YES if Chef can make string A equal to string B by applying the above operation any number of times. Otherwise, output NO.

You may print each character of YES and NO in uppercase or lowercase (for example, yes, yEs, Yes will be considered identical).

------ Constraints ------ 

$1 ≤T ≤10^{5}$
$2 ≤N ≤10^{5}$
- The sum of $N$ over all test cases does not exceed $2 \cdot 10^{5}$

----- Sample Input 1 ------ 
3
2
00
10
3
010
000
4
0011
0100

----- Sample Output 1 ------ 
NO
YES
YES

----- explanation 1 ------ 
Test case $1$: It can be proven that we can not make $A$ equal to $B$ by using the given operation.

Test case $2$: We can apply the following operations: $0\underline{10} \rightarrow 0\underline{11} \rightarrow 000$.

Test case $3$: We can apply the following operations: $0\underline{01}1 \rightarrow 01\underline{11} \rightarrow 0100$.
