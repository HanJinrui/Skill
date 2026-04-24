Chef found an array A of N elements. He defines a subarray as *bad* if the maximum element of the subarray is equal to the minimum element of the subarray.

More formally, a subarray [L,R] (1 ≤ L ≤ R ≤ N) is *bad* if \texttt{max}(A_{L}, A_{L+1}, \ldots , A_{R}) = \texttt{min} (A_{L}, A_{L+1}, ... , A_{R}).

Chef is allowed to change at most K elements of the array.  
Find the minimum number of *bad* subarrays Chef can obtain after changing at most K elements of the array.    

------ Input Format ------ 

- First line will contain T, the number of test cases. Then the test cases follow.
- Each test case contains two lines of input, the first line contains two space-separated integers N and K - the number of elements in the array and the maximum number of elements Chef can change respectively.
- The second line contains N space-separated integers A_{1}, A_{2},\ldots, A_{N} - the initial array.

------ Output Format ------ 

For each test case, output the minimum number of *bad* subarrays Chef can obtain after changing at most K elements of the array.

------ Constraints ------ 

$1 ≤ T ≤ 3\cdot 10^{4}$
$1 ≤ N ≤ 10^{5}$
$1 ≤ K ≤ N$
$1 ≤ A_{i} ≤ 10^{9}$
- Sum of $N$ over all test cases does not exceed $3\cdot 10^{5}$.

----- Sample Input 1 ------ 
3
3 1
1 2 3
4 2
3 3 3 1
5 1
1 1 1 1 1

----- Sample Output 1 ------ 
3
4
7

----- explanation 1 ------ 
Test case $1$: The minimum number of *bad* subarrays Chef can obtain is $3$. Chef does not need to perform any operations. The subarrays where the maximum element is equal to the minimum element are $[1,1], [2,2],$ and $[3,3]$ where $[L,R]$ denotes the subarray starting at index $L$ and ending at index $R$.

Test case $2$: The minimum number of *bad* subarrays Chef can obtain is $4$. Chef can perform $2$ operations and change the array to $[2, 4, 3, 1]$. The subarrays where the maximum element is equal to the minimum element are $[1,1], [2,2], [3,3],$ and $[4,4]$.
