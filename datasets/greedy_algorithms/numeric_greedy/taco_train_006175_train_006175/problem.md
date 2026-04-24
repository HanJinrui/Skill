A spider present at the bottom of the well of height H, needs to get out of it. The walls of the well are very slippery. In each step, it climbs U metres and slips down D metres. If in the last step, the spider gets out of the well by climbing U metres, it does not slip back. Find the number of steps the spider takes.
Example 1:
Input: 
H = 200, U = 50, D = 1
Output: 5
Explaination: 
First Step: 50 -1 = 49 
Second Step: 49 + 50 - 1 = 98 
Third Step: 98 + 50 - 1 = 147 
Fouth Step: 147 + 50 - 1 = 196
Fifth Step: Reach beyond H.
Example 2:
Input: 
H = 100, U = 5, D = 3
Output: 49
Explanation:
A single step covers (U-D=2) in each step. 
You can cover 96 in 48 steps. In the 49th 
step increment by 5 and don't decrement by 3.
Example 3:
Input:
H = 10, U = 4, D = 1
Output: 4
Explaination:
First Step: 4 - 1 = 3
Second Step: 3 + 4 - 1 = 6 
Third Step: 6 + 4 - 1 = 9 
Fourth Step: 9+4 = 13 > 10
 
Your Task:
You do not need to read input or print anything. Your task is to complete the function minStep() which takes H, U and D as input parameters and returns the steps required to go beyond H.
Expected Time Complexity: O(1)
Expected Auxiliary Space: O(1)
Constraints:
50 ≤ H ≤ 1000
1 ≤ D < U ≤ 100

Starter code:
```python
#User function Template for python3



class Solution:

    def minStep(self, H, U, D):

        # code here
```
