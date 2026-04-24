The RPS world championship is here. Here two players A and B play the game. You need to determine who wins.
Both players can choose moves from the set {R,P,S}.
The game is a draw if both players choose the same item. 
The winning rules of RPS are given below:
	Rock crushes scissor
	Scissor cuts paper
	Paper envelops rock
 
Example 1:
Input:
S = "RR"
Output: DRAW
Explanation: Both A and B chooses a Rock.
Hence, it's a draw.
Ã¢â¬â¹Example 2:
Input: 
S = "RS"
Output: A
Explanation: A chose a Rock whereas B chose
a Scissor. Rock crushes the Scissor and thus, 
A wins.
Your Task:
You don't need to read input or print anything. Your task is to complete the function gameResult() which takes the string S as input and returns a string denoting the answer. Return "A" if A wins, "B" if B wins and "DRAW" if it's a draw.
Expected Time Complexity: O(1).
Expected Auxiliary Space: O(1).
Constraints:
|S| = 2
S_{i} = R/S/P

Starter code:
```python
#User function Template for python3

class Solution:
    def gameResult(self, s):
        # code here
```
