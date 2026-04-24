Given an array of integers, check whether there is a subsequence with odd sum and if yes, then finding the maximum odd sum. If no subsequence contains odd sum, print -1.
Example 1:
Input:
N=4
arr[] = {4, -3, 3, -5}
Output: 7
Explanation:
The subsequence with maximum odd
sum is 4 + 3 = 7
Example 2:
Input:
N=5
arr[] = {2, 5, -4, 3, -1}
Output: 9
Explanation:
The subsequence with maximum odd 
sum is 2 + 5 + 3 + -1 = 9
Your Task:
Since, this is a function problem. You don't need to take any input, as it is already accomplished by the driver code. You just need to complete the function findMaxOddSubarraySum() that takes array arr and integer N as parameters and returns the desired value.
 
Expected Time Complexity: O(N).
Expected Auxiliary Space: O(1).
Constraints:
2 ≤ N ≤ 10^{7}
-10^{3} <= arr[i] <= 10^{3}

Starter code:
```python
#User function Template for python3


class Solution:
    def findMaxOddSubarraySum(self,arr,n):
        #code here.
```
