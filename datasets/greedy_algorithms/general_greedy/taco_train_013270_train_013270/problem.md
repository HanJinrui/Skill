You are given a permutation P of length N. You can perform the following operation on P:
Choose any i and j such that i < j and P_{i} < P_{j}, and remove exactly one of them from the array. After removing, the remaining parts of the array are concatenated.

Find out if it is possible to apply the given operation any number of times such that only one element remains in the array.

Note: A permutation of length N is an array where every element from 1 to N occurs exactly once.

------ Input Format ------ 

- The first line contains T - the number of test cases. Then the test cases follow.
- The first line of each test case contains N - the length of the permutation P.
- The second line of each test case contains N space-separated integers P_{1}, P_{2}, \dots, P_{N} - elements of the permutation.

------ Output Format ------ 

For each test case, output YES if it is possible to reduce the array to a single element using the given operation. Otherwise, output NO.

You may print each character of the string in uppercase or lowercase (for example, the strings yEs, yes, Yes and YES will all be treated as identical).

------ Constraints ------ 

$1 ≤T ≤3 \cdot 10^{5}$
$1 ≤N ≤3 \cdot 10^{5}$
$1 ≤P_{i} ≤N$
$P_{1}, P_{2}, \dots, P_{N}$ form a permutation of length $N$
$\sum N$ over all test cases is at most $3 \cdot 10^{5}$

----- Sample Input 1 ------ 
3
4
3 1 2 4
3
2 3 1
6
5 2 3 6 1 4

----- Sample Output 1 ------ 
YES
NO
YES

----- explanation 1 ------ 
- Test case $1$: We can apply operations as follows (the bolded elements are the pair chosen for that operation): $
[\textbf{3}, \text{1}, \text{2}, \textbf{4}] \rightarrow
[\textbf{1}, \text{2}, \textbf{4}] \rightarrow
[\textbf{2}, \textbf{4}] \rightarrow
[\text{4}]- Test case $2$: It can be shown that it is not possible to remove all elements except one element from the array.
- Test case $3$: We can apply operations as follows: $
[\textbf{5}, \text{2}, \text{3}, \textbf{6}, \text{1}, \text{4}] \rightarrow
[\text{2}, \textbf{3}, \textbf{6}, \text{1}, \text{4}] \rightarrow
[\textbf{2}, \text{3}, \text{1}, \textbf{4}] \rightarrow
[\textbf{3}, \text{1}, \textbf{4}] \rightarrow
[\textbf{1}, \textbf{4}] \rightarrow
[\text{4}]
