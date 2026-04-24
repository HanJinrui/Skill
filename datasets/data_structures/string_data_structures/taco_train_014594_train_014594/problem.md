A Duck number is a positive number which has zeroes present in it, For example, 3210, 8050896, 70709 are all Duck numbers. A number with only leading 0s is not considered as Duck Number. For example, numbers like 035 or 0012 are not considered as Duck Numbers. A number like 01203 is considered as Duck because there is a non-leading 0 present in it.
The task is to check whether the given number N is a Duck number or not.
 
Example 1:
Input: 707069
Output: YES
Explanation: 707069 contains a non-leading 0.
 
Example 2:
Input: 02364
Output: NO
Explanation: contains only leading 0.
 
Your Task:
Your task is to complete the function check_duck() which takes a single argument(string N) and returns true if N is a Duck number else false. You need not take input or print anything. The driver code will itself print "YES" if the returned value is true and "NO" if the returned value is false.
Expected Time Complexity: O(|N|).
Expected Auxiliary Space: O(1).
 
Constraints :
1 ≤ Length of N ≤ 10^{4}

Starter code:
```python
#User function Template for python3



class Solution:



    def check_duck(self, N):

        # code here
```
