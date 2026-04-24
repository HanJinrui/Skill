Given a string S, find whether it fulfills the following criteria. 
When split from the middle, the string should give two halves having the same characters and same frequency of each character. If the number of characters in the string is odd, ignore the middle character.
Example 1:
Input: S = "abcdbca"
Output: YES
Explanation: The string has length 7 which
is odd, hence we ignore the middle character
'd'. The frequency of 'a', 'b' and 'c' is 
same in both the halves. Hence, the string
fulfills the given criteria. 
Ã¢â¬â¹Example 2:
Input: S = "abbaab"
Output: NO
Explanation: The frequency of 'a' in both
the halves is different. Hence, the string
does not fulfill the given criteria. 
Your Task:
You don't need to read input or print anything. Your task is to complete the function passed() which takes the string S as input parameter and returns a boolean value denoting whether it fulfills the given criteria or not. 
Expected Time Complexity: O(|S|)
Expected Auxiliary Space: O(1)
Constraints:
1<=|S|<=10^{5}

Starter code:
```python
#User function Template for python3



class Solution:

    def passed(self, s):

        # code here
```
