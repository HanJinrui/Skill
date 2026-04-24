Read problem statements in [Mandarin], [Russian], and [Vietnamese] as well.

An index of an array is called a fixed point if the value on the index of the array is equal to the index itself. Formally, an index i of an array A of length N is a fixed point if A_{i} = i, where 1≤ i ≤ N.

For example, in the array A = [1, 3, 3, 4, 1], the indices 1, 3, 4 are fixed points.

Chef has an array A consisting of N integers. Chef tries to find the number of fixed points over all subarrays of the array A. More formally, for every pair (L, R) such that 1 ≤ L ≤ R ≤ N, Chef considers the subarray A_{L}, A_{L+1}, \dots, A_{R} and calculates the total number of fixed points in all such subarrays. However, Chef finds this task very hard. Can you help him find the number of fixed points over all subarrays?

------ Input Format ------ 

- The first line contains T denoting the number of test cases. Then the test cases follow.
- The first line of each test case contains an integer N, denoting the length of the array.
- The second line contains N space-separated integers A_{1}, A_{2}, \dots, A_{N}, denoting the given array.

------ Output Format ------ 

For each test case, print a single line containing one integer - the number of fixed points over all subarrays.

------ Constraints ------ 

$1 ≤ T ≤ 10^{3}$
$1 ≤ N ≤ 10^{5}$
$1 ≤ A_{i} ≤ N$
- Sum of $N$ over all test caes does not exceed $5\cdot 10^{5}$.

------ subtasks ------ 

Subtask 1 (100 points): Original constraints

----- Sample Input 1 ------ 
3
2
1 2
3
2 3 2
4
1 3 4 2

----- Sample Output 1 ------ 
3
1
5

----- explanation 1 ------ 
Let, $A[L, R]$ denotes the subarray consisting of integers from index $L$ to index $R$ of the array $A$(i.e $A_{L}, A_{L+1}, \dots, A_{R}$).

Test case $1$: 
- In the subarray $A[1, 1] = [1]$, the number of fixed points is $1$.
- In the subarray $A[1, 2] = [1, 2]$, the number of fixed points is $2$.
- In the subarray $A[2, 2] = [2]$, there is no fixed point.

Hence the total fixed points over all subarrays $= 1 + 2 + 0 = 3$.

Test case $2$: In the subarray $A[2, 3] = [3, 2]$, the second index is a fixed point. There is no fixed point in any other subarrays.
