You are given an array A of length N. 

You can perform the following operation on the array, as long as it has more than one element:
Choose any two adjacent elements, remove them from the array and insert their sum at that position.
Formally, if the current length of the array is |A|, you can choose an index 1 ≤ i < |A|, and transform the array into [A_{1}, A_{2}, \ldots, A_{i-1}, A_{i} + A_{i+1}, A_{i+2}, \ldots, A_{N}].

Note that after each operation, the length of array decreases by exactly 1.

Print the minimum number of operations to be applied on array A such that all the elements in the resulting array are equal. See sample explanation for more details.

------ Input Format ------ 

- The first line of input contains a single integer T, denoting the number of test cases. The description of T test cases follows.
- Each test case consists of two lines of input.
- The first line contains an integer N.
- The second line contains N space-separated integers, the elements of array A.

------ Output Format ------ 

For each test case, output on a new line the minimum number of operations required to make all the elements equal.

------ Constraints ------ 

$1 ≤ T ≤ 10^{4}$
$2 ≤ N ≤ 3 \cdot 10^{4}$
$-3 \cdot 10^{4} ≤ A_{i} ≤ 3 \cdot 10^{4}$
- Sum of $N$ over all test cases does not exceed $3 \cdot 10^{4}$

------ subtasks ------ 

Subtask #1 (100 points): Original constraints

----- Sample Input 1 ------ 
4
3
5 2 3
2
6 9
5
3 6 5 4 9
3
3 3 3

----- Sample Output 1 ------ 
1
1
2
0

----- explanation 1 ------ 
Test case $1$: It is optimal to remove $A_{2}$ and $A_{3}$ in the first operation, after which the array becomes $[5,5]$ — all of whose elements are equal.

Test case $2$: Remove $A_{1}$ and $A_{2}$ after which the array becomes $[15]$, which contains equal elements because it is of length $1$.

Test case $3$: First remove $A_{3}$ and $A_{4}$ after which the updated array $A$ becomes $[3,6,9,9]$. Now remove $A_{1}$ and $A_{2}$ after which the array becomes $[9,9,9]$. 

Test case $4$: The array elements are already equal.
