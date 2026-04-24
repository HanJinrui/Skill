An array A is called *weird* if it can be sorted in non-decreasing order by applying the given operation any number of times:
Select any index i (1 ≤ i ≤ |A|) and set A_{i} := -A_{i}.

For example: A = [2, 1, 3] is *weird* since after applying the operation at i = 1, A becomes [-2, 1, 3] which is sorted.

JJ has a permutation P of length N. He wants to find the number of subarrays of P which are *weird*. Can you help him?

------ Input Format ------ 

- The first line contains a single integer T — the number of test cases. Then the test cases follow.
- The first line of each test case contains an integer N — the size of the permutation P.
- The second line of each test case contains N space-separated integers P_{1}, P_{2}, \dots, P_{N} denoting the permutation P.

------ Output Format ------ 

For each test case, output on a new line the number of *weird* subarrays of P.

------ Constraints ------ 

$1 ≤ T ≤ 10^{5}$
$1 ≤ N ≤ 10^{5}$
$P$ is a permutation.
- Sum of $N$ over all test cases does not exceed $2 \cdot 10^{5}$.

----- Sample Input 1 ------ 
3
3
2 3 1
3
2 1 3
4
1 2 3 4

----- Sample Output 1 ------ 
5
6
10

----- explanation 1 ------ 
Test Case 1: Weird subarrays of $P$ are: $[2], [3], [1], [2, 3], [3, 1]$.

Test Case 2: Weird subarrays of $P$ are: $[2], [1], [3], [2, 1], [1, 3], [2, 1, 3]$.
