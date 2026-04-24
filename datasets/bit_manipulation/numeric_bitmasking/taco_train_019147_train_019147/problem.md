Read problem statements in [Bengali], [Russian], [Mandarin] and [Vietnamese] as well.

You are given an array A of N non-negative integers, where N is odd. Find the minimum non-negative integer x that satisfies the equation

(A_{1} + x) \oplus (A_{2} + x) \oplus \dots \oplus (A_{N} + x) = 0

where \oplus denotes the [bitwise XOR operation]. If no such x exists, print -1.

Note: The input of this problem is large, so use fast input/output methods.

------ Input Format ------ 

- First line of the input contains a single integer T, the number of test cases. The description of T test cases follows.
- The first line of each test case contains a single integer N, denoting the size of the array A.
- The second line of each test case contains N space-separated non-negative integers A_{1}, A_{2} \dots A_{N}.

------ Output Format ------ 

For each test case, print a single line containing one integer. If there does not exist any non-negative integer x that satisfies the given equation, print -1. Otherwise, print the minimum value of x that satisfies the given equation.

------ Constraints ------ 

$1 ≤ T ≤ 10^{5}$
$1 ≤ N ≤ 10^{6}$
$0 ≤ A_{i} ≤ 10^{18}$
- The value of $N$ is guaranteed to be odd.
- Sum of $N$ over all test cases is less than or equal to $10^{6}$.

------ subtasks ------ 

Subtask 1 (20 points):
$1≤ T≤ 10^{3}$
$1≤ N ≤ 10^{3}$
$0≤ A_{i} ≤ 10^{3}$
The value of $N$ is guaranteed to be odd.
Sum of $N$ over all test cases is less than or equal to $10^{3}$.

Subtask 2 (80 points):
Original constraints

----- Sample Input 1 ------ 
4
3
2 4 5
3
0 0 0
3
1 1 1
3
1 1 2

----- Sample Output 1 ------ 
1
0
-1
-1

----- explanation 1 ------ 
Test case 1:

We have to find minimum non-negative integer $x$ such that 
$$(2 + x) \oplus (4 + x) \oplus (5 + x) = 0$$
Let $f(x) = (2 + x) \oplus (4 + x) \oplus (5 + x)$.
- For $x = 0$, we have
$$f(0) = (2 + 0) \oplus (4 + 0) \oplus (5 + 0) = 2\oplus 4\oplus 5 = 3$$
- For $x = 1$, we have
$$f(1) = (2 + 1) \oplus (4 + 1) \oplus (5 + 1) = 3\oplus 5\oplus 6 = 0$$

Therefore, $x = 1$ is the minimum non-negative integer that satisfies the given equation.

Test case 2:

We have to find minimum non-negative integer $x$ such that 
$$(0 + x) \oplus (0 + x) \oplus (0 + x) = 0$$
i.e. $x \oplus x \oplus x = 0$. But since $0 \oplus 0 \oplus 0 = 0$, it follows that $x = 0$ is the minimum non-negative integer that satisfies the given equation.

Test case 3:

We have to find minimum non-negative integer $x$ such that 
$$(1 + x) \oplus (1 + x) \oplus (1 + x) = 0$$
But $a \oplus a = 0$ and $0 \oplus a = a$ for any non-negative integer $a$. It follows that 
$$(1 + x) \oplus (1 + x) \oplus (1 + x) = 0 \oplus (1 + x) = 1 + x$$

This implies that $x$ satisfies the given equation if and only if it satisfies $1 + x = 0$ if and only if $x = -1$. But $-1$ is a negative integer and therefore, there does not exist any $x$ that satisfies the given equation.

Test case 4:

We have to find minimum non-negative integer $x$ such that 
$$(1 + x) \oplus (1 + x) \oplus (2 + x) = 0$$
It follows that 
$$(1 + x) \oplus (1 + x) \oplus (2 + x) = 0 \oplus (2 + x) = 2 + x$$

This implies that $x$ satisfies the given equation if and only if it satisfies $2 + x = 0$, which can only happen if $x = -2$. But $-2$ is a negative integer and therefore, there does not exist any non-negative $x$ that satisfies the given equation, hence we output $-1$.
