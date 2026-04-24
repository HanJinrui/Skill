Read problems statements in Mandarin Chinese  and Russian. 
Alexandra has some distinct integer numbers a_{1},a_{2}...a_{n}.
Count number of pairs (i,j) such that:
1≤ i ≤ n
1≤ j ≤ n
a_{i} < a_{j}
 
------ Input ------ 

The first line of the input contains an integer T denoting the number of test cases. The description of T test cases follows.The first line of each test case contains a single integer n denoting the number of numbers Alexandra has. The second line contains n space-separated distinct integers a_{1}, a_{2}, ..., a_{n} denoting these numbers.
 
------ Output ------ 

For each test case, output a single line containing number of pairs for corresponding test case.
 
------ Constraints ------ 

$1 ≤ T ≤ 4$
$1 ≤ n ≤ 100000$
$0 ≤ a_{i} ≤ 10^{9}$
$All the a_{i} are distinct

----- Sample Input 1 ------ 
2
2
12 11
3
13 11 12
----- Sample Output 1 ------ 
1
3
----- explanation 1 ------ 
Case 1: Only one such pair of (i, j) indices exists: (2,1), since a2 1. 
Case 2: 3 possible pairs of indices: (2,1), (2,3), (3,1) .
