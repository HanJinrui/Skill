There are N office cubicles placed in a straight line, each with a bright bulb. Each light bulb can brighten K rooms on either side of it (also the one in which the light bulb itself is), but all the cubicles don't have a bulb. You are given an array A which gives the information about the location of the bulbs. If A[i] is equal to 1, then the cubicle has a light bulb, else if A[i] is 0, then the cubicle doesn't have a bulb. You need to find out whether all the cubicles are bright or not.
Example 1:
Input: N = 4, K = 3
A = {0, 1, 0, 1}
Output: 1
Explaination: The first cubicle can be 
brightened by 2nd cubicle. The third 
cubicle can be brightened by 4th cubicle.
Example 2:
Input: N = 7, K = 2
A = {1, 0, 0, 0, 0, 0, 1}
Output: 0
Explaination: The fourth cubicle cannot be 
brightened in any way.
Your Task:
You do not need to read input or print anything. Your task is to complete the function isBrightened() which takes N, K and A as input parameters and returns 1 if all the cubicles can be brightened. Otherwise, returns 0.
Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)
Constraints:
1 ≤ N ≤ 10^{4}
1 ≤ K ≤ 20
0 ≤ A[i] ≤ 1

Starter code:
```python
#User function Template for python3

class Solution:
    def isBrightened(self, N, K, A):
        # code here
```
