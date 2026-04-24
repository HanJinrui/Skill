Read problem statements in [Bengali], [Russian], [Mandarin] and [Vietnamese] as well.

You are given a binary string S. You can perform the following operations on S:

Flip: Pick an index i (1 ≤ i ≤ |S|) and flip the i-th character (i.e change 1 to 0 or 0 to 1). For e.g. 01\underline{1}001 \rightarrow 01\underline{0}001
Compress: Pick any non-empty substring consisting of the same character and replace it with a single occurrence of that character. For e.g. 100\underline{1111}10 \rightarrow 100\underline{1}10

You want to make all the characters of the binary string equal (i.e. either all characters are 0 or all characters are 1). Find the minimum number of operations required to do so.

------ Input Format ------ 

- The first line of input contains a single integer T, denoting the number of test cases. The description of T test cases follows.
- The first and only line of each test case contains a binary string S.

------ Output Format ------ 

For each test case, output a single line containing one integer - the minimum number of operations required to make all the characters of S equal.

------ Constraints ------ 

$1 ≤T ≤10^{5}$
$1 ≤|S| ≤10^{6}$
$S$ is a binary string.
- It is guaranteed that the sum of $|S|$ over all test cases does not exceed $10^{6}$.

------ subtasks ------ 

Subtask #1 (5 points):
$1 ≤ T ≤ 10^{3}$
$1 ≤ |S| ≤ 10$

Subtask #2 (20 points):
$1 ≤ T ≤ 10^{3}$
$1 ≤ |S| ≤ 50$

Subtask #3 (75 points):
Original constraints

----- Sample Input 1 ------ 
3
100011
1110011
000101110

----- Sample Output 1 ------ 
2
2
3

----- explanation 1 ------ 
In the first test case,

- $1\underline{000}11 \xrightarrow{\text{compress}} 1\underline{0}11$
- $1\underline{0}11 \xrightarrow{\text{flip}} 1\underline{1}11$

In the second test case,

- $111\underline{0}011 \xrightarrow{\text{flip}} 111\underline{1}011$
- $1111\underline{0}11 \xrightarrow{\text{flip}} 1111\underline{1}11$

In the third test case,

- $0001\underline{0}1110 \xrightarrow{\text{flip}} 0001\underline{1}1110$
- $000\underline{11111}0 \xrightarrow{\text{compress}} 000\underline{1}0$
- $000\underline{1}0 \xrightarrow{\text{flip}} 000\underline{0}0$
