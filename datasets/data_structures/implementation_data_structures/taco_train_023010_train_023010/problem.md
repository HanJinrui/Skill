Alice has an array A of length N which is initially a *permutation*. She dislikes K numbers which are B_{1}, B_{2}, \ldots, B_{K} all of which are distinct. Therefore, she removes all the occurrences of these numbers from A. The order of the remaining elements of the A does not change. 

Can you find out the resulting array A?

Note: A *permutation* of length N is an array where every integer from 1 to N occurs exactly once.

------ Input Format ------ 

- The first line contains a single integer T — the number of test cases. Then the test cases follow.
- The first line of each test case contains an integer N — the size of the array A.
- The second line of each test case contains N integers A_{1}, A_{2}, \ldots, A_{N} denoting the array A.
- The third line of each test case contains an integer K — the size of the array B.
- The fourth line of each test case contains K integers B_{1}, B_{2}, \ldots, B_{K} denoting the numbers which Alice dislikes.

------ Output Format ------ 

For each test case, output the resulting array A after the removal of all occurrences of B_{1}, B_{2}, \ldots B_{K}.

It is guaranteed that there will be at least one element in the resulting array.

------ Constraints ------ 

$1 ≤ T ≤ 1000$
$1 ≤ K < N ≤ 10^{5}$
$1 ≤A_{i}, B_{i} ≤N$
$A$ is initially a *permutation*.
$B_{i} \ne B_{j}$ when $(i \ne j)$
- Sum of $N$ over all test cases does not exceed $2 \cdot 10^{5}$.

----- Sample Input 1 ------ 
3
4
4 1 3 2
2
3 1
9
5 2 9 1 8 6 4 3 7
3
5 8 9
5
3 4 5 1 2
2
2 3

----- Sample Output 1 ------ 
4 2
2 1 6 4 3 7
4 5 1

----- explanation 1 ------ 
Test Case 1: Here $A = [4, 1, 3, 2]$ and $B = [3, 1]$. The resulting array $A$ after removing all the numbers which Alice dislikes is $[4, 2]$.

Note that here $[2, 4]$ is an incorrect answer since the order of elements should be the same as in the original array.

Test Case 2: Here $A = [5, 2, 9, 1, 8, 6, 4, 3, 7]$ and $B = [5, 8, 9]$. The resulting array $A$ after removing all the numbers which Alice dislikes is $[2, 1, 6, 4, 3, 7]$.

Test Case 3: Here $A = [3, 4, 5, 1, 2]$ and $B = [2, 3]$. The resulting array $A$ after removing all the numbers which Alice dislikes is $[4, 5, 1]$.
