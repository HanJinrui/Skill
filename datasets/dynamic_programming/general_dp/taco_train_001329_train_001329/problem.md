Given a Binary string st and a number k. You have to find the Longest continuous sequence of '0' after repeating Given string K time.
Example 1:
Input: k = 3
st = 100001
Output: 4
Explaination: The string repeated k times 
become 100001100001100001. Here the longest 
continuous sequence of 0 is 4.
Example 2:
Input: k = 4
st = 000
Output: 12
Explaination: When st is repeated 4 times 
it become 000000000000. The longest sequence 
becomes of length 12.
Your Task:
You do not need to read input or print anything. Your task is to complete the function lcsK() which takes k and st as input parameters and returns the length of the longest continuous sequence of 0's after repeating st k times.
Expected Time Complexity: O(|st|)
Expected Auxiliary Space: O(1)
Constraints:
1 ≤ |st| ≤ 10^{5}
1 ≤ k ≤ 10^{5}

Starter code:
```python
#User function Template for python3

class Solution:
    def lcsK(self, k, st):
        # code here
```
