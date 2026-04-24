JJ had an array A of length N such that 0 ≤ A_{i} < 2^{30} for all 1 ≤ i ≤ N.  
He listed down the [XOR] of all the [subsequences] of A of size ≥ (N - 1) in some random order. Let's call the XOR of these (N + 1) subsequences as B_{1}, B_{2}, \ldots, B_{N+1}.

Unfortunately, he lost the initial array A. Can you help him recover it?

If there are multiple arrays which satisfy the given conditions, print any. Also, it is guaranteed that corresponding to the given input, an answer always exists.

------ Input Format ------ 

- The first line will contain T - the number of test cases. Then the test cases follow.
- The first line of each test case contains an integer N - the size of the initial array A.
- The second line of each test case contains (N + 1) integers B_{1}, B_{2}, \ldots, B_{N+1} - the XOR of all the subsequences of A of size ≥ (N - 1) in some random order.

------ Output Format ------ 

For each test case, output N integers A_{1}, A_{2}, \ldots, A_{N} which satisfy the given conditions.

If multiple answers exist, print any.

------ Constraints ------ 

$1 ≤ T ≤ 10^{5}$
$2 ≤ N ≤ 2 \cdot 10^{5}$
$0 ≤ B_{i} < 2^{30}$
- Sum of $N$ over all test cases does not exceed $2 \cdot 10^{5}$.

------ subtasks ------ 

Subtask 1 (40 points):
$N$ is odd
Subtask 2 (60 points):
Original constraints.

----- Sample Input 1 ------ 
2
3
2 3 0 1
5
27 15 23 30 29 31

----- Sample Output 1 ------ 
1 2 3
1 2 4 8 16

----- explanation 1 ------ 
Let $\oplus$ denote the [bitwise XOR operation].

- Test Case 1: $A = [1, 2, 3]$ satisfies all the conditions since $[2, 3, 0, 1] = [1 \oplus 3, 1 \oplus 2, 1 \oplus 2 \oplus 3, 2 \oplus 3]$

- Test Case 2: $A = [1, 2, 4, 8, 16]$ satisfies all the conditions since $[27, 15, 23, 30, 29, 31] = 
[1 \oplus 2 \oplus 8 \oplus 16, 1 \oplus 2 \oplus 4 \oplus 8, 1 \oplus 2 \oplus 4 \oplus 16, 2 \oplus 4 \oplus 8 \oplus 16, 1 \oplus 4 \oplus 8 \oplus 16, 1 \oplus 2 \oplus 4 \oplus 8 \oplus 16]$

----- Sample Input 2 ------ 
2
2
1 0 1
4
5 3 1 4 3

----- Sample Output 2 ------ 
1 1
5 4 2 2

----- explanation 2 ------ 
Note: The above test case belongs to subtask 2.

Let $\oplus$ denote the [bitwise XOR operation].

- Test Case 1: $A = [1, 1]$ satisfies all the conditions since $[1, 0, 1] = [1, 1 \oplus 1, 1]$

- Test Case 2: $A = [5, 4, 2, 2]$ satisfies all the conditions since $[5, 3, 1, 4, 3] = [5 \oplus 2 \oplus 2, 5 \oplus 4 \oplus 2, 5 \oplus 4 \oplus 2 \oplus 2, 4 \oplus 2 \oplus 2, 5 \oplus 4 \oplus 2]$
