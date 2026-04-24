There is an array A with N elements. Each element of A has a fixed *polarity*: either north or south. 

Chef is allowed to perform some (possibly zero) operations on the array A. In one operation, Chef can:

Pick some subarray of array A, such that, the first and last elements of the subarray have different polarities, and, rearrange the elements in this subarray any way he wants. 

Note that the polarity of each element remains unchanged after an operation.

Find the minimum number of operations required to sort the array in non-decreasing order, or state that it is impossible.

A subarray of A is obtained by deletion of several (possibly, zero or all) elements from the beginning and several (possibly, zero or all) elements from the end.

------ Input Format ------ 

- The first line contains an integer T, denoting the number of test cases. The T test cases then follow.
- The first line of each test case contains a single integer N.
- The second line of each test case contains N space-separated integers A_{1}, A_{2}, \ldots, A_{N}.
- The third line of each test case contains a string of length N, the ith character of which is either \texttt{N} or \texttt{S}, representing that the ith element of A has north or south polarity, respectively.

------ Output Format ------ 

For each test case, if it impossible to sort the array, output -1. Otherwise, output a single integer: the minimum number of operations required to sort the array.

------ Constraints ------ 

$1 ≤ T ≤ 10^{5}$
$1 ≤ N ≤ 2 \cdot 10^{5}$
$1 ≤ A_{i} ≤ 10^{9}$
- The sum of $N$ across all test cases doesn't exceed $2 \cdot 10^{5}$.

------ subtasks ------ 

Subtask #1 (100 points): original constraints

----- Sample Input 1 ------ 
6
5
1 3 2 3 7
NNSNS
2
2 1
SS
3
1 8 12
SNS
3
3 2 1
NSN
5
1 2 3 5 4
NSNSN
5
1 1 2 2 1
SNSNN

----- Sample Output 1 ------ 
1
-1
0
2
1
1

----- explanation 1 ------ 
Let's represent elements with a polarity of north in $\color{red}{\text{red}}$, and elements with a polarity of south in $\color{blue}{\text{blue}}$. The polarity of each element is also labelled above it.

- In the first test case, we can sort the array in a single operation as follows.
- Rearrange the subarray $[A_{1}, A_{2}, A_{3}]$: $[\color{red}{\stackrel{\texttt{N}}{1}}, \color{red}{\stackrel{\texttt{N}}{3}}, \color{blue}{\stackrel{\texttt{S}}{2}}, \color{red}{\stackrel{\texttt{N}}{3}}, \color{blue}{\stackrel{\texttt{S}}{7}}\color{black}{]} \to [\color{red}{\stackrel{\texttt{N}}{1}}, \color{blue}{\stackrel{\texttt{S}}{2}}, \color{red}{\stackrel{\texttt{N}}{3}}, \color{red}{\stackrel{\texttt{N}}{3}}, \color{blue}{\stackrel{\texttt{S}}{7}}\color{black}{]}$.

- In the second test case, the array $[\color{blue}{\stackrel{\texttt{S}}{2}}, \color{blue}{\stackrel{\texttt{S}}{1}}\color{black}{]}$ cannot be sorted, since no operations can be performed.

- In the third test case, the array is already sorted, so the answer is $0$.

- In the fourth test case, we can sort the array in two operations as follows.

- Rearrange the subarray $[A_{2}, A_{3}]$: $[\color{red}{\stackrel{\texttt{N}}{3}}, \color{blue}{\stackrel{\texttt{S}}{2}}, \color{red}{\stackrel{\texttt{N}}{1}}\color{black}{]} \to [\color{red}{\stackrel{\texttt{N}}{3}}, \color{red}{\stackrel{\texttt{N}}{1}}, \color{blue}{\stackrel{\texttt{S}}{2}}\color{black}{]}$.
- Rearrange the subarray $[A_{1}, A_{2}, A_{3}]$: $[\color{red}{\stackrel{\texttt{N}}{3}}, \color{red}{\stackrel{\texttt{N}}{1}}, \color{blue}{\stackrel{\texttt{S}}{2}}\color{black}{]} \to [\color{red}{\stackrel{\texttt{N}}{1}}, \color{blue}{\stackrel{\texttt{S}}{2}}, \color{red}{\stackrel{\texttt{N}}{3}}\color{black}{]}$.
