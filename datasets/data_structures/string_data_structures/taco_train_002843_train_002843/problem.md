Given a string S of digits(0-9).Find the maximum value that can be obtained from the string by putting either '*' or '+' operators in between the digits while traversing from left to right of the string and picking up a single digit at a time.
Example 1:
Input: 
S="01230"
Output: 
9
Explanation: 
we have 01230.We traverse from 
left and pick zero.Now we encounter '1'. 
We see if 0*1 gives maximum or 0+1.Now we 
have ans=1.Now we traverse further.We 
encounter '2'.Now we see whether 1*2 gives 
max or 1+2.Now we have ans=3.Now we 
traverse further. We encounter'3'.
We see if 3*3 gives max or 3+3.
The ans is now 9.Now we traverse further. 
We encounter 0, we see if 9+0 gives max or 
9*0. The ans is now 9. We've traversed the
whole string so we stop.
Example 2:
Input: 
S="891"
Output: 
73
Explanation:
We start at 8,then go to
9 and see whether 8+9 is greater or
8*9.Now we have 72,we traverse 
forward and check whether 72*1 is 
greater or 72+1.In this way, we get 
the answer as 73.
Your Task:
You don't need to read input or print anything. Your task is to complete the function MaximumIntegerValue() which takes the string S as input parameter and returns the maximum integer value that can be created using given procedures
Expected Time Complexity: O(|S|)
Expected Auxiliary Space: O(1)
Constraints:
1 <= |S| < 20
S contains only digits from 0 to 9
Leading 0's maybe present.

Starter code:
```python
#User function Template for python3

class Solution:
    def MaximumIntegerValue(self,S):
        #code here
```
