There are N ticket sellers where the ith ticket seller has A[i] tickets. 
The price of a ticket is the number of tickets remaining with the ticket seller. They are allowed to sell at most K tickets. Find the maximum amount they can earn by selling K tickets. 
The amount of tickets of each seller is provided in array A. Give the answer modulo 10^{9} + 7.
Example 1:
Input: N = 5, K = 3
A = {4, 3, 6, 2, 4}
Output: 15
Explaination: Consider 0 based indexing. 
For first two turns the 2nd seller sells. 
For the third turn either 0th or 2nd 
seller can sell. So the total becomes 
6 + 5 + 4 = 15.
Example 2:
Input: N = 6, K = 2
A = {5, 3, 5, 2, 4, 4}
Output: 10
Explaination: The turns are taken by 
0th and 2nd seller. 5 + 5 = 10 is the 
maximum amount.
Your Task:
You do not need to take input or print anything. Your task is to complete the function maxAmount() which takes N, K, and the array A as input parameters and returns the maximum amount they can get by selling K tickets.
Expected Time Complexity: O(N*log(N))
Expected Auxiliary Space: O(N)
Constraints:
1 ≤ N ≤ 10^{5}
1 ≤ A[i], K ≤ 10^{6}

Starter code:
```python
#User function Template for python3



class Solution:

    def maxAmount(self, N, K, A):

        # code here
```
