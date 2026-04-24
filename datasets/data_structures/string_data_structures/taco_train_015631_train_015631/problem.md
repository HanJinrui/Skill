CodeMart is a shopping platform and it is distributing gift vouchers to its esteemed users. The voucher can be redeemed by providing a fixed amount of shopping credits to the platform. One credit is sent by a user to the platform by doing one occurance in CodeMart. Since there is a huge rush of people you are required to manage the users on the basis of first come first serve. The user which came first and has exactly k occurrences at last is given the voucher first. You are given an array arr[ ] with the id's of N users in chronological order of their occurances . You are required to print the id of the user which will be given the voucher first. If no such user meets the condition print "-1".
Example 1:
Input:
N = 7 
K = 2
arr[] = {1, 7, 4, 3, 4, 8, 7} 
Output: 7
Explanation: Both 7 and 4 occur 2 times.
But 7 is the first that occurs 2 times.  
Example 2:
Input:
N = 6 
K = 1 
arr[] = {4, 1, 6, 1, 6, 4} 
Output: -1 
Explanation: No one occurs exactly 1 time.
Your Task:
This is a function problem. You don't need to take any input, as it is already accomplished by the driver code. You just need to complete the function firstElement() that takes array arr, integer n and integer k as input parameters and returns the required answer.
Expected Time Complexity: O(N).
Expected Auxiliary Space: O(max(arr[i])).
Constraints:
1 ≤ N ≤ 10^{4}
1 ≤ arr[i] ≤ 10^{3}

Starter code:
```python
#User function Template for python3

class Solution:
    def firstElement(self, arr, n, k):
```
