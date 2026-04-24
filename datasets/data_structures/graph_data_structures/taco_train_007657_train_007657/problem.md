Given the following grid containing alphabets from A-Z and  a string S.Find the shortest possible path to type all characters of given string in given order using only left,right,up and down movements(while staying inside the grid).Initially you start at A(on the top-left corner).
Find the horizontal movement first(Left/Right) and, then, the vertical movement(Up/Down) for each character of the string.
Grid:
A B C D E
F G H I J
K L M N O
P Q R S T
U V W X Y
Z
Example:
Input:
S=GFG
Output:
RIGHT DOWN OK LEFT OK RIGHT OK 
Explanation:
We start at A, go towards G,
then towards F and finally again towards G,
using the shortest paths possible.When You
reach the character, insert "OK" into the
string array.
Example 2:
Input:
S=GEEK
Output:
RIGHT DOWN OK RIGHT RIGHT
RIGHT UP OK OK LEFT LEFT LEFT
LEFT DOWN DOWN OK 
Explanation:
Starting from A, we go 
towards G,then E,we stay at E,Then 
we go towards K using the shortest paths.
Your Task:
You don't need to read input or print anything.Your task is to complete the function ShortestPath() which takes a string S and returns an array of strings containing the order of movements required to cover all characters of S.
Expected Time Complexity: O(N)
Expected Auxillary Space: O(1)
Constraints:
1 ≤ |S| ≤ 10^{6}
S consists of character from A-Z.

Starter code:
```python
#User function Template for python3

class Solution:
    def ShortestPath(self,S):
        #code here
```
