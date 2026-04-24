Blobo2 is in his practical exam. The teacher gave him a *permutation* A of N integers.
 
The teacher has allowed Blobo2 to make a certain type of operation on the *permutation*. In one operation, he can:
Apply left shift on the permutation. In other words, he can take the first element of the permutation and move it to the back of the permutation. 

The teacher has asked Blobo2 to find the lexicographically smallest permutation possible after applying any (possibly zero) number of given operations.

Since Blobo2 wants to impress his teacher, he decided to perform at most two swaps in addition to the allowed operation.

Find the lexicographically smallest possible permutation Blobo2 can generate after applying at most two swaps and any number of given operations.

Note:
A permutation of size N consists of all integers from 1 to N exactly once.
During a swap, Blobo2 can choose any two indices i and j (1≤ i,j≤ N) and swap A_{i} with A
_j.
A permutation X is said to be lexicographically smaller than a permutation Y if X_{i} < Y_{i}, where i is the first index where both the permutations differ.

------ Input Format ------ 

- The first line of input will contain a single integer T, denoting the number of test cases.
- The second line will contain the integer N, denoting the size of the permutation.
- The third line contains N distinct integers, the elements of the permutation A.

------ Output Format ------ 

Output the lexicographically smallest possible permutation Blobo2 can generate after applying at most two swaps and any number of given operations.

------ Constraints ------ 

$1≤ T≤ 5\cdot 10^{5}$
$1≤ N≤ 10^{5}$
$1≤ A_{i}≤ N$
$A$ is a permutation
- The sum of $N$ over all test cases won't exceed $5\cdot 10^{5}$.

----- Sample Input 1 ------ 
2
5
5 2 1 4 3
5
3 5 2 1 4

----- Sample Output 1 ------ 
1 2 3 4 5 
1 2 3 4 5

----- explanation 1 ------ 
Test case $1$: Blobo2 can perform $2$ swaps:
- For the first swap, Blobo2 can swap the first and second elements: $[\underline{5},\underline{2},1,4,3]$ $\rightarrow$ $[2,5,1,4,3]$
- For the second swap, he can swap the first and fourth elements: $[\underline{2},5,1,\underline{4},3]$ $\rightarrow$ $[4,5,1,2,3]$

Finally, Blobo2 will left shift the array two times which will lead to the lexicographically smallest permutation: $[1,2,3,4,5]$.

Test case $2$: Blobo2 can perform $2$ swaps:
- For the first swap, Blobo2 can swap the third and fifth elements: $[3,5,\underline{2},1,\underline{4}]$ $\rightarrow$ $[3,5,4,1,2]$
- For the second swap, he can swap the second and third elements: $[3,\underline{5},\underline{4},1,2]$ $\rightarrow$ $[3,4,5,1,2]$

Finally, Blobo2 will left shift the array two times which will lead to the lexicographically smallest permutation: $[1,2,3,4,5]$.
