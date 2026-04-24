Geek wants to distribute M balls among N children. His nemesis Keeg wants to disrupt his plan and removes P balls from Geek's bag. The minimum number of balls required to make each child happy are given in an array arr[]. Find the number of ways Geek can distribute the remaining balls so that each is happy. 
Example 1:
Input: 
m = 13, n = 4, p = 5
arr = {2, 3, 1, 3}
Output: -1
Explaination: Number of balls left is 
m-p = 8. Minimum 9 balls are required to 
make everyone happy. So the task is not 
possible and the answer is -1.
Example 2:
Input: 
m = 30, n = 10, p = 14
arr = {2, 2, 1, 1, 1, 2, 2, 3, 1, 1}
Output: 1
Explaination: At least 16 balls are required 
to make the children happy. 16 balls are left. 
So there is only one way to make them happy.
Your Task:
You do not need to read input or print anything. Your task is to complete the function countWays() which takes m, n, p and arr as input parameters and returns the  number of possible ways to distribute the balls. Return the answer modulo 10^{9} + 7. If there is no way of making everyone happy, return -1.
Expected Time Complexity: O(m*n)
Expected Auxiliary Space: O(n)
Constraints:
1 ≤ m, p ≤ 1000
1 ≤ n ≤ 100
1 < arr[i] < 10

Starter code:
```python
#User function Template for python3



class Solution:

    def countWays(self, m, n, p, arr):

        # code here
```
