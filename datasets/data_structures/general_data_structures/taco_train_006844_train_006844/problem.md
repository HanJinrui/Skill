You are given two sets, $\mbox{A}$ and $\mbox{B}$. 

Your job is to find whether set $\mbox{A}$ is a subset of set $\mbox{B}$.
 
If set $\mbox{A}$ is subset of set $\mbox{B}$, print True.

If set $\mbox{A}$ is not a subset of set $\mbox{B}$, print False.

Input Format

The first line will contain the number of test cases, $\mathbf{T}$. 

The first line of each test case contains the number of elements in set $\mbox{A}$.

The second line of each test case contains the space separated elements of set $\mbox{A}$.

The third line of each test case contains the number of elements in set $\mbox{B}$.

The fourth line of each test case contains the space separated elements of set $\mbox{B}$.

Constraints

$\textbf{0}<T<21$ 
$0<\text{Number of elements in each set}<1001$

Output Format

Output True or False for each test case on separate lines.

Sample Input
3
5
1 2 3 5 6
9
9 8 5 6 3 2 1 4 7
1
2
5
3 6 5 4 1
7
1 2 3 5 6 8 9
3
9 8 2

Sample Output
True 
False
False

Explanation

Test Case 01 Explanation

Set $\mbox{A}$ = {1 2 3 5 6} 

Set $\mbox{B}$ = {9 8 5 6 3 2 1 4 7} 

All the elements of set $\mbox{A}$ are elements of set $\mbox{B}$. 

Hence, set $\mbox{A}$ is a subset of set $\mbox{B}$.
