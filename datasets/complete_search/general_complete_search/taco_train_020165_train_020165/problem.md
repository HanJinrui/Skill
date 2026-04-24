Chef received an array A of N integers as a valentine's day present. He wants to maximize the length of the longest strictly increasing subsequence by choosing a subarray and adding a fixed integer X to all its elements.

More formally, Chef wants to maximize the length of the [longest strictly increasing subsequence] of A by performing the following operation at most once:

Pick 3 integers L, R and X \ (1 ≤ L ≤ R ≤ N, \ X \in \mathbb{Z}) and assign A_{i} := A_{i} + X \ \forall \ i \in [L, R].

Find the length of the longest strictly increasing sequence Chef can obtain after performing the operation at most once.

------ Input Format ------ 

- The first line of the input contains a single integer T denoting the number of test cases. The description of T test cases follows.
- The first line of each test case contains one integer N, the size of the array.
- The next line contains N space-separated integers, where the i^{th} integer denotes A_{i}.

------ Output Format ------ 

For each test case, print a single line containing one integer ― the length of the longest strictly increasing sequence Chef can obtain.

------ Constraints ------ 

$1 ≤ T ≤ 10^{3}$
$1 ≤ N ≤ 2 \times 10^{5}$
$1 ≤ A_{i} ≤ 10^{9}$
- Sum of $N$ over all test cases does not exceed $2 \cdot 10^{5}$.

----- Sample Input 1 ------ 
3
3
1 2 1
5
1 5 8 6 9
4
1 2 2 1

----- Sample Output 1 ------ 
3
5
3

----- explanation 1 ------ 
Test case $1$: Chef can pick $(L,R,X)=(3,3,2)$. On performing the operation, $A$ becomes $[1,2,3]$. The LIS of the updated array has length $3$. The elements of the LIS are $[1,2,3]$.

Test case $2$: Chef can pick $(L,R,X)=(2,3,-3)$. On performing the operation, $A$ becomes $[1,2,5,6,9]$. The LIS of the updated array has length $5$. The elements of the LIS are $[1,2,5,6,9]$.

Test case $3$: Chef can pick $(L,R,X)=(4,4,4)$. On performing the operation, $A$ becomes $[1,2,2,5]$. The LIS of the updated array has length $3$. The elements of the LIS are $[1,2,5]$.
