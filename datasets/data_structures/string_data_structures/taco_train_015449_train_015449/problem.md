Chef has two strings A and B consisting of lowercase alphabets, each of length N. Help Chef in finding the number of indices i (1 ≤ i ≤ N) such that A[i \dots N] < B[i \dots N].

S[i \dots N] denotes the suffix of string S starting at index i, i.e. S_{iS}_{i+1} \dots S_{N}. 
String S < String T denotes that S is lexicographically smaller than T. If two strings S and T have the same length N, we say that S is lexicographically smaller than T if there exists an index i(1 ≤ i ≤ N) such that S_{1} = T_{1}, S_{2} = T_{2}, \ldots, S_{i-1} = T_{i-1} and S_{i} < T_{i}. For example, "abc" is lexicographically smaller than "acd", "abe", but not smaller than "abc", "aac".

------ Input Format ------ 

- The first line contains T denoting the number of test cases. Then the test cases follow.
- The first line of each test case contains N, denoting the length of the strings A and B.
- The second line of each test case contains the string A.
- The third line of each test case contains the string B.

------ Output Format ------ 

For each test case, print a single line containing one integer -  the number of indices i such that A[i \dots N] < B[i\dots N].

------ Constraints ------ 

$1 ≤ T ≤ 10^{5}$
$1 ≤ N ≤ 10^{6}$
- The sum of $N$ over all test cases does not exceed $10^{6}$

----- Sample Input 1 ------ 
2
2
ab
bb
3
aaa
aab
----- Sample Output 1 ------ 
1
3

----- explanation 1 ------ 
Test Case $1$: 
- For $i = 1$, $A[1 \dots 2] = $ "$ab$", $B[1 \dots 2] = $ "$bb$" and lexicographically, "$ab$" $<$ "$bb$".
- For $i = 2$, $A[2 \dots 2] =$ "$b$", $B[2 \dots 2] = $ "$b$" and lexicographically, "$b$" $=$ "$b$".

Test Case $2$: For each $i \in \{1 , 2, 3\}$, $A[i \dots 3] < B[i \dots 3]$.
