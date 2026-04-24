Given a Sentence S of length N containing only english alphabet characters, your task is to write a program that converts the given sentence to Snake Case sentence. Snake case is the practice of writing compound words or phrases in which the elements are separated with one underscore character (_) and no spaces, and the first letter of each word written in lowercase. For ease keep all the characters in lowercase.
Note: The given sentence will not start with a Whitespace.
Example 1: 
Input: 
N = 14
S = "Geeks ForGeeks"
Output: "geeks_forgeeks"
Explanation: All upper case characters are
converted to lower case and the whitespace
characters are replaced with underscore '_'.
Example 2: 
Input: 
N = 21
S = "Here comes the garden"
Output: "here_comes_the_garden"
Explanation: All upper case characters are
converted to lower case and the whitespace 
characters are replaced with underscore '_'.
Your Task:
You don't need to read input or print anything. Your task is to complete the function snakeCase() which takes N and a String S as input parameters and returns the converted string .
Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)
Constraints:
1 ≤ N ≤ 10^{5}

Starter code:
```python
class Solution:
    def snakeCase(self, S , n):
        # code here
```
