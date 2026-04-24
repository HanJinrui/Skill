Given two arrays A and B each of length N.
   
Find the value \sum_{i=1}^N\sum_{j=1}^N \max(A_{i}\oplus B_{j},A_{i}\& B_{j}).  
Here \oplus and \& denote the [bitwise XOR operation] and [bitwise AND operation] respectively.

------ Input Format ------ 

- The first line of input contains a single integer T - the number of test cases. The description of T test cases follows.
- The first line of each test case contains an integer N - the length of arrays A and B.
- The second line of each test case contains N space-separated integers A_{1},A_{2},…,A_{N} representing the array A.
- The third line of each test case contains N space-separated integers B_{1},B_{2},…,B_{N} representing the array B.

------ Output Format ------ 

For each test case, output the value \sum_{i=1}^N\sum_{j=1}^N \max(A_{i}\oplus B_{j},A_{i}\& B_{j}).

------ Constraints ------ 

$1 ≤ T ≤ 10^{5}$
$1 ≤ N ≤ 10^{5}$
$0 ≤ A_{i}, B_{i} < 2^{20}$
- Sum of $N$ does not exceed $2\cdot 10^{5}$ over all test cases.

----- Sample Input 1 ------ 
3
2
3 4
1 2
1
0
0
3
2 4 3
1 2 1
----- Sample Output 1 ------ 
15
0
30
----- explanation 1 ------ 
- Test Case $1$: For the given arrays, the value is: $\max(3\oplus 1,3\& 1) + \max(3\oplus 2,3\& 2) + \max(4\oplus 1,4\& 1) + \max(4\oplus 2,4\& 2) = 2 + 2 + 5 + 6 = 15$.

- Test Case $2$: For the given arrays, the value is: $\max(0\oplus 0,0\& 0) = 0$.

- Test Case $3$: For the given arrays, the value is: $\max(2\oplus 1,2\& 1) + \max(2\oplus 2,2\& 2) + \max(2\oplus 1,2\& 1) + \max(4\oplus 1,4\& 1) + \max(4\oplus 2,4\& 2) + \max(4\oplus 1,4\& 1) + \max(3\oplus 1,3\& 1) + \max(3\oplus 2,3\& 2) + \max(3\oplus 1,3\& 1)$  
$= 3 + 2 + 3 + 5 + 6 + 5 + 2 + 2 + 2 = 30$.
