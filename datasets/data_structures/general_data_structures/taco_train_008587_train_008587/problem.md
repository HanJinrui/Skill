Given an array Arr of N positive integers, find the missing elements (if any) in the range 0 to max of Arr_{i}. 
Example 1:
Input:
N = 5
Arr[] = {62, 8, 34, 5, 332}
Output: 0-4 6-7 9-33 35-61 63-331
Explanation: Elements in the range 0-4, 6-7, 
9-33, 35-61 and 63-331 are not present.
Example 2:
Input:
N = 4
Arr[] = {13, 0, 32, 500}
Output: 1-12 14-31 33-499
Explanation: Elements in the range 1-12, 
14-31 and 33-499 are not present.
Your Task:
You don't need to read input or print anything. Your task is to complete the function findMissing() which takes the array of integers arr and its size n as input parameters and returns a string denoting the missing elements. If
there are more than one missing, collate them using hyphen (-) and separate each different range with a space. If there are no missing element then return "-1".
Expected Time Complexity: O(N)
Expected Auxiliary Space: O(N)
Constraints
1 <= N <= 10^{7}
0 <= Arr_{i} <= 10^{7}

Starter code:
```python
#User function Template for python3



class Solution:

    def printMissing(self, arr, n):

        # code here
```
