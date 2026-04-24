You are at the side of a river. You are given a m litre jug and a n litre jug . Both the jugs are initially empty. The jugs dont have markings to allow measuring smaller quantities. You have to use the jugs to measure d litres of water . Determine the minimum no of operations to be performed to obtain d litres of water in one of the jugs.
The operations you can perform are:
	Empty a Jug
	Fill a Jug
	Pour water from one jug to the other until one of the jugs is either empty or full.
 
Example 1:
Input: m = 3, n = 5, d = 4
Output: 6
Explanation: Operations are as follow-
1. Fill up the 5 litre jug.
2. Then fill up the 3 litre jug using 5 litre
   jug. Now 5 litre jug contains 2 litre water.
3. Empty the 3 litre jug.
4. Now pour the 2 litre of water from 5 litre 
   jug to 3 litre jug.
5. Now 3 litre jug contains 2 litre of water 
   and 5 litre jug is empty. Now fill up the 
   5 litre jug.
6. Now fill one litre of water from 5 litre jug 
   to 3 litre jug. Now we have 4 litre water in 
   5 litre jug.
Example 2:
Input: m = 8, n = 56, d = 46
Output: -1
Explanation: Not possible to fill any one of 
the jug with 46 litre of water.
 
Your Task:
You don't need to read or print anything. Your task is to complete the function minSteps() which takes m, n and d ans input parameter and returns the minimum number of operation to fill d litre of water in any of the two jug.
 
Expected Time Comeplxity: O(d)
Expected Space Complexity: O(1)
Constraints:
1 ≤ n,m ≤ 100
1 ≤ d ≤ 100

Starter code:
```python
#User function Template for python3



class Solution:

	def minSteps(self, m, n, d):

		# Code here
```
