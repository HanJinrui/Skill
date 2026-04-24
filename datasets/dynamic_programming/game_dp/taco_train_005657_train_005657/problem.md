See Russian Translation

Adam and Bob are playing a game. The game is parameterized by the three integers a,b,c. They start out with the integer 1, with Adam going first. Suppose the current integer is S. On a player's turn, he may change the current integer to any integer between a×S and b×S, inclusive. The first player to make the current integer be at least as large as c is declared the winner. Given that Adam and Bob play optimally, return the winner of the game. 

Input format:

The first line of input will contain an integer T, denoting the number of test cases.
Each test case will be given on one line, which contains 3 integers, a,b,c

Output format:

Print the name of the person who will win for each test case on a separate line.

Constraints:

For all subtasks
1 ≤ T ≤ 10^4

30 pts:
2 ≤ a ≤ b ≤ 10
2 ≤ c ≤ 20

60 pts:
2 ≤ a ≤ b ≤ 50
2 ≤ c ≤ 1,000

10 pts:
2 ≤ a ≤ b ≤ 100
2 ≤ c ≤ 10^18

SAMPLE INPUT
6
2 2 10
2 10 20
10 10 3
2 3 100
22 40 500
2 100 1000000000000000000

SAMPLE OUTPUT
Bob
Bob
Adam
Adam
Bob
Adam

Explanation

Note, the fourth and fifth case does not fit within the limits of the first subtask, and the sixth case does not fit within the limits of the first or second subtask. 

In the first case, a player turn consists of multiplying the current integer by 2. Thus, Adam turns the number to 2, Bob makes it 4, Adam makes it 8, then Bob makes it 16. This is at least 10, so Bob is the winner.

In the second case, no matter what Adam does on the very first turn, Bob can just multiply the integer by 10 to make it exceed 20. So, Bob can always win.
