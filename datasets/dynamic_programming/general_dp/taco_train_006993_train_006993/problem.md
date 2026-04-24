Samu is playing a shooting game in  play station. There are two apples to aim in this shooting game. Hitting first apple will provide her X points and hitting second apple will provide her Y points. And if she misses the apple she chose to hit, she wont get any point.

Now she is having N coins and each shoot will cost her 1 coin and she needs to score at least W points to win the game.

Samu don't like to loose at any cost. At each turn, she has two choices. The choices include:-
Hitting first apple with probability P1 percent. However, she
   might miss it with probability (1-P1) percentage.
Hitting second apple with probability P2 percent. However, she
   might miss it with probability (1-P2) percentage.

She would like to know what is the maximal expected probability(as a percentage b/w 0 and 100) of winning the shooting game.

Input Format: 
First line contains the number of test cases T. 
Each test case consists of six space separated integers of the form X Y N W P1 P2 as described in the statement.

Output Format: 
For each test case, print the result as described above in a separate line.

Note:
Choosing to hit any apple is entirely her choice. Both are independent events meaning P1 + P2 may/may not exceed 100.
Output must contain 6 digits after decimal.

Constraints: 
1 ≤ T ≤ 10
1 ≤ X,Y ≤ 10
1 ≤ N,W ≤ 10^3
0 ≤ P1,P2 ≤ 100

SAMPLE INPUT
1
2 3 2 5 50 25

SAMPLE OUTPUT
12.500000

Explanation

Samu is getting 2 points from shooting first apple and 3 points from shooting second Apple.

She had 2 chances to shoot and she need to score atleast 5 points so anyhow she need to shoot Apple 1 in one shoot and Apple 2 in another shoot , if she wants to win.

The maximum probability of winning is 0.5 * 0.25 = 0.125 = 12.5%
