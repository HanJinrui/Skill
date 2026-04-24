You are given arrays A and B with N non-negative integers each.

An array X of length N is called *good*, if:
All elements of the array X are non-negative;
X_{1} | X_{2} | \ldots | X_{i} = A_{i} for all (1≤ i≤ N);
X_{i} \& X_{(i+1)} \& \ldots \& X_{N} = B_{i} for all (1≤ i≤ N).

Find the maximum bitwise XOR of all elements over all good arrays X.  
More formally, find the maximum value of X_{1}\oplus X_{2}\oplus \ldots X_{N}, over all good arrays X.  
It is guaranteed that at least one such array X exists.

Note that |, \&, and \oplus denote the bitwise [or], [and], and [xor] operations respectively.

------ Input Format ------ 

- The first line of input will contain a single integer T, denoting the number of test cases.
- Each test case consists of multiple lines of input.
- The first line of each test case contains one integer N — the size of the array.
- The next line contains N space-separated integers describing the elements of the array A. 
- The next line contains N space-separated integers describing the elements of the array B. 

------ Output Format ------ 

For each test case, output on a new line, the maximum bitwise XOR of all elements over all good arrays X.  

------ Constraints ------ 

$1 ≤ T ≤ 10^{5}$
$1 ≤ N ≤ 10^{5}$
$0 ≤ A_{i} < 2^{30}$
$0 ≤ B_{i} < 2^{30}$
- It is guaranteed that at least one such array $X$ exists.
- Sum of $N$ over all test cases is less than $3\cdot 10^{5}$.

----- Sample Input 1 ------ 
2
3
0 3 3
0 2 2
2
2 3
0 1

----- Sample Output 1 ------ 
1
3
----- explanation 1 ------ 
Test case $1$: An optimal *good* array is $X = [0, 3, 2]$.
- For $i = 1$: $A_{1} = X_{1} = 0$ and $B_{1} = X_{1}$ $\&$ $X_{2}$ $\&$ $X_{3} = 0$.
- For $i = 2$: $A_{2} = X_{1}$ $|$ $X_{2} = 3$ and $B_{2} = X_{2}$ $\&$ $X_{3} = 2$.
- For $i = 3$: $A_{3} = X_{1}$ $|$ $X_{2}$ $|$ $X_{3} = 3$ and $B_{3} = X_{3} = 2$.

The XOR of all elements of $X$ is $0\oplus 3\oplus 2 = 1$. It can be proven that this is the maximum XOR value for any $X$.

Test case $2$: An optimal *good* array is $X = [2, 1]$.
- For $i = 1$: $A_{1} = X_{1} = 2$ and $B_{1} = X_{1}$ $\&$ $X_{2} = 0$.
- For $i = 2$: $A_{2} = X_{1}$ $|$ $X_{2} = 3$ and $B_{2} = X_{2} = 1$.

The XOR of all elements of $X$ is $2\oplus 1 = 3$. It can be proven that this is the maximum XOR value for any $X$.
