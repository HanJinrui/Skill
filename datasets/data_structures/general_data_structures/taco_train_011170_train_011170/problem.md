Given an integer array arr of size N. The Range of a subarray of arr is the difference between the largest and smaller element in the subarray.  
Return the sum of all subarray ranges of arr.
Example 1:
Input:
N = 3
arr[ ] = {1, 2, 3}
Output: 4
Explanation: The 6 subarrays of arr are the following :
{1 } , range = largest - smallest = 1 - 1 = 0 
{2 } , range = 2 - 2 = 0
{3 } , range = 3 - 3 = 0
{1, 2}, range = 2 - 1 = 1
{2, 3}, range = 3 - 2 = 1
{1, 2, 3}, range = 3 - 1 = 2
sum of all ranges is 0 + 0 + 0 + 1 + 1 + 2 = 4
 
Example 2:
Input:
N = 4
arr[ ] = {-32, 0, -2, 72}
Output: 318
 
Your Task:
You don't need to read input or print anything. Your task is to complete the function subarrayRanges() which takes the array of integers arr and N as parameters and returns a sum of all subarrays ranges of arr.
Expected Time Complexity: O(N)
Expected Auxiliary Space: O(N)
Constraints:
1 ≤ N ≤ 10^{3}
10^{-9 }≤ arr_{i  }≤ 10^{-9}

Starter code:
```python
#User function Template for python3



class Solution:

    def subarrayRanges(self, N, arr):

        # Code here
```
