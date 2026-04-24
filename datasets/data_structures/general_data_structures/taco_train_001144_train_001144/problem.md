Chef has an array A of length N.

In one operation, Chef can choose any two distinct indices i, j (1 ≤ i, j ≤ N, i \neq j) and either change A_{i} to A_{j} or change A_{j} to A_{i}.

Find the minimum number of operations required to make all the elements of the array equal.

------ Input Format ------ 

- First line will contain T, number of test cases. Then the test cases follow.
- First line of each test case consists of an integer N - denoting the size of array A.
- Second line of each test case consists of N space-separated integers A_{1}, A_{2}, \dots, A_{N} - denoting the array A.

------ Output Format ------ 

For each test case, output the minimum number of operations required to make all the elements equal.

------ Constraints ------ 

$1 ≤ T ≤ 100$
$2 ≤ N ≤ 1000$
$1 ≤ A_{i} ≤ 1000$

----- Sample Input 1 ------ 
4
3
1 2 3
4
5 5 5 5
4
2 2 1 1
3
1 1 2

----- Sample Output 1 ------ 
2
0
2
1

----- explanation 1 ------ 
Test Case $1$: You can make all the elements equal in $2$ operations. In the first operation, you can choose indices $1, 2$ and convert $A_{1}$ to $A_{2}$. So the array becomes $[2, 2, 3]$. Now you can choose indices $1, 3$ and convert $A_{3}$ to $A_{1}$, so the final array becomes $[2, 2, 2]$.

Test Case $2$: Since all the elements are already equal there is no need to perform any operation.

Test Case $3$: You can make all the elements equal in $2$ operations. In the first operation, you can choose indices $1, 3$ and convert $A_{1}$ to $A_{3}$. So the array becomes $[1, 2, 1, 1]$. Now you can choose indices $1, 2$ and convert $A_{2}$ to $A_{1}$, so the final array becomes $[1, 1, 1, 1]$.

Test Case $4$: You can make all the elements equal in $1$ operation. You can pick indices $2, 3$ and convert $A_{3}$ to $A_{2}$ after which the array becomes $[1, 1, 1]$.
