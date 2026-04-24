You are given an integer N. Construct a permutation A of length N which is attractive.

A permutation is called attractive if the [bitwise XOR] of all absolute differences of adjacent pairs of elements is equal to 0.

Formally, a permutation A = [A_{1}, A_{2}, \ldots, A_{N}] of length N is said to be attractive if:

|A_{1}-A_{2}|  \oplus |A_{2}-A_{3}| \oplus \ldots \oplus |A_{N-1} - A_{N}| = 0

where \oplus denotes the bitwise XOR operation.

Output any attractive permutation of length N. If no attractive permutation exists, print -1 instead.

Note: A permutation of length N is an array A = [A_{1}, A_{2}, \ldots, A_{N}] such that every integer from 1 to N occurs exactly once in A. For example, [1, 2, 3] and [2, 3, 1] are permutations of length 3, but [1, 2, 1], [4, 1, 2], and [2, 3, 1, 4] are not.

------ Input Format ------ 

- The first line of input contains a single integer T, denoting the number of test cases. The description of T test cases follows.
- Each test case consists of a single line of input, containing one integer N.

------ Output Format ------ 

For each test case, output on a single line an attractive permutation of N integers, or -1 if no attractive permutation exists.

------ Constraints ------ 

$1 ≤ T ≤ 1000$
$2 ≤ N ≤ 10^{5}$
- Sum of $N$ over all cases won't exceed $2 \cdot 10^{5}$.

----- Sample Input 1 ------ 
2
3
6
----- Sample Output 1 ------ 
3 2 1
5 2 3 6 4 1 

----- explanation 1 ------ 
Test Case $1$: $ |3-2| \oplus |2-1|  =  1 \oplus 1 = 0$

Note that there are other correct answers — for example, $[1, 2, 3]$ would also be accepted as correct.

Test Case $2$: $ |5-2| \oplus |2-3| \oplus |3-6| \oplus |6-4| \oplus |4-1| = 3 \oplus 1 \oplus 3 \oplus 2 \oplus 3 = 0$
