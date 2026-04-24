The two countries of A and B are at war against each other. Both countries have N number of soldiers. The power of these soldiers are given by A[i]...A[N] and B[i]....B[N].
These soldiers have a peculiarity. They can only attack their counterpart enemies, like A[i] can attack only B[i] and not anyone else. A soldier with higher power can kill the enemy soldier. If both soldiers have the same power, they both die. You need to find the winner country.
Example 1:
Ã¢â¬â¹Input : a[ ] = {2, 2}, b[ ] = {5, 5}
Output : B
Explanation:
Both countries have 2 soldiers.
B[0] kills A[0], B[1] kills A[1]. 
A has 0 soldiers alive at the end. 
B has both soldiers alive at the end.
Return "B" as a winner.
Ã¢â¬â¹Example 2:
Input : a[ ] = {9}, b[ ] = {8}  
Output :  A
Your Task:
This is a function problem. The input is already taken care of by the driver code. You only need to complete the function Country_at_war() that takes an array (a), another array (b), sizeOfArray (n), and return the string "A" if A is the winner, "B" if B is the winner and "DRAW" if it draws. The driver code takes care of the printing.
Expected Time Complexity: O(N).
Expected Auxiliary Space: O(1).
 
Constraints:
1 ≤ N ≤ 10^{5}
0 ≤ A_{i} ≤ 10^{7}
0 ≤ B_{i} ≤ 10^{7}

Starter code:
```python
#User function Template for python3



def Country_at_war (arr, brr, n) : 

    #Complete the function
```
