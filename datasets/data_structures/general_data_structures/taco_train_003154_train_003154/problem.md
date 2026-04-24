There are N coins placed on the road where arr[i] is the denomination of i^{th} coin. A Fox is looking to collect some of these coins. The fox is very greedy and follows a weird pattern of collecting coins: the fox collects coins in only increasing order of their denomination since it always craves for more money and all the coins it collects are contiguous. The fox wants to maximize the amount of money it collects.
Unfortunately, the Fox is greedy but not intelligent enough to find the solution and asks you for help. Find the maximum amount of money the fox can collect. 
 
Example 1:
Input:
N=6
arr[] = {2, 1, 4, 7, 3, 6} 
Output: 12
Explanation: Contiguous Increasing subarray 
             {1, 4, 7} = 12.
 
Example 2:
Input:
N=5
arr[] = {38, 7, 8, 10, 12} 
Output: 38
Your Task:
Since, this is a function problem. You don't need to take any input, as it is already accomplished by the driver code. You just need to complete the function largestSum() that takes array arr and integer N as parameters and returns the desired output.
 
Expected Time Complexity: O(N).
Expected Auxiliary Space: O(1).
 
Constraints:
1 ≤ N ≤ 10^{5}

Starter code:
```python
#User function Template for python3





def largestSum(arr, N):
```
