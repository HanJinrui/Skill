Given two stacks of pizzas such that each contains 10 pizzas of varying radii. Geek can only eat a pizza from a stack if it is also present in the other stack, in the same order. The pizzas that he selects need not be continuous. Find the number of pizzas Geek can eat.
 
Example 1:
Input:
Stack1 = {891 424 945 741 897 514 692 221 678 168}
Stack2 = {702 952 221 614 69 753 821 971 318 364}
Output: 1
Explanation: There is only one common element.
 
Example 2:
Input:
Stack1 = {476 241 866 571 827 599 949 948 579 726}
Stack2 = {371 359 610 216 885 876 92 10 171 724}
Output: 0
Explanation: There is no common element.
Your Task:  
You don't need to read input or print anything. Your task is to complete the function getCommon() which takes two arrays stack1[] and stack2[], each of fixed size 10 as input parameters and returns the number of pizzas Geek can eat.
 
Expected Time Complexity : O(N^{2})
Expected Auxiliary Space : O(N^{2}) Where N is the stack length = 10.
 
Constraints:
Stack_{1 }= Stack_{2} = 10
1 <= radii <= 10^{3}

Starter code:
```python
#User function Template for python3

class Solution:
    def getCommon(self, stack1, stack2):
```
