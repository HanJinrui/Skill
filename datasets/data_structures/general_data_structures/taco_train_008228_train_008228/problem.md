Given an array containing n numbers. The task is to find the maximum sum bitonic subarray. A bitonic subarray is a subarray in which elements are first increasing and then decreasing. A strictly increasing or strictly decreasing subarray is also considered as bitonic subarray.
 
Example 1:
Input:
n = 7
a[] = {5, 3, 9, 2, 7, 6, 4}
Output:
19
Explanation:
All Bitonic Subarrays are as follows:
{5}, {3}, {9}, {2}, {7}, {6}, {4},
{5,3}, {3,9}, {9,2}, {2,7}, {7,6}, 
{6,4}, {3,9,2}, {2,7,6}, {7,6,4}, {2,7,6,4}.
Out of these, the one with the maximum
sum is {2,7,6,4} whose sum is 19.
 
Example 2:
Input:
n = 7
a[] = {5, 4, 3, 2, 1, 10, 6}
Output:
17
Your Task:  
You don't need to read input or print anything. Your task is to complete the function maxSumBitonicSubArr() which takes the array a[] and its size n as inputs and returns the maximum bitonic subarray sum.
 
Expected Time Complexity: O(n)
Expected Auxiliary Space: O(1)
 
Constraints:
1<=n<=10^{5}
1<=a[i]<=10^{5}

Starter code:
```python
#User function Template for python3

class Solution:
    def maxSumBitonicSubArr(self, a, n):
        #Code here
```
