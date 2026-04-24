Chef has an array A of length N.

In one operation, Chef can remove any one element from the array. 

Determine the minimum number of operations required to make all the elements same.

------ Input Format ------ 

- The first line of input will contain a single integer T, denoting the number of test cases.
- Each test case consists of multiple lines of input.
- The first line of each test case contains a single integer N —the length of Array A.
- Next line contains N space-separated integers A_{1}, A_{2}, A_{3}, \dots, A_{N} - denoting the array A.

------ Output Format ------ 

For each test case, output the minimum number of operations required to make all the elements same.

------ Constraints ------ 

$1 ≤ T ≤ 4000$
$1 ≤ N ≤ 10^{5}$
$1 ≤ A_{i} ≤ N$
- Sum of $N$ over all test cases do not exceed $3 \cdot 10^{5}$

----- Sample Input 1 ------ 
4
3
3 3 3
6
1 3 2 1 2 2
4
1 2 1 2
5
1 3 2 4 5

----- Sample Output 1 ------ 
0
3
2
4

----- explanation 1 ------ 
Test case $1$: All the elements are already same. Thus we need to perform zero operations.

Test case $2$: We remove the elements $A_{1}, A_{2},$ and $A_{4}$ using three operations. The array becomes $[2, 2, 2]$ where all elements are same.

Test case $3$: We remove the elements $A_{1}$ and $A_{3}$ using two operations. The array becomes $[2, 2]$ where all elements are same.

Test case $4$: We remove the elements $A_{1}, A_{2}, A_{3},$ and $A_{4}$ using four operations. The array becomes $[5]$.
