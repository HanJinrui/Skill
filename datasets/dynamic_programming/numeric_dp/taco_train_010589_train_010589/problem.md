A Lucas Number is a number which is represented by the following recurrence
L_{n} = L_{n-1} + L_{n-2} for n>1
L_{0} = 2
L_{1} = 1
Given a number N, find the N^{th} lucas number.
Note: Since the output may be very large calculate the answer modulus 10^9+7.
Example 1:
Input:
N = 5
Output: 11
Explanation: L_{3} + L_{4} = L5
L_{3 }= 4 and L_{4} = 7
Ã¢â¬â¹Example 2:
Input: 
N = 7
Output: 29
Explanation: L_{5} + L_{6} = L_{7}
L_{5}_{ }= 11 and L_{6} = 18
Your Task:
You don't need to read input or print anything. Your task is to complete the function lucas() which takes integer N  as input parameter and return N^{th}  Lucas number.
Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)
Constraints:
1 <= N <= 10^{6}

Starter code:
```python
#User function Template for python3



class Solution:

    def lucas(self, n):

        # code here
```
