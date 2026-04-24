Dragonado rarely gets stuck on a problem, unless of course, if it's a XOR Problem. 

Dragonado while coming back from the Fruit Market, finds an array A of N elements. He wants to find 4 integers, say i_{1},i_{2},i_{3} and i_{4}, such that:

\texttt{popcount}(A_{i_{1}} \oplus A_{i_{2}}) = \texttt{popcount}(A_{i_{3}} \oplus A_{i_{4}})
1 ≤ i_{1},i_{2},i_{3},i_{4} ≤ N  and   i_{1},i_{2},i_{3},i_{4}  are pairwise distinct. 

Here, \texttt{popcount}(x) denotes the number of set bits in the binary representation of x. Secondly, \oplus denotes the [bitwise XOR operation].

Can you help Dragonado find four integers i_{1}, i_{2}, i_{3} and i_{4} which satisfy the given conditions?

Output -1 if no answer exists.

If multiple answers exist, output any.

Note: The input of this problem is large, so use fast input/output methods.

------ Input Format ------ 

- The first line contains a single integer T - the number of test cases. Then the test cases follow.
- The first line of each test case contains an integer N - the size of the array A.
- The second line of each test case contains N space-separated integers A_{1}, A_{2}, \dots, A_{N} denoting the array A.

------ Output Format ------ 

For each test case, output i_{1},i_{2},i_{3},i_{4} which satisfy the given conditions. 

Output -1 if no numbers satisfying the conditions exist.

------ Constraints ------ 

$1 ≤ T ≤ 10^{4}$
$4 ≤ N ≤ 10^{5}$
$1 ≤ A_{i} ≤ 10^{9}$
- It is guaranteed that sum of $N$ over all test cases does not exceed $2 \cdot 10^{6}$

----- Sample Input 1 ------ 
2
4
1 2 5 6
4
1 2 3 4

----- Sample Output 1 ------ 
1 4 2 3
-1
----- explanation 1 ------ 
Test case-1: $1, 4, 2, 3$ is a valid answer because:

- $\texttt{popcount}(A_{1} \oplus A_{4}) = \texttt{popcount}(7) = 3$
- $\texttt{popcount}(A_{2} \oplus A_{3}) = \texttt{popcount}(7) = 3$

Therefore, $\texttt{popcount}(A_{i_{1}} \oplus A_{i_{2}}) = \texttt{popcount}(A_{i_{3}} \oplus A_{i_{4}})$

Test case-2: We can prove that no $i_{1}, i_{2}, i_{3}, i_{4}$ exist that satisfy the given conditions.
