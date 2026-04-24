Read problems statements in Mandarin chinese, Russian and Vietnamese as well. 

Chef is playing a game with his brother Chefu. Before the game begins, C cards are placed on a table. Each card has a number written on it; since C can be very large, these numbers are described by two sequences A and D. Each of these sequences has length N; for each i (1 ≤ i ≤ N), D_{i} cards, each with number A_{i} written on it, are placed on the table. Therefore, C is equal to the sum of elements of D. Note that the elements of A don't have to be unique.

You are also given a sequence B with length K. The game will last for exactly K rounds numbered 1 through K. The players alternate turns — Chef plays on odd-numbered turns and his brother on even-numbered turns. In the i-th round, the current player must select B_{i} cards currently lying on the table, keep these cards on the table and discard all other cards.

Chef's goal is to maximize the sum of numbers written on cards that remain on the table after the last round, while Chefu's goal is minimize this sum. What will be the sum of numbers written on cards remaining on the table if both players play optimally?

------ Input ------ 

The first line of the input contains a single integer T denoting the number of test cases. The description of T test cases follows.
The first line of each test case contains two space-separated integers N and K.
The second line contains N space-separated integers A_{1}, A_{2}, ..., A_{N}.
The third line contains N space-separated integers D_{1}, D_{2}, ..., D_{N}.
The fourth line contains K space-separated integers B_{1}, B_{2}, ..., B_{K}.

------ Output ------ 

For each test case, print a single line containing one integer — the sum of numbers on cards that remain on the table at the end of the game.

------ Constraints ------ 

$1 ≤ T ≤ 100$
$1 ≤ N, K ≤ 100,000$
$1 ≤ sum of N over all test cases ≤ 100,000$
$1 ≤ sum of K over all test cases ≤ 100,000$
$1 ≤ A_{i}, D_{i} ≤ 1,000,000 for each valid i$
$1 ≤ B_{i} ≤ C for each valid i$
$B_{i+1} < B_{i} for each valid i$

------ Subtasks ------ 

Subtask #1 (20 points): 

$D_{i} = 1 for each valid i$
$sum of N over all test cases ≤ 1,000$
$sum of K over all test cases ≤ 1,000$

Subtask #2 (80 points): original constraints

----- Sample Input 1 ------ 
1
4 2
1 2 3 4
2 2 2 2
6 3
----- Sample Output 1 ------ 
7
----- explanation 1 ------ 
Example case 1: The cards that are on table initially are 1, 1, 2, 2, 3, 3, 4, 4 Chef in his turn should select 6 cards to keep and discard the rest, so he will keep 2, 2,
3, 3, 4, 4 after that Chefu should keep 3 cards and discard the rest, so he will keep 2, 2,
3 after that the game ends and sum of cards remained on the table is 2 + 2 + 3 = 7
