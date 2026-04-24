Given an array arr[] of size n>3, the task is to check whether the given array can be arranged in the form of a Left or Right positioned array?
Left or Right Positioned Array means each element in the array is equal to the number of elements to its left or number of elements to its right.
Note: 1 represents true and 0 represents false.
 
Example 1:
Input  : 
arr[] = {1, 3, 3, 2}
Output : 
1
Explanation :
This array has one such arrangement {3, 1, 2, 3}.
In this arrangement, first element '3' indicates
that three numbers are after it, the 2nd element
'1' indicates that one number is before it, the
3rd element '2' indicates that two elements are
before it.
 
Example 2:
Input : 
arr[] = {1, 6, 5, 4, 3, 2, 1}
Output :
0
Explanation :
No such arrangement is possible
 
Example 3:
Input : 
arr[] = {2, 0, 1, 3}
Output: 
1
Explanation :
Possible arrangement is {0, 1, 2, 3}
 
Example 4:
Input : 
arr[] = {2, 1, 5, 2, 1, 5}
Output : 
"1"
Explanation :
Possible arrangement is {5, 1, 2, 2, 1, 5}
Your Task:
You don't need to print anything, printing is done by the driver code. You have to complete the function leftRight() which takes the array arr[] and its size N as inputs and returns True if the array can be arranged to form left or right positioned array, else False as the answer.
 
Expected Time Complexity: O(N)
Expected Auxiliary Space: O(N)
Constraints:
4 ≤ N ≤ 100000
0 ≤ arr[i] ≤ 1000

Starter code:
```python
#User function Template for python3

class Solution:
    def leftRight(self, arr, n):
        # Your code goes here
```
