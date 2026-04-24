Given an array A consisting of N non-negative integers. 

You need to perform the following operation (N - 1) times:
Sort the array A in ascending order.
Let M be the current size of the array A. Replace the array A by [(A_{2} - A_{1}), (A_{3} - A_{2}), \ldots ,(A_{M} - A_{M-1})]. Note that each time the operation is performed, the size of the array reduces by one.

Find the remaining element after (N-1) operations.

------ Input Format ------ 

- The first line contains an integer T denoting number of test cases. The T test cases then follow.
- The first line of each test case contains an integer N - the size of the array.
- The second line of each test case contains N space-separated integers A_{1}, A_{2}, \ldots, A_{N}.

------ Output Format ------ 

For each test case, output single line: the remaining element after (N-1) operations.

------ Constraints ------ 

$1 ≤ T ≤ 10^{5}$
$1 ≤ N ≤ 10^{5}$
$0 ≤ A_{i} ≤ 10^{18}$
- Sum of $N$ over all test cases does not exceed $2 \cdot 10^{5}$.

----- Sample Input 1 ------ 
2
4
29 19 0 3
1
777
----- Sample Output 1 ------ 
1
777
----- explanation 1 ------ 
- Test case 1: The operations look like:
- Operation $1$: Sort the array. Now, $A$ becomes $[0, 3, 19, 29]$. Replace the array. Thus, $A = [(3-0), (19-3), (29-19)] = [3, 16, 10]$.
- Operation $2$: Sort the array. Now, $A$ becomes $[3, 10, 16]$. Replace the array. Thus, $A = [(10-3), (16-10)] = [7, 6]$.
- Operation $3$: Sort the array. Now, $A$ becomes $[6, 7]$. Replace the array. Thus, $A = [(7-6)] = [1]$.

Thus, the remaining element after $3$ operations is $1$.

- Test case 2: Since $N = 1$, you don't need to perform any operation. The remaining element after $0$ operations is $777$.
