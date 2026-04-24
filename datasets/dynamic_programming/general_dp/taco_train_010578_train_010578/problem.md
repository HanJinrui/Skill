Find the number of occurrences of a given search word in a 2d-Array of characters where the word can go up, down, left, right, and around 90-degree bends.
Note: While making a word you can use one cell only once.
Example 1:
Input: 
R = 4, C = 5
mat = {{S,N,B,S,N},
       {B,A,K,E,A},
       {B,K,B,B,K},
       {S,E,B,S,E}}
target = SNAKES
Output:
3
Explanation: 
S N B S N
B A K E A
B K B B K
S E B S E
Total occurrence of the word is 3
and denoted by color.
Example 2:
Input:
R = 3, C = 3 
mat = {{c,a,t},
       {a,t,c},
       {c,t,a}}
target = cat
Output:
5
Explanation: Same explanation
as first example.
Your task:
You don't need to read input or print anything. Your task is to complete the function findOccurrence() which takes the mat containing N*M 2-d array of characters and target as input parameters and returns the number of occurrences of the target.
Expected Time Complexity: O(R*C*2^{2*len}), Where len is the length of the target String.
Expected Auxiliary Space: O(1)
Constraints:
1 ≤ len ≤ 15
1 ≤ R, C ≤ 50

Starter code:
```python
#User function Template for python3



class Solution:

    def findOccurrence(self,mat,target):
```
