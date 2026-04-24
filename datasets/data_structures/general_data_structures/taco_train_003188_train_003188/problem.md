Given an array arr[] of the size N, the task is to find a number such that when the number is processed against each array element starting from the 0th index till the (n-1)-th index under the conditions given below, it never becomes negative.
	If the number is greater than an array element, then it is increased by difference of the number and the array element.
	If the number is smaller than an array element, then it is decreased by difference of the number and the array element.
Example 1:
Input: N = 5, arr[] = {3, 4, 3, 2, 4}
Output:  4
Explanation: If we process 4 from left 
to right in given array, we get following :
When processed with 3, it becomes 5.
When processed with 5, it becomes 6
When processed with 3, it becomes 9
When processed with 2, it becomes 16
When processed with 4, it becomes 28
We always get a positive number. For all 
values lower than 4, it would become 
negative for some value of the array.
Example 2:
Input: N = 2, arr[] = {4, 4}
Output: 3
Explanation: When processed with 4, 
it becomes 2 When processed with 
next 4, it becomes 1
 
Your Task:
This is a function problem. You don't need to take any input, as it is already accomplished by the driver code. You just need to complete the function find() that takes array A and integer N as parameters and returns the smallest possible number.
 
Expected Time Complexity: O(N). 
Expected Auxiliary Space: O(1).
 
Constraints:
1 ≤ N ≤ 10^{6}

Starter code:
```python
class Solution:

    def find(self, arr, n):

        # Your code goes here
```
