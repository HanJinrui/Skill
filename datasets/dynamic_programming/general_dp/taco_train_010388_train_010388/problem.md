Ma5termind is crazy about Action Games. He just bought a new one and got down to play it. Ma5termind usually finishes all the levels of a game very fast. But, This time however he got stuck at the very first level of this new game. Can you help him play this game.  

To finish the game, Ma5termind has to cross $N$ levels. At each level of the game, Ma5termind has to face $\mbox{M}$ enemies. Each enemy has its associated power $\mbox{P}$ and some number of bullets $\mbox{B}$. To knock down an enemy, Ma5termind needs to shoot him with one or multiple bullets whose collective count is equal to the power of the enemy. If Ma5termind manages to knock down any one enemy at a level, the rest of them run away and the level is cleared.   

Here comes the challenging part of the game. 

Ma5termind acquires all the bullets of an enemy once he has knocked him down. Ma5termind can use the bullets acquired after killing an enemy at $i^{\mbox{th}}$ level only till the $(i+1)^{th}$ level.  

However, the bullets Ma5termind carried before the start of the game can be taken forward and can be used to kill more enemies.  

Now, Ma5termind has to guess the minimum number of bullets he must have before the start of the game so that he clears all the $N$ levels successfully.  

NOTE  

Bullets carried before the start of the game can be used to kill an enemy at any level.  
One bullet decreases the power of an enemy by 1 Unit.  
For better understanding of the problem look at the sample testcases.  

Input Format

First line of input contains a single integer $\mathbf{T}$ denoting the number of test cases. 

First line of each test case contains two space separated integers $N$ and $\mbox{M}$ denoting the number of levels and number of enemies at each level respectively. 

Each of next $N$ lines of a test case contain $\mbox{M}$ space separated integers, where $j^{th}$ integer in the $i^{\mbox{th}}$ line denotes the power $\mbox{P}$ of $j^{th}$ enemy on the $i^{\mbox{th}}$ level. 

Each of the next $N$ lines of a test case contains $\mbox{M}$ space separated integers, where $j^{th}$ integer in the $i^{\mbox{th}}$ line denotes the number of bullets $\mbox{B}$ $j^{th}$ enemy of $i^{\mbox{th}}$ level has.  

Constraints 

$1\leq T\leq100$ 

$1\leq N\leq100$ 

$1\leq M\leq5\times10^5$ 

$1\leq P,B\leq1000$ 

For each test file, sum of $N\times M$ over all the test cases does not exceed $5\times10^5$.   

Output Format

For each test case, print the required answer.  

Sample Input
2
3 3
3 2 1 
1 2 3
3 2 1
1 2 3
3 2 1
1 2 3
3 3 
3 2 5 
8 9 1 
4 7 6 
1 1 1 
1 1 1 
1 1 1 

Sample Output
1
5   

Explanation

For the First test case , Ma5termind kills the enemy in the following order:

Ma5termind kills the $3^{rd}$ enemy at the $1^{st}$ level, takes all his bullets and moves to the next level.
Ma5termind kills the $1^{st}$ enemy at the $2^{nd}$ level, takes all his bullets and moves to the next level.
Ma5termind kills the $1^{st}$ enemy at the $3^{rd}$ level, takes all his bullets and moves to the next level.

So this way Ma5termind can successfully finish this game with only $\mbox{I}$ bullet in hand before the start of the game.

For the second test case , Ma5termind kills the enemy in the following order:

Ma5termind kills the $2^{nd}$ enemy at the $1^{st}$ level, takes all his bullets and moves to the next level.
Ma5termind kills the $3^{rd}$ enemy at the $2^{nd}$ level, takes all his bullets and moves to the next level.
Ma5termind kills the $1^{st}$ enemy at the $3^{rd}$ level, takes all his bullets and moves to the next level.

So this way Ma5termind can successfully finish this game with only $5$ bullet in hand before the start of the game.

NOTE: 

There can be more than one way of getting the optimal answer but that does not matter in our case, because we need to answer the minimum number of bullets required.
