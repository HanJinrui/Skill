King is getting ready for a war. He know his strengths and weeknesses so he is taking required number of soldiers with him. King can only defeat enemies with strongest and weakest power, and one soldier can only kill one enemy. Your task is to calculate that how many soldiers are required by king to take with him for the war.
Note: The array may contain duplicates.
 
Example 1:
Input:
N = 2
A[] = {1, 5}
Output:
0
Explanatation:
The king will itself be able to defeat all the enemies.
 
Example 2:
Input:
N = 3
A[] = {1, 2, 5}
Output:
1
Explanatation:
The king will defeat enemies with power
1 and 5, and he will need 1 soldier to
defeat the enemy with power 2.
 
Your Task:  
You don't need to read input or print anything. Your task is to complete the function SoldierRequired() which takes the array A[] and its size N as inputs and returns the number of soldiers, king will need to take with him for the war.
Expected Time Complexity: O(NLogN)
Expected Auxiliary Space: O(1)
 
Constraints:
1 ≤ N ≤ 10^{6 }
1 ≤ Ai ≤ 10^{6}
^{Array may contain duplicates}

Starter code:
```python
#User function Template for python3

class Solution:
    def SoldierRequired(self, arr, n):
         # Your code goes here
```
