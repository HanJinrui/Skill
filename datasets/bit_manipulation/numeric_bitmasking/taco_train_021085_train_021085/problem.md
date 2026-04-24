You are given an array A, consisting of N distinct integers.  
Calculate number of pairs (i,j) (1 ≤ i < j ≤ N), such that 2 \cdot (A_{i} \oplus A_{j}) = A_{i} + A_{j}, where \oplus denotes [bitwise XOR].

------ Input Format ------ 

- The first line contains two integers N - the size of the array. 
- The second line contains N space-separated integers A_{1}, \ldots, A_{N} - the elements of the array A.

------ Output Format ------ 

For each test case, output the number of pairs satisfying constraints.

------ Constraints ------ 

$2 ≤ N ≤ 10^{6}$
$1 ≤ A_{i} ≤ 2^{60}-1$

------ subtasks ------ 

Subtask $1$ (20 points): $2 ≤ N ≤ 2000$
Subtask $2$ (40 points): $1 ≤ A_{i} ≤ 2^{20}-1$
Subtask $3$ (40 points): Original constraints.

----- Sample Input 1 ------ 
4
1 2 3 6

----- Sample Output 1 ------ 
2

----- explanation 1 ------ 
There are $2$ pairs $(i,j)$ satisfying all the conditions.
- $(i,j)= (1, 3)$. Thus, $2\cdot (A_{1}\oplus A_{3}) = 2\cdot (1\oplus 3) = 2\cdot 2 = 4$. Also, $A_{1}+A_{3} = 1+3 = 4$.
- $(i,j)= (2, 4)$. Thus, $2\cdot (A_{2}\oplus A_{4}) = 2\cdot (2\oplus 6) = 2\cdot 4 = 8$. Also, $A_{2}+A_{4} = 2+6 = 8$.

----- Sample Input 2 ------ 
5
4 3 9 7 1
----- Sample Output 2 ------ 
1
----- explanation 2 ------ 
There is only one pair $(i,j)$ satisfying all the conditions:
- $(i,j) = (2, 5)$. Thus, $2\cdot (A_{2}\oplus A_{5}) = 2\cdot (3\oplus 1) = 2\cdot 2 = 4$. Also, $A_{2}+A_{5} = 3+1 = 4$.
