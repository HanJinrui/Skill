Given an array A of size N. 

You can do the following operation on the array:
Pick any 2 distinct indices i and j such that A_{i}=A_{j};
Change all the elements between the indices i and j to A_{i}, i.e, for all k (i ≤ k ≤ j), set A_{k}=A_{i}.

Find the minimum number of operations required to sort the array in non-decreasing order. If it is not possible to sort the array, print -1 instead.

------ Input Format ------ 

- The first line contains a single integer T - the number of test cases. Then the test cases follow.
- The first line of each test case contains an integer N - the size of the array A.
- The second line of each test case contains N space-separated integers A_{1}, A_{2}, \dots, A_{N} denoting the array A.

------ Output Format ------ 

For each test case, the minimum number of operations required to sort the array. If it is not possible to sort the array, print -1 instead.

------ Constraints ------ 

$1 ≤ T ≤ 10^{4}$
$1 ≤ N ≤ 2 \cdot 10^{5}$
$0 ≤ A_{i} ≤ N $
- Sum of $N$ over all test cases does not exceed $2 \cdot 10^{5}$.

----- Sample Input 1 ------ 
2
6
1 2 1 3 4 3
3
3 1 2
----- Sample Output 1 ------ 
2
-1
----- explanation 1 ------ 
Test Case $1$: We can sort the array using $2$ operations. 
- In the first operation select indices $1$ and $3$. After this operation, the array will be $A = [1,1,1,3,4,3]$.
- In the second operation select indices $4$ and $6$. After this operation, the array will be $A = [1,1,1,3,3,3]$.

Thus, the array is sorted using $2$ operations. It can be proven that the array cannot be sorted in less than $2$ operations.

Test Case $2$: It is not possible to sort the array using any number of operations.
