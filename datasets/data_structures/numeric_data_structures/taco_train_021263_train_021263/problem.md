Given a set of n numbers. The task is to count all the subsets of the given set which only have even numbers and all are distinct.
Note: By the property of sets, if two subsets have the same set of elements then they are considered as one. For example: [2, 4, 8] and [4, 2, 8] are considered to be the same.
 
Example 1:
Input : 
n = 8
a[] = {4, 2, 1, 9, 2, 6, 5, 3}
Output : 
7
Explanation:
The subsets are:
[4], [2], [6], [4, 2],
[2, 6], [4, 6], [4, 2, 6]
 
Example 2:
Input : 
n = 13
a[] = {10, 3, 4, 2, 4, 20, 10, 6, 8, 14, 2, 6, 9}
Output : 
127
Your Task:  
You don't need to read input or print anything. Your task is to complete the function countSubsets() which takes the array a[] and its size n as inputs and returns the Count of possible subsets.
 
Expected Time Complexity: O(n)
Expected Auxiliary Space: O(n)
 
Constraints:
1<=n<=10^{5}
1<=a[i]<=10^{3}
It is Guaranteed that answers will fit in 64-bits.

Starter code:
```python
#User function Template for python3



def countSubsets( a, n):

    # code here
```
