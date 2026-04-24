Given an sequence from 1 to N and also given an array arr[] of size N. Basically the array is the permutation of 1 to N which determinds that the element from i^{th} position should move to the j^{th} position. Now the task is to find the minimum number of operations such that each array element is present at its original positions.
(For more understanding please go through the examples)
Note: the answer can be large, so return the answer modulo 10^9+7.
Example 1:
Input: N = 3, arr[] = {1,2,3}
Output: 1
Explanation: 
Given special arrangement arr[]: 
1 2 3
Given sequence 
1 2 3
so 1 should go 1^{th} position, 2 should
go 2^{nd} position and 3 should go 3^{rd}
position. So the minimum number of operation
needed is 1.
Example 2:
Input: N = 5, arr[] = {2,3,1,5,4}
Output: 6
Explanation:
Given special arrangement arr[]:
2 3 1 5 4
Given sequence is:
1 2 3 4 5
so, here we explained one step,
1 should go to 2^{nd} position, 2 should go 
3^{rd} position, 3 should go 1^{st} position, 4 
should go 5^{th} and 5 should go 4^{th} position. 
these are the required. So after 1st operation
new sqquence will look like 
3 1 2 5 4.
Here we explained the complete operations.
operations for the array
0. 1 2 3 4 5
1. 3 1 2 5 4
2. 2 3 1 4 5
3. 1 2 3 5 4
4. 3 1 2 4 5
5. 2 3 1 5 4
6. 1 2 3 4 5.
So after 6th operations the 
array rearrange itself to 
its original positions.
Your Task:
You don't need to read or print anything. Your task is to complete the function rearrange_array() which take arr[] of size N as input parameter and returns an integer which denotes the minimum number of operations needed.
 
Expected Time Complexity: O(N)
Expected Space Complexity: O(1)
 
Constraints:
1 <= N <= 10^{5}

Starter code:
```python
#User function Template for python3



class Solution:

    def rearrangeArray(self,n,arr):

        #code here
```
