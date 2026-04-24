Jonas asked Martha to stand at point $(x_{1},y_{1})$ on an infinite cartesian plane. He gave her a string $S$ which consists of operations in the form of characters 'R', 'L', 'U', and 
'D'.

Each character of the string corresponds to the following movements: 

'R' means moving right by $1$ unit i.e, $(x,y)$ to $(x+1,y)$.
'L' means moving left by $1$ unit i.e, $(x,y)$ to $(x-1,y)$.
'U' means moving up by $1$ unit i.e, $(x,y)$ to $(x,y+1)$.
'D' means moving down by $1$ unit i.e, $(x,y)$ to $(x,y-1)$.

Now, Jonas asks Martha $Q$ queries. In each query, coordinates are given of form $(x_{2},y_{2})$. Martha needs to tell if it is possible to move from $(x_{1},y_{1})$ to $(x_{2},y_{2})$ by choosing a subsequence of given string $S$ and performing the operations in sequential order.Starting point $(x_{1},y_{1})$ remains same for all queries.

If it is possible, print "YES" and the length of the smallest possible subsequence of string, else print "NO".

Recall that string $a$ is a subsequence of a string $b$ if $a$ can be obtained from $b$ by deletion of several (possibly zero or all) characters. For example, for the string $a$="codechef", the following strings are subsequences: "code", "ee", "odchef", "df", "", and others, but the following are not subsequences: "ced", "eehc", "cofe".

Note: Use of Fast IO is recommended.

------ Input: ------

First line will contain $T$, number of test cases. Then test cases follow.
For each test case, first line will contain string $S$, string of operations.
Second line will contain coordinates $x_{1}$ and $y_{1}$.
Third line will contain $Q$, number of queries.
$Q$ lines follow. Each line will contain coordinates $x_{2}$ and $y_{2}$.

------ Output: ------
For each query if subsequence exists then print "YES" (without quotes) and length of smallest possible subsequence separated by a space in new line, else print "NO" (without quotes) in new line.

------ Constraints  ------
$1 ≤ T ≤ 10$
$1 ≤ |S| ≤ 10^{6}$
$-10^{8} ≤ x_{1},x_{2},y_{1},y_{2} ≤ 10^{8}$
$1 ≤ Q ≤ 10^{5}$

----- Sample Input 1 ------ 
1
RLUDRLUD
1 2
2
2 3
1 -2
----- Sample Output 1 ------ 
YES 2
NO
----- explanation 1 ------ 
Given String is "RLUDRLUD", $(x_{1},y_{1})$ is $(1,2)$. We can move from $(1,2)$ to $(2,3)$ in just two operations if we choose subsequence as "RU" or "UR".

Suppose we choose "RU" as a subsequence. 'R' means moving from $(1,2)$ to $(2,2)$. 'U' means moving from $(2,2)$ to $(2,3)$.

In the second query, we can't move from (1,2) to (1,-2) using operations of the given string.
