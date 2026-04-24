Mila and Gila are sisters, Mila being the younger one. They both have some number of coins of different denominations with them. Mila being a stubborn little sister won’t share her coins with anyone but wants that both of the sisters have equal money. Gila being an understanding elder sister accepts to give some of her coins to Mila if that can make the money equal.
You are given N - number of coins Gila has and list of integers A[ ] - denominations of N coins of Gila.
As Mila won’t share any of her coins with anyone, you are only provided with the total money with Mila M and no details of her denominations.
You are required to find out whether they can distribute the money among themselves such that both of them have equal money or not.
Example 1:
Input:
N = 5 and M = 6
A[] = [1, 2, 3, 0, 6]
Output: 1
Explanation:
Gila can give her Rs. 3 coin to Mila.
Hence, both of them would have Rs. 9
Example 2:
Input:
N = 5 and M = 5
A[] = [1, 2, 3, 2, 6]
Output: 0
Your Task:  
You don't need to read input or print anything. Your task is to complete the function sisterCoin() which takes the integer N, integer M and an array A[ ] as input parameters and returns the 1 if they can distribute the money among themselves such that both of them have equal amount or return 0 otherwise.
Expected Time Complexity: O(N*M)
Expected Auxiliary Space: O(N*M)
Constraints:
1 ≤ N ≤ 50
0 ≤ M ≤ 5000
0 ≤ value of a coin ≤ 100

Starter code:
```python
#User function Template for python3

class Solution:
    def sisterCoin (self, arr, N, M):
        pass
        # code here
```
