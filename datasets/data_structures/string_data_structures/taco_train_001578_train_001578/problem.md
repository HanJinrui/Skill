You are given a binary string S of length N (i.e. every character of S is either 0 or 1).

You can perform the following operation on S:
select any two indices i, j of the same parity, i.e. either both i, j are odd or both i, j are even
swap S_{i} and S_{j}

For example, in the string 1110, we can swap the second and the fourth characters to get 1011. However, we can never obtain 1101 from 1110 by performing such swaps.

Find the maximum possible number of occurrences of the string 01 as a [substring] of S after performing the above operation any number of times (it is also allowed to not perform any operation).

For example, the string 1110 has no occurrence of the string 01 as a substring, whereas we can swap the second and fourth characters to obtain 1{\color{red}{01}}1 which has exactly one occurrence of 01 (colored red).

------ Input Format ------ 

- The first line of input contains an integer T, denoting the number of testcases. The description of the T testcases follow.
- Each testcase consists of two lines.
- The first line contains a single integer N, the length of the string S.
- The second line contains a binary string of length N.

------ Output Format ------ 

- For each testcase, print in a single line, an integer — the answer as per the problem statement.

------ Constraints ------ 

$1 ≤ T ≤ 4000$
$1 ≤ |S| ≤ 10^{5}$
- The sum of $|S|$ over all testcases doesn't exceed $10^{5}$

------ subtasks ------ 

Subtask #1 (100 points): Original constraints

----- Sample Input 1 ------ 
3
5
00100
5
01010
5
10001
----- Sample Output 1 ------ 
1
2
2
----- explanation 1 ------ 
Test case $1$: The only strings that can be obtained by performing the given operations are $\{10000, 00100, 00001\}$. Of these the two strings $0{\color{red}{01}}00$ and $000{\color{red}{01}}$ contain exactly one occurrence of $01$.

Test case $2$: The given string $S$ cannot be changed by performing the given operation and contains $2$ occurrences of the string $01$, i.e. ${\color{red}01}{\color{blue}01}0$.

Test case $3$: The only strings that can be obtained by performing the given operations are $\{00101, 10001, 10100\}$. The string $0{\color{red}{01}}{\color{blue}{01}}$ contains two occurrences of $01$.
