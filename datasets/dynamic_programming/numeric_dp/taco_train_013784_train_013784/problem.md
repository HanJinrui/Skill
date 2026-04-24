A Padovan Sequence is a sequence which is represented by the following recurrence relation
P(N) = P(N-2) + P(N-3)
P(0) = P(1) = P(2) = 1
Given a number N, find the N^{th} number in this sequence.
Note: Since the output may be very large, compute the answer modulus 10^9+7.
Example 1:
Input:
N = 3
Output: 2
Explanation: P_{1} + P_{0} = P3
P_{1 }= 1 and P_{0} = 1
Ã¢â¬â¹Example 2:
Input: 
N = 4
Output: 2
Explanation: P_{2} + P_{1} = P_{4}
_{ }P2 = 1 and P_{1} = 1
Your Task:
You don't need to read input or print anything. Your task is to complete the function padovanSequence() which takes integer N as input parameter and return N^{th} number in Padovan Sequence.
Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)
Constraints:
1 <= N <= 10^{6}

Starter code:
```python
#User function Template for python3



class Solution:

    def padovanSequence(self, n):

        # code here
```
