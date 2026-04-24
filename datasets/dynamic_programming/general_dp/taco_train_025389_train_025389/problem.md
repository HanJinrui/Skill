You are given an array A consisting of N integers.

In one operation, you can:
Choose any two indices i and j (i \neq j);
Subtract min(A_{i} , A_{j}) from both A_{i} and A_{j}. Note that min(A_{i} , A_{j}) denotes the minimum of A_{i} and A_{j}.

Determine whether you can make all the elements of the array equal to zero in less than or equal to N operations.

If it is possible to do so, output the required operations as well.

------ Input Format ------ 

- The first line of input contains a single integer T, denoting the number of test cases. The description of T test cases follows.
- The first line of each test case contains a single integer N, denoting number of elements in A.
- The second line of each test case contains N space-separated integers A_{1}, A_{2}, \ldots, A_{N}.

------ Output Format ------ 

For each test case, if it possible to make all the elements of the array equal to zero in less than or equal to N operations, print K+1 lines:
- In the first line, print K (1≤ K ≤ N), the required operations.
- In each of the next K lines, print two space-separated integers i and j, denoting the operation.

In case it is not possible to make all elements equal to 0, print a single line containing -1.

------ Constraints ------ 

$1 ≤ T ≤ 50$
$2 ≤ N ≤ 300$
$1 ≤ A_{i} ≤ 300$
- The sum of $N$ over all test cases does not exceed $600$.

----- Sample Input 1 ------ 
3
2
1 1 
3 
1 3 1
4
1 3 1 3

----- Sample Output 1 ------ 
1
1 2
-1
2
1 3
2 4
----- explanation 1 ------ 
Test case $1$: We can pick $i = 1$ and $j = 2$ and subtract $min(A_{1}, A_{2}) = 1$ from both $A_{1}$ and $A_{2}$. Thus, the final array is $[0 , 0]$.

Test case $2$: It can be proven that there is no way to make all elements of the array equal to zero.

Test case $3$: We can perform $2$ operations in the following way:
- Pick $i = 1$ and $j = 3$ and subtract $min(A_{1}, A_{3}) = 1$ from both $A_{1}$ and $A_{3}$. Thus, the obtained array is $[0, 3, 0, 3]$.
- Pick $i = 2$ and $j = 4$ and subtract $min(A_{2}, A_{4}) = 3$ from both $A_{2}$ and $A_{4}$. Thus, the obtained array is $[0, 0, 0, 0]$.
