Alice and Bob are playing the game of Nim with $n$ piles of stones with sizes $p_0,p_1,\ldots,p_{n-1}$. If Alice plays first, she loses if and only if the 'xor sum' (or 'Nim sum') of the piles is zero, i.e., $p_0\oplus p_1\oplus...\oplus p_{n-1}=0$.

Since Bob already knows who will win (assuming optimal play), he decides to cheat by removing some stones in some piles before the game starts. However, to reduce the risk of suspicion, he must keep at least one pile unchanged. Your task is to count the number of ways Bob can remove the stones to force Alice into losing the game. Since the number can be very large, output the number of ways modulo $10^9+7$. Assume that both players will try to optimize their strategy and try to win the game.

Input Format

The first line of the input contains an integer $n$ denoting the number of piles. The next line contains $n$ space-separated integers $p_0,p_1,\ldots,p_{n-1}$ indicating the sizes of the stone piles.

Constraints

$3\leq n\leq100$  
$0<p[i]<10^9$  

Output Format

Print a single integer denoting the number of ways Bob can force Alice to lose the game, modulo $10^9+7$.  

Sample Input 0
3
1 2 3

Sample Output 0
4

Explanation 0

The answer is $4$. The four possible resulting lists of piles is:

$[0,2,2]$ 
$[1,0,1]$ 
$[1,1,0]$ 
$[1,2,3]$  

Note that $[0,1,1]$ is not allowed since he must keep one pile unchanged.

Sample Input 1
10
10 10 1 1 1 1 1 10 10 10

Sample Output 1
321616
