Given a screen containing alphabets from a-z, we can go from one character to another character using a remote. The remote contains left, right, top and bottom keys.
Remote :
Find the shortest possible path to type all characters of given string using the remote. The initial position is top left and all characters of input string should be printed in order. Find the total number of moves in such a path(Move UP, DOWN, LEFT, RIGHT). Pressing OK also accounts for one move.
Screen:
a b c d e
f g h i j
k l m n o
p q r s t
u v w x y
z
Example 1:
Input: str = "abc"
Output: 5
Explanation: Remote's position is at 'a'
initially. So 'a' -> 'b' = 1 step, 
'b'-> 'c'= 1 step. Three OK moves will also
be needed to print the three characters.
Example 2:
Input: str = "a"
Output: 1
Explanation: Remote is initially at 'a'.
 
Your Task:
You don't need to read or print anything. Your task is to complete the function FindPath() which takes the string str as input parameter and returns the minimum number of moves to cover all characters of the given string.
 
Expected Time Compelxity: O(n)
Expected Space Complexity: O(1)
 
Constraints:
1 <= |str| <= 10^{5}

Starter code:
```python
#User function Template for python3

class Solution:
	def FindPath(self, str):
		# Code here
```
