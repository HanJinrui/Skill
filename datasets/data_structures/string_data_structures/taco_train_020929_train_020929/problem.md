Given an array. Calculate the sum of lengths of contiguous subarrays having all distinct elements.
 
Example 1:
Input:
N=3
arr[] = { 1,2,3 }
Output: 10
Explanation: 
{1, 2, 3} is a subarray of length 3 with 
distinct elements. Total length of length
three = 3. {1, 2}, {2, 3} are 2 subarray 
of length 2 with distinct elements. Total 
length of lengths two = 2 + 2 = 4
{1}, {2}, {3} are 3 subarrays of length 1
with distinct element. Total lengths of 
length one = 1 + 1 + 1 = 3
Sum of lengths = 3 + 4 + 3 = 10
Example 2:
Input:
N=1
arr[] = { 1 }
Output: 1
Explanation: 
{1} is the only subarray with distinct 
elements of length 1.  
Your Task:
You don't need to read input or print anything. Your task is to complete the function sumoflength() that takes array arr and integer N as input parameters and returns the sum of lengths of contiguous subarrays having all distinct elements.
Expected Time Complexity: O(N).
Expected Auxiliary Space: O(N).
 
Constraints:
1 ≤ N ≤ 10^{6}

Starter code:
```python
#User function Template for python3



class Solution:

    def sumoflength(self,arr,n):
```
