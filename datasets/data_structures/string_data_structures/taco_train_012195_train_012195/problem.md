Given a string and number of rows ‘n’. Print the string formed by concatenating n rows when the input string is written in row-wise Zig-Zag fashion.
Example 1:
Input: 
str = "ABCDEFGH"
n = 2
Output: "ACEGBDFH"
Explanation: 
Let us write input string in 
Zig-Zag fashion in 2 rows.
A   C   E   G  
  B   D   F   H
Now concatenate the two rows and ignore 
spaces in every row. We get "ACEGBDFH"
Example 2:
Input: 
str = "GEEKSFORGEEKS"
n = 3
Output: GSGSEKFREKEOE
Explanation: 
Let us write input string in 
Zig-Zag fashion in 3 rows.
G       S       G       S
  E   K   F   R   E   K
    E       O       E
Now concatenate the two rows and ignore spaces
in every row. We get "GSGSEKFREKEOE"
Your Task:
You need not read input or print anything. Your task is to complete the function convert() which takes 2 arguments(string str, integer n) and returns the resultant string.
Expected Time Complexity: O(|str|).
Expected Auxiliary Space: O(|str|).
Constraints:
1 ≤ N ≤ 10^{5}

Starter code:
```python
#User function Template for python3

class Solution:

    def convert(self, Str, n):
        # code here
```
