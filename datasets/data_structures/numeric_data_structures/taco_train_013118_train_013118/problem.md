Ram and Rohan are participating in a tournament. Together they must face off against x contenders whose strengths are given in an array arr[]. The respective strength of Ram and Rohan in m and n. They take turns taking part in face-off matches with contenders and Ram goes first. They win a match only if their opponent's strength is an integral multiple of their strengths. If the opponent is defeated, he can not fight again. 
Find out who among Ram and Rohan is a better player. If both of them win the same number of matches then both are winners.
Example 1:
Input: 
x = 7
m = 2, n = 3
arr = {4, 5, 7, 6, 9, 10, 14}
Output: Ram
Explaination: Ram win against opponents 
having strength 4, 6, 10, 14 and Rohan 
win against opponent having strength 9.
Example 2:
Input: 
x = 6
m = 5, n = 3
arr = {1, 9, 9, 10, 9, 18}
Output: Rohan
Explaination: Ram win against opponent 
having strength 10 and Rohan win against 
three opponents having strength 9 and one 
having strength 18.
Your Task:
You do not need to read input or print anything. Your task is to complete the function winner() which takes x, m, n and arr as input parameters and returns one of the strings from {"Ram", "Rohan", "Both"} based on the answer. 
Expected Time Complexity: O(x)
Expected Auxiliary Space: O(1)
Constraints:
1 ≤ x, n, m ≤ 10^{5}
1 ≤ arr[i] ≤ 10^{18}

Starter code:
```python
#User function Template for python3



class Solution:

    def winner(self, x, m, n, arr):

        # code here
```
