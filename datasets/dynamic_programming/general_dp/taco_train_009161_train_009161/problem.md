Given an array A of N positive integers. The task is to count the number of Arithmetic Progression subsequence in the array.
Note: Empty sequence or single element sequence is Arithmetic Progression. 
Example 1:
Input : 
N = 3
A[] = { 1, 2, 3 }
Output : 
8
Explanation:
Arithmetic Progression subsequence from the 
given array are: {}, { 1 }, { 2 }, { 3 }, { 1, 2 },
{ 2, 3 }, { 1, 3 }, { 1, 2, 3 }.
Example 2:
Input :
N = 3
A[] = { 10, 20, 30,} 
Output :
8
Explanation: 
Arithmetic Progression subsequence 
from the given array are: {}, { 10 }, 
{ 20 }, { 30 }, { 10, 20 }, { 20, 30 }, 
{ 10, 30 }, { 10, 20, 30 }.
Your Task:
You don't need to read input or print anything. Your task is to complete the function count() which takes an integer N and an array A as input parameters and returns the total count of AP sub-sequences in the array.
 
Expected Time Complexity: O(N * (Minimum value in A - Maximum Value in A)) 
Expected Space Complexity: O(N)
Constraints:
1<= N <=100
1<= A[i] <=100

Starter code:
```python
#User function Template for python3

class Solution:
    def count(self,N,A):
        # code here
```
