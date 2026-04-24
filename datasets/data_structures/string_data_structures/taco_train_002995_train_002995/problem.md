Alice and Bob are playing a game on a binary string S of length N.

Alice and Bob alternate turns, with Alice going first. On their turn, the current player must choose any index 1 ≤ i < |S| such that S_{i} \neq S_{i+1} and erase either S_{i} or S_{i+1} from the string. This reduces the length of S by one, and the remaining parts of S are concatenated in the same order.

The player who is unable to make a move loses.

Determine the winner if both players play optimally.

------ Input Format ------ 

- The first line of input contains a single integer T denoting the number of test cases. The description of T test cases follows.
- The first line of each test case contains a single integer N, the length of the string.
- The second line contains the binary string S of length N.

------ Output Format ------ 

For each test case output Alice if Alice wins the game, otherwise output Bob.
The output is not case-sensitive, so for example "Bob", "boB" and "Bob" are all considered equivalent.

------ Constraints ------ 

$1 ≤ T ≤ 1000$
$2 ≤ N ≤ 10^{5}$
$S$ is a binary string
- Sum of $N$ over all test cases does not exceed $2 \cdot 10^{5}$.

----- Sample Input 1 ------ 
3
4
1111
3
110
4
1010

----- Sample Output 1 ------ 
Bob
Alice
Bob
----- explanation 1 ------ 
Test Case $1$: There is no such index $i$ such that $S_{i} \neq S_{i+1}$. So, Alice does not have any move and loses, making Bob the winner.

Test Case $2$: Alice can choose $i=2$ (because $S_{2} = 1$ and $S_{3} = 0$) and remove $S_{3}$. After this move, the remaining string is "$11$". Bob now has no moves and thus loses.
