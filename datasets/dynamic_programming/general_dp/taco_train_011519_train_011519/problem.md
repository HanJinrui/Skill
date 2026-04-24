Given three numbers N, X, and Y. Geek and his friend playing a coin game. In the beginning, there are N coins. In each move, a player can pick X, Y, or 1 coin. Geek always starts the game. The player who picks the last coin wins the game. The task is to check whether Geek will win the game or not if both are playing optimally.
Example 1:
Input: N = 5, X = 3, Y = 4
Output: 1
Explanation: There are 5 coins, every 
player can pick 1 or 3 or 4 coins on 
his/her turn. Geek can win by picking 
3 coins in first chance. Now 2 coins 
will be left so his friend will pick 
one coin and now Geek can win by 
picking the last coin.
Example 2:
Input: N = 2, X = 3, Y = 4
Output: 0
Explanation: Geek picks 1 and then 
his friend picks 1.
Your Task:  
You don't need to read input or print anything. Complete the function findWinner() which takes N, X, and Y as input parameters and returns 1 if Geek can win otherwise 0.
Expected Time Complexity: O(|N|)
Expected Auxiliary Space: O(|N|)
Constraints:
1 ≤ |N| ≤ 10^{6}

Starter code:
```python
#User function Template for python3

class Solution:

	def findWinner(self, N,X,Y):

		# code here
```
