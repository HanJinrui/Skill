Read problems statements in [Mandarin Chinese], [Russian], [Vietnamese] and [Bengali] as well. 

Given an array A of N non-negative integers, you can choose any non-negative integer X and replace every element A_{i} with (A_{i}\oplus X) Here, \oplus denotes the [bitwise XOR operation].

Using the above operation exactly once, your goal is to minimize the bitwise OR of the new array. In other words, find X such that (A_{1}\oplus X)\lor \cdots \lor (A_{N} \oplus X) is minimized, where \lor denotes the [bitwise OR operation].

Find the value of X and the minimum possible bitwise OR of the new array.

------ Input Format ------ 

- The first line contains a single integer T - the number of test cases. Then T test cases follow.
- The first line of each test case contains a single integer N - the length of the array.
- The next line contains N integers A_{1},\ldots, A_{N}.

------ Output Format ------ 

For each test case, print two integers: X and the minimum possible bitwise OR of the new array.

If there are multiple values of X that achieve the minimum bitwise OR, print any of them.

------ Constraints ------ 

$1 ≤ T ≤ 5000$
$ 1 ≤ N ≤ 100 $
$ 0 ≤  A_{i} ≤ 10^{9} $

----- Sample Input 1 ------ 
1
2
4 6
----- Sample Output 1 ------ 
6 2
----- explanation 1 ------ 
Here, if we take $X=6$, then our expression would become $(4\oplus 6) \lor (6\oplus 6) = 2\lor 0 = 2$, which is the minimum possible.
