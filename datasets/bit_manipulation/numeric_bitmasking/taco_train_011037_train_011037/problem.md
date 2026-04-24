Given two integer numbers, F and S. In binary form of the numbers, for every i^{th }set bit in F, negate the i ^{th }bit in S.
Example 1:
Input:
F = 2 , S = 5
Output:
7
Explanation:
2 is represented as 10 in binary and
5 is represented as 101. Hence negating
the 2nd bit of 5 from right, thus the
new number becomes 7 i.e. 111. 
Example 2:
Input:
F = 1 , S = 3
Output:
2
Explanation:
1-1 and 3-11 in binary, thus negating
1st bit of 3 from right we get 10 i.e. 2. 
 
Your Task:
You don't need to read input or print anything. Your task is to complete the function negaBit() which takes 2 Integers F and S as input and returns the modified S.
Expected Time Complexity: O(1)
Expected Auxiliary Space: O(1)
 
Constraints:
1 <= F,S <= 10^{6}

Starter code:
```python
#User function Template for python3

class Solution:
    def negaBit(self, F , S):
        # code here
```
