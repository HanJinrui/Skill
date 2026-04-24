You have a binary string S of length N. In one operation you can select a substring of S and reverse it. For example, on reversing the substring S[2,4] for S=11000, we change 1 \textcolor{red}{100} 0 \rightarrow 1 \textcolor{red}{001} 0.

Find the minimum number of operations required to sort this binary string.  
It can be proven that the string can always be sorted using the above operation finite number of times.

------ Input Format ------ 

- The first line of input will contain a single integer T, denoting the number of test cases.
- Each test case consists of 2 lines of input.
- The first line of each test case contains a single integer N — the length of the binary string.
- The second line of each test case contains a binary string S of length N.

------ Output Format ------ 

For each test case, output on a new line — the minimum number of operations required to sort the binary string.

------ Constraints ------ 

$1 ≤ T ≤ 2\cdot 10^{5}$
$1 ≤ N ≤ 2\cdot 10^{5}$
- Sum of $N$ over all test cases does not exceed $10^{6}$.
- String $S$ consists of only '$0$'s and '$1$'s.

----- Sample Input 1 ------ 
4
3
000
4
1001
4
1010
6
010101
----- Sample Output 1 ------ 
0
1
2
2
----- explanation 1 ------ 
Test case $1$: The string is already sorted, hence, zero operations are required to sort it. 

Test case $2$: We can sort the string in the following way:  $\textcolor{red}{100} 1$ $\rightarrow$ $0011$. 

Test case $3$: We can sort the string in the following way:  
$1 \textcolor{red}{01} 0$ $\rightarrow$ $\textcolor{red}{1100}$ $\rightarrow$ $0011$.  
It can be proven that this string cannot be sorted in less than $2$ operations.

Test case $4$: We can sort the string in the following way:  
$0 \textcolor{red}{1010}1$ $\rightarrow$ $00 \textcolor{red}{10}11$ $\rightarrow$ $000111$.  
It can be proven that this string cannot be sorted in less than $2$ operations.
