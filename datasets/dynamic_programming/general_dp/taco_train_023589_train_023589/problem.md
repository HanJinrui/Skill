Let's consider a permutation P = {$p_{1}$,$ p_{2}$, ..., $p_{N}$} of the set of N = {1, 2, 3, ..., N} elements .  

P is called a magic set if it satisfies both of the following constraints:  

Given a set of K integers, the elements in positions $a_{1}$, $a_{2}$, ..., $a_{K}$ are less than their adjacent elements, i.e., $p_{ai-1} > p_{ai} < p_{ai+1}$
Given a set of L integers, elements in positions $b_{1}$, $b_{2}$, ..., $b_{L}$ are  greater than their adjacent elements, i.e., $p_{bi-1} < p_{bi} > p_{bi+1}$

How many such magic sets are there?

Input Format 

The first line of input contains three integers N, K, L separated by a single space. 

The second line contains K integers, $a_{1}$, $a_{2$}, ... $a_{K}$ each separated by single space. 

the third line contains L integers, $b_{1}$, $b_{2}$, ... $b_{L}$ each separated by single space. 

Output Format 

Output the answer modulo 1000000007 (10^{9}+7).

Constraints 

3 <= N <= 5000 

1 <= K, L <= 5000 

2 <= $a_{i}$, $b_{j}$ <= N-1, where i ∈ [1, K] AND j ∈ [1, L]  

Sample Input #00  

4 1 1
2
3

Sample Output #00  

5

Explanation #00

Here, N = 4 $a_{1}$ = 2 and $b_{1}$ = 3. The 5 permutations of {1,2,3,4} that satisfy the condition are 

2 1 4 3
3 2 4 1
4 2 3 1
3 1 4 2
4 1 3 2

Sample Input #01

10 2 2
2 4
3 9

Sample Output #01

161280
