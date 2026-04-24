Given an array A containing N integers.Find out how many elements should be added such that all elements between the maximum and minimum of the array is present in the array.
Example 1:
Input:
N=5
A=[205,173,102,324,957]
Output:
851
Explanation:
The maximum and minimum of given 
array is 957 and 102 respectively.We need 
to add 854 elements out of which
3 are already present.So answer is 851.
Example 2:
Input:
N=1
A=[545]
Output:
0
Explanation:
We don't need to add any element
to the array.
Your Task:
You don't need to read input or print anything. Your Task is to complete the function countElements() which takes an integer N and an array A of size N and returns the number of elements needed to be added to the array so, that all elements between the minimum and maximum of the array are present.
Expected Time Complexity:O(N)
Expected Auxillary Space:O(10^{5})
Constraints:
1<=N,A[i]<=10^{5}

Starter code:
```python
#User function Template for python3

class Solution:
    def countElements(self,N,A):
        #code here
```
