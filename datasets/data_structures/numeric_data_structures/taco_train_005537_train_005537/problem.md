Read problems statements in [Russian].

Chef has an array A of size N. Chef wants to choose any subsequence of size exactly  \lceil \frac{N}{2} \rceil from the array such that GCD of all the elements in that sequence must be 2. Chef names such a kind of sequence as a *half-sequence*.   

Help Chef to find whether he would be able to select any half-sequence in the given array.

As a reminder,
A subsequence of an array is a sequence that can be derived from the given array by deleting zero or more elements without changing the order of the remaining elements.   
GCD stands for Greatest Common Divisor. The greatest common divisor of a subsequence is the largest integer d such that all the numbers in sequence are divisible by d. For more information, refer to [here].
\lceil x \rceil  is the ceiling (round up) operation:  \lceil 3.5 \rceil = 4 ,\lceil 2 \rceil = 2 .   

------ Input Format ------ 

- The first line contains an integer T denoting the number of test cases. The T test cases then follow.
- The first line of each test case contains a single integer N denoting the size of the array.
- The second line of each test case contains N space-separated integers A_{1}, A_{2}....A_{N} denoting the given array.

------ Output Format ------ 

For each test case, output on one line YES if Chef can find a half-sequence, else print NO. Output is case insensitive.

------ Constraints ------ 

$1 ≤T ≤20$
$2 ≤N ≤10^{5}$
$1 ≤A_{i} ≤10^{9}$
- Sum of $N$ over all test cases does not exceed $10^{5}$

----- Sample Input 1 ------ 
3
5
1 2 3 4 5
4
1 2 3 4
3
30 42 70
----- Sample Output 1 ------ 
NO
YES
NO
----- explanation 1 ------ 
- For the first test case, Chef wants to select $\lceil \frac{5}{2} \rceil = 3$ numbers. But for any $3$ numbers, GCD would not be $2$. Therefore the answer is NO.

- For the second test case, Chef wants to select $\lceil \frac{4}{2} \rceil = 2$ numbers. Chef can select the subsequence $[2,4]$ with GCD of $2$. Therefore the answer is YES.

- For the third test case, Chef wants to select $\lceil \frac{3}{2} \rceil = 2$ numbers. But for any $2$ numbers, GCD would be bigger than $2$. Therefore the answer is NO.
