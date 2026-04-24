Given a string of a constant length, print a triangle out of it. The triangle should start with the given string and keeps shrinking downwards by removing one character from the begining of the string. The spaces on the left side of the triangle should be replaced with dot character.
 
Example 1: 
Input:
S = Geeks
Output:
Geeks
.eeks
..eks
...ks
....s
Example 2: 
Input:
S = @io30 
Output:
 @io30
.io30
..o30
...30
....0 
 
Your Task:
You don't need to read input or print anything. Your task is to complete the function triDownwards() which takes a String S and returns a string formed by joining all the lines together. For the Input "GEEKS" you should return the String "GEEKS.EEKS..EKS...KS....S".
 
Expected Time Complexity: O(|S|^{2})
Expected Auxiliary Space: O(|S|)
 
Constraints:
1 <= |S| <=100

Starter code:
```python
#User function Template for python3



class Solution:

    def triDownwards(self, S):

        # code here
```
