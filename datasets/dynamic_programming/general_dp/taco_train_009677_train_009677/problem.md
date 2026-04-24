In a tournament, $n$ players play against each other exactly once. Each game results in exactly one player winning. There are no ties. You have been given a scorecard containing the scores of each player at the end of the tournament. The score of a player is the total number of games the player won in the tournament. However, the scores of some players might have been erased from the scorecard. How many possible scorecards are consistent with the input scorecard?

Input Format

The first line contains a single integer $\boldsymbol{\boldsymbol{t}}$ denoting the number of test cases. $\boldsymbol{\boldsymbol{t}}$ test cases follow.  

The first line of each test case contains a single integer $n$. The second line contains $n$ space-separated integers $s_1,s_2,\ldots,s_n$. $s_i$ denotes the score of the $\boldsymbol{i}$th player. If the score of the $\boldsymbol{i}$th player has been erased, it is represented by $-1$.

Constraints

$1\leq t\leq20$
$1\leq n\leq40$
$-1\leq s_i<n$

Output Format

For each test case, output a single line containing the answer for that test case modulo $10^9+7$. 

Sample Input 0
5
3
-1 -1 2
3
-1 -1 -1
4
0 1 2 3
2
1 1
4
-1 -1 -1 2

Sample Output 0
2
7
1
0
12

Explanation 0

For the first case, there are 2 scorecards possible: (0,1,2) or (1,0,2). 

For the second case, the valid scorecards are (1,1,1), (0,1,2), (0,2,1), (1,0,2), (1,2,0), (2,0,1), (2,1,0). 

For the third case, the only valid scorecard is (0,1,2,3). 

For the fourth case, there is no valid scorecard. It is not possible for both players to have score of 1. 

For the fifth case, 6-variations of {(3,1,0)[2]}, and 3 variations each of {(2,2,0)[2]} and {(2,1,1)[2]}.
