Given a circle of radius R, divide it into N pieces such that every piece is 1/Mth of the original circle, where N and M are positive non-zero integers and M>=N. Find the arc length of the piece of the circle that is left over after the distribution.
Example 1:
Input:
R=7.50
N=4
M=7
Output:
20.19
Explanation:
3/7th of the circle is left which equals 
20.19 arc length.
Example 2:
Input:
R=6.66
N=3
M=4
Output:
10.46
Explanation:
1/4th of the circle is left which equals 
10.46 of arc length.
Your Task:
You don't need to read input or print anything. Your task is to complete the function remainingCircle() which takes R, N, M as input parameters and returns the arc length of the portion of the circle left after removing N portions of size 1/Mth each.
Expected Time Complexity:O(1)
Expected Auxillary Space:O(1)
Constraints:
1<=R<=1000.0
1<=N<=M<=1000
Pi=3.14

Starter code:
```python
#User function Template for python3

class Solution:
    def remainingCircle(self,R,N,M):
        #code here
```
