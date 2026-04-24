Given an array Arr[] of N elements. Perform K right circular rotations on given ranges [L...R]. After performing these rotations, we need to find element at a given index X.
Example 1:
Input:
N = 5, X = 1, K = 2
Arr[] = {1, 2, 3, 4, 5}
Ranges[][] = {{0, 2}, {0, 3}}
Output: 3
Explanation: Rotating the elements in range 
0-2 and 0-3, we have array as 4 3 1 2 5. 
Element at first position is 3.
Example 2:
Input:
N = 3, X = 2, K = 1
Arr[] = {1, 2, 3}
Ranges[][] = {{0, 1}}
Output: 3
Your Task:
You don't need to read input or print anything. Your task is to complete the function findElement() which takes the array of integers arr, n, x, ranges and k as parameters and returns an integer denoting the answer.
Expected Time Complexity: O(K)
Expected Auxiliary Space: O(1)
Constraints:
2 <= N <= 10^{5}
1 <= Arr[i] <= 10^{5}
1 <= K <= 10^{5}
X < N
0 <= L <= R

Starter code:
```python
#User function Template for python3



class Solution:
    def findElement(self, a, n, x, ranges, k):
        # code here
```
