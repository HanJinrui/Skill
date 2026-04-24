You are a traveler, lost in a jungle. Backtrack your steps and find the starting point. 
Currently, you are at coordinates (x,y). You are also given an array pathCoordinates [ ] where each element is a (a,b) pair. 
The i^{th} pair (a,b), in the array, denotes that in the i^{th} move you moved your X co-ordinate by a and Y co-ordinate by b. 
if X,Y coordinates in an instant are (c,d) then your next move will be to ( c+a, d+b). 
Example 1:
Input: x = 2, y = 2, 
pathCoordinates = {{1,0},{0,1},{1,1}}
Output: {0,0}
Explaination:
{0,0} was the starting point of the traveler.
At first he changed his X co-ordinate by 1 and
Y co-ordinate by 0.
{0,0} -> {1,0}
After that he changed his X co-ordinate by 0 and
Y co-ordinate by 1.
{0,0} -> {1,0} -> {1,1}
And finally, he changed his X co-ordinate by 1 and
Y co-ordinate by 1.
{0,0} -> {1,0} -> {1,1} -> {2,2}
Example 2:
Input: x = 1, y = 2,
pathCoordinates = {{1,1}}
Output: {0,1}
Explaination:
The route followed by the traveller is
{0,1} -> {1,2}.
 
Your Task:
You don't need to read or print anything. Your task is to complete the function findStartingPoint() which takes x, y, and pathCoordinates as input parameters and returns a list containing the starting point.
 
Expected Time Compelxity: O(n) where n = length of pathCoordinates.
Expected Space Complexity: O(1)
 
Constraints:
1 <= n <= 10^{3}

Starter code:
```python
#User function Template for python3

class Solution:
	def findStartingPoint(self, x, y, pathCoordinates):
		#Code here
```
