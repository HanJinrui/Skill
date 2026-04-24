Given N unique characters (in infinite supply), find the number of possible mapped strings of length N.
A mapped string follows following properties:
1. Both left and right halves of the string contains same set of characters.
2. Each half contains N / 2 unique characters.
For example: “abccba” is Mapped string since the left and right halves contain unique characters and both halves contain same set of characters but "abcbcd" is not.
As the answer can be very large, find it modulo 10^{9} + 7.
Note: N is always even.
Example 1:
Input: N = 2
Output: 2 
Explanation: Suppose two unique characters
are 'a' and 'b', then there will be two 
mapped strings - 'aa' and 'bb'.
Example 2:
Input: N = 4
Output: 24
Explanation: Suppose four unique characters
are 'a', 'b', 'c' and 'd' and for each pair of
them there will be four mapped strings. Hence, 
there are total 6 pairs so 6 * 4 = 24 total 
mapped strings.
Your Task:  
You dont need to read input or print anything. Complete the function mapStr() which takes N as input parameter and returns the number of possible mapped strings of length N.
Expected Time Complexity: O(N)
Expected Auxiliary Space: O(N)
Constraints:
2 ≤ N ≤ 100000

Starter code:
```python
#User function Template for python3
class Solution:
    def mapStr (ob, N):
        # code here
```
