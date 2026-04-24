You are given an array A of N positive integers. Let G be the [gcd] of all the numbers in the array A. 
 
You have to find if there exist K non-empty, non-intersecting subarrays of A for which the [arithmetic mean] of the gcd of those K subarrays equals G.

Formally, let g_{1}, g_{2}, \ldots, g_{K} be the gcd of those K chosen subarrays, then, \frac{(g_{1} + g_{2} + .... + g_{K})}{K} = G should follow.

If there exist K such subarrays, output YES, otherwise output NO.

Note: Two subarrays are non-intersecting if there exists no index i, such that, A_{i} is present in both the subarrays.

------ Input Format ------ 

- The first line of input will contain a single integer T, denoting the number of test cases.
- Each test case consists of multiple lines of input.
- The first line of each test case contains two space-separated integers — the number of integers in the array A and the integer K, respectively.
- The next line contains N space-separated positive integers A_{1}, A_{2}, \ldots, A_{N}, the elements of the array A.

------ Output Format ------ 

For each test case, if there exist K such subarrays, output YES, otherwise output NO.

You may print each character of the string in uppercase or lowercase (for example, the strings YES, yEs, yes, and yeS will all be treated as identical).

------ Constraints ------ 

$1 ≤ T ≤ 1000$
$1 ≤ N ≤ 2 \cdot {10}^5$
$1 ≤ K ≤ N$
$1 ≤ A_{i} ≤ 2 \cdot {10}^5$
- The sum of $N$ over all test cases won't exceed $4 \cdot {10}^5$.

----- Sample Input 1 ------ 
4
6 4
2 2 3 3 2 2
1 1
1
5 3
1 2 3 4 5
4 3
6 12 18 24
----- Sample Output 1 ------ 
NO
YES
YES
NO

----- explanation 1 ------ 
Test case $1$: It is impossible to find $4$ non-empty, non-intersecting subarrays which satisfy the given condition.

Test case $2$: There is only one element in the array. Here, $G = 1$ and, for the subarray $[1]$, $g = 1$. Thus, it is possible to satisfy the conditions. 

Test case $3$: Here, $G = gcd(1,2,3,4,5) = 1$. We can choose $3$ non-empty, non-intersecting subarrays $\{[1], [2,3], [4,5]\}$ where $gcd(1) = 1$, $gcd(2,3) = 1$, and $gcd(4,5) = 1$. Thus, the arithmetic mean = $\frac{(1 + 1 + 1)}{3} = 1$. Hence, we can have $3$ such subarrays.  

Test case $4$: It is impossible to find $3$ non-empty, non-intersecting subarrays which satisfy the given condition.
