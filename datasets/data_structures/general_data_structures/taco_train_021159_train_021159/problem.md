Given an array of N integers arr[ ], the task is to count the minimum number of operations to equalize the array i.e. to make all array elements equal.
In one operation, you can choose two elements arr[i] and arr[j] such that arr[i] > arr[j] and change them to arr[i] = arr[i] - 1 and arr[j] = arr[j] + 1.
If it is impossible to equalize the array print "-1".
Example 1:
Input:
N = 5
arr[] = {1, 3, 2, 0, 4}
Output:  3
Explanation: We can equalize the array by 
making value of all elements equal to 2. 
To achieve this we need to do minimum 3 
operations:
1. arr[0]++ and arr[1]--
2. arr[3]++ and arr[4]--
3. arr[3]++ and arr[4]--
Example 2:
Input:
N = 3
arr[] = {1, 7, 1}
Output:  4
Your Task:
This is a function problem. You don't need to take any input, as it is already accomplished by the driver code. You just need to complete the function minOperations() that takes array arr[ ] and integer N as input parameters and returns the required answer.
Note - return -1, if it is not possible to equalize the array.
Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1).
Constraints:
1 ≤ N ≤ 10^{5}

Starter code:
```python
#User function Template for python3



class Solution:
    def findDifference(self,arr,N):
        #Code here
```
