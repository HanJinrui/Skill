You are given a string S of length N, which consists of digits from 0 to 9. You can apply the following operation to the string:

Choose an integer L with 1≤ L ≤ N and apply S_{i} = (S_{i} + 1) \mod 10 for each 1 ≤ i ≤ L.

For example, if S=39590, then choosing L=3 and applying the operation yields the string S=\underline{406}90.

The prefix of string S of length l\;(1 ≤ l ≤ \mid S \mid ) is string S_{1} S_{2} \dots S_{l}. A prefix of length l is called good if S_{1}=0, S_{2}=0, \dots, S_{l}=0. Find the length of the longest good prefix that can be obtained in string S by applying the given operation maximum K times.

------ Input Format ------ 

- The first line of input contains an integer T, denoting the number of test cases. The T test cases then follow:
- The first line of each test case contains two space-separated integers N, K.
- The second line of each test case contains the string S.

------ Output Format ------ 

For each test case, output in a single line the length of the longest good prefix that can be obtained in string S by applying the given operation maximum K times.

------ Constraints ------ 

$1 ≤ T ≤ 10^{5}$
$1 ≤ N ≤ 10^{5}$
$0 ≤ K ≤ 10^{9}$
$\mid S \mid = N$
$S$ contains digits from $0$ to $9$
- Sum of $N$ over all test cases does not exceed $3 \cdot 10^{5}$.

------ subtasks ------ 

Subtask 1 (100 points): Original constraints

----- Sample Input 1 ------ 
6
3 5
380
3 9
380
4 2
0123
5 13
78712
6 10
051827
8 25
37159725

----- Sample Output 1 ------ 
0
3
1
3
2
5

----- explanation 1 ------ 
Test case $1$: There is no way to obtain zeros on the prefix of the string $S = 380$ by applying the given operation maximum $5$ times.

Test case $2$: The optimal strategy is: choose $L = 2$ and apply the operation twice, resulting in $S=500$, then choose $L = 1$ and apply the operation $5$ times, resulting in $S=000$.

Test case $4$: One of the possible sequence of operations is the following:
- Choose $L = 5$ and apply the operation thrice, resulting in $S=01045$.
- Choose $L = 2$ and apply the operation $9$ times, resulting in $S=90045$. 
- Choose $L = 1$ and apply the operation once, resulting in $S=00045$.
