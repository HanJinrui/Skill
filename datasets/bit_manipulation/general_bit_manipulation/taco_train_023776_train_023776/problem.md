Consider a zero-indexed matrix with $m$ rows and $n$ columns, where each row is filled gradually. Given the first row of the matrix, you can generate the elements in the subsequent rows using the following formula:

$a_{i,j}=a_{i-1,j}\oplus a_{i-1,j+1}\text{}\forall j:0\leq j\leq n-2$
$a_{i,n-1}=a_{i-1,n-1}\oplus a_{i-1,0}$

Each row is generated one by one, from the second row through the last row. Given the first row of the matrix, find and print the elements of the last row as a single line of space-separated integers.

Note: The $\theta$ operator denotes bitwise XOR.

Input Format

The first line contains two space-separated integers denoting the respective values of $n$ (the number of columns in the matrix) and $m$ (the number of rows in the matrix). 

The second line contains $n$ space-separated integers denoting the respective values of the elements in the matrix's first row.

Constraints

$1\leq n\leq10^5$
$1\leq m\leq10^{18}$
$0\leq a_{i,j}\leq10^9$

Output Format

Print $n$ space-separated integers denoting the respective values of the elements in the last row of the matrix.

Sample Input 0
4 2
6 7 1 3

Sample Output 0
1 6 2 5

Explanation 0

We use the formula given above to calculate the $n=4$ values in the last row of the matrix:

$a_{1,0}=a_{0,0}\oplus a_{0,1}=6\oplus7=1$  
$a_{1,1}=a_{0,1}\oplus a_{0,2}=7\oplus1=6$  
$a_{1,2}=a_{0,2}\oplus a_{0,3}=1\oplus3=2$  
$a_{1,3}=a_{0,3}\oplus a_{0,0}=3\oplus6=5$  

We then print each value (in order) as a single line of space-separated integers.
