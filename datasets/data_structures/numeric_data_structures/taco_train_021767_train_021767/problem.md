Given an array Arr[] of size N. Find the number of subarrays whose sum is an even number.
Example 1:
Input:
N = 6
Arr[] = {1, 2, 2, 3, 4, 1}
Output: 9
Explanation: The array {1, 2, 2, 3, 4, 1} 
has 9 such possible subarrays. These are-
 {1, 2, 2, 3}          Sum = 8
 {1, 2, 2, 3, 4}       Sum = 12
 {2}                   Sum = 2 (At index 1)
 {2, 2}                Sum = 4
 {2, 2, 3, 4, 1}       Sum = 12
 {2}                   Sum = 2 (At index 2)
 {2, 3, 4, 1}          Sum = 10
 {3, 4, 1}             Sum = 8
 {4}                   Sum = 4
Example 2:
Input:
N = 4
Arr[] = {1, 3, 1, 1}
Output: 4
Explanation: The array {1, 3, 1, 1} 
has 4 such possible subarrays.
These are-
 {1, 3}            Sum = 4
 {1, 3, 1, 1}      Sum = 6
 {3, 1}            Sum = 4
 {1, 1}            Sum = 2
Your Task:
You don't need to read input or print anything. Your task is to complete the function countEvenSum() which takes the array of integers arr[] and its size n as input parameters and returns an integer denoting the answer.
Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)
Constraints:
1 <= N <= 10^{5}
1<= Arr[i] <=10^{9}

Starter code:
```python
#User function Template for python3



class Solution:

    def countEvenSum(self, arr, n):

        # code here
```
