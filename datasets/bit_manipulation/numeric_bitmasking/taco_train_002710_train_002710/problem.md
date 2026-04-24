You are given an array A consisting of N integers.

From array A, we create a new array B containing all pairwise bitwise ANDs of elements from A. That is, B consists of N\cdot(N-1)/2 elements, each of the form A_{i} \mathbin{\&} A_{j} for some 1 ≤ i < j ≤ N.

In array B, we repeat the following process till there is only one element remaining:
Let the current maximum and minimum element of array B be X and Y respectively.
Remove X and Y from array B and insert X \mathbin{|} Y into it.

Determine the last remaining element in array B.

Here, \mathbin{\&} denotes the [Bitwise AND operation] and \mathbin{|} denotes the [Bitwise OR operation].

------ Input Format ------ 

- The first line of input contains a single integer T, denoting the number of test cases. The description of T test cases follows.
- The first line of each test case contains a single integer N, denoting the number of elements in A.
- The second line of each test case contains N space-separated integers A_{1}, A_{2}, \ldots, A_{N}.

------ Output Format ------ 

For each test case, print a single line containing one integer — the last remaining element in array B.

------ Constraints ------ 

$1 ≤ T ≤ 10^{4}$
$2 ≤ N ≤ 10^{5}$
$0 ≤ A_{i} ≤ 10^{9}$
- The sum of $N$ over all test cases does not exceed $2\cdot 10^{5}$.

----- Sample Input 1 ------ 
3
2
1 3
3
2 7 1
4
4 6 7 2
----- Sample Output 1 ------ 
1
3
6

----- explanation 1 ------ 
Test Case $1$: Array $B$ will be $[A_{1} \mathbin{\&} A_{2}] = [1 \mathbin{\&} 3] = [1]$. There is only one element in $B$ so the answer is $1$.

Test Case $2$: Array $B$ will be $[A_{1} \mathbin{\&} A_{2}, A_{1} \mathbin{\&} A_{3}, A_{2} \mathbin{\&} A_{3}] = [2 \mathbin{\&} 7, 2 \mathbin{\&} 1, 7 \mathbin{\&} 1] = [2, 0, 1]$.

Then, we do the following operations on $B$:
1. Remove $2$ and $0$ from $B$ and insert $2\mathbin{|} 0 = 2$ into it. Now, $B = [1, 2]$.
2. Remove $2$ and $1$ from $B$ and insert $2\mathbin{|} 1 = 3$ into it. Now, $B = [3]$.

The last remaining element is thus $3$.
