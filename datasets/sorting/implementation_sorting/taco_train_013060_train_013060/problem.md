Today Omar has assignment problems from his math professor. Yes, Omar has infinite number of questions that he must solve today. The first problem went something like this.  

Given N integers in the form of A_i where 1 ≤ i ≤ N, Omar wants to make each number A_i in the N numbers equal to M. To convert a number A_i to M, it will cost |M - A_i| units. The problem asks to find out the minimum cost to convert all the N numbers to M, so you should choose the best M to get the minimum cost. 

Omar gets bored easily from these kind of questions, can you solve it for him ?

Input:

First line of the input contains an integer T denoting the number of test cases. 
First line of every test-case contains an integer N.      
Second line of every test case contains N space separated integers A_i.

Output:

For each case, print the minimum cost that Omar needs to pay to convert each A_i to M, in a separate line.   

Constraints:

1 ≤ T ≤ 10.
1 ≤ N ≤ 10 ^ 5.
1 ≤ A_i ≤ 10^{9}

SAMPLE INPUT
1
4
1 2 4 5

SAMPLE OUTPUT
6

Explanation

One of the best M's you could choose in this case is 3.   
So the answer = |1 - 3| + |2 - 3| + |4 - 3| + |5 - 3| = 6.
