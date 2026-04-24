Read problem statements in [Russian], [Mandarin Chinese], [Bengali], and [Vietnamese] as well.

In a season, each player has three statistics: runs, wickets, and catches. Given the season stats of two players A and B, denoted by R, W, and C respectively, the person who is better than the other in the most statistics is regarded as the better overall player. Tell who is better amongst A and B. It is known that in each statistic, the players have different values.

------ Input Format ------ 

- The first line contains an integer T, the number of test cases. Then the test cases follow.
- Each test case contains two lines of input.
- The first line contains three integers R_{1}, W_{1}, C_{1}, the stats for player A.
- The second line contains three integers R_{2}, W_{2}, C_{2}, the stats for player B.

------ Output Format ------ 

For each test case, output in a single line "A" (without quotes) if player A is better than player B and "B" (without quotes) otherwise.

------ Constraints ------ 

$1 ≤ T ≤ 1000$
$0 ≤ R_{1}, R_{2} ≤ 500$
$0 ≤ W_{1}, W_{2} ≤ 20$
$0 ≤ C_{1}, C_{2} ≤ 20$
$R_{1} \neq R_{2}$
$W_{1} \neq W_{2}$
$C_{1} \neq C_{2}$

------ subtasks ------ 

Subtask 1 (30 points): $1 ≤ R ≤ 10000$
Subtask 2 (70 points): $1 ≤ R ≤ 10^{9}$

----- Sample Input 1 ------ 
3
0 1 2
2 3 4
10 10 10
8 8 8
10 0 10
0 10 0
----- Sample Output 1 ------ 
B
A
A
----- explanation 1 ------ 
Test Case $1$: Player $B$ is better than $A$ in all $3$ fields.

Test Case $2$: Player $A$ is better than $B$ in all $3$ fields.

Test Case $3$: Player $A$ is better than $B$ in runs scored and number of catches.
