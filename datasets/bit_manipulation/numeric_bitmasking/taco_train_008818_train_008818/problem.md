A permutation P of length N (1-based) is called good if it satisfies the following these conditions:
For each 1 ≤ i ≤ N, P_{i} \neq i
|P_{1} - 1| \oplus |P_{2} - 2| \oplus \ldots \oplus |P_{N} - N| = 0

Here, \oplus denotes the [bitwise XOR operation] and |X| denotes the absolute value of X.

Find any good permutation P of length N or print -1 if no such permutation exists.

Note: A permutation of length N is an array which contains every integer from 1 to N (inclusive) exactly once.

------ Input Format ------ 

- The first line contains a single integer T - the number of test cases. Then the test cases follow.
- The first and only line of each test case contains an integer N - the length of the permutation P.

------ Output Format ------ 

For each test case, print -1 if no such permutation exists. Otherwise, in a single line, output N space-separated integers - the required good permutation. If more than one solution exists, you may print any of them.

------ Constraints ------ 

$1 ≤ T ≤ 10^{6}$
$1 ≤ N ≤ 10^{6}$
- Sum of $N$ over all test cases does not exceed $10^{6}$

----- Sample Input 1 ------ 
3
1
2
8
----- Sample Output 1 ------ 
-1
2 1
7 1 5 6 3 4 8 2
----- explanation 1 ------ 
Test case 1: There is only one permutation $P = [1]$ of length $1$. Since $P_{1} = 1$ the answer does not exist.

Test case 2: Consider the permutation $P = [2, 1]$. Both conditions are satisfied.
* $P_{1} \neq 1$ and $P_{2} \neq 2$
* $|P_{1} - 1| \oplus |P_{2} - 2| = |2 - 1| \oplus |1 - 2| = 1 \oplus 1 = 0$

Test case 3: Both conditions are satisfied for $P = [7, 1, 5, 6, 3, 4, 8, 2]$.
