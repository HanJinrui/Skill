You are playing a video-game in which your character has to cross N hurdles. Initially, your character has N energies states corresponding to each hurdle. All the hurdles have their respective heights.
Now, your character can only jump over a hurdle if its energy at that instant is greater than or equal to the hurdle's height.
When you cross a hurdle of height h, your current energy gets reduced by h. The remaining energy can be rolled over for subsequent hurdles.
Also, after your character crosses a hurdle, it gets an energy boost that is equal to the position of that hurdle(1,2,3....).
So, given N, N energy states, and N hurdle heights; you need to find whether you can win the game or not. You can only win if your character can successfully cross all the hurdles.
Example 1:
Ã¢â¬â¹Input : 
original_energies[ ] = {1, 1, 1}
hurdles_heights[ ] = {0, 2, 4}
Output : You Win! 3
Explanation:
Your inital energy for 1st hurdle is 1. 
The hurdle height is 0. You can cross it. 
The energy 1-0 =1 get rolled over to the 
next state. Also, you gets a boost of 1 since 
you crossed the first hurdle. The total 
energy of the next state becomes 1(rolled over)
+1(boost)+1(2nd states energy)=3. Now 3>= 2, 
so you can cross it. The energy 3-2=1 get rolled 
over. Also, you get a boost of 2 since you 
crossed 2nd hurdle. So, the next state's total 
energy becomes 1(rolled over)+2(boost)+
1(state's energy)=4. Now, 4>=4, so you can cross 
it. The remeining energy is 4 - 4=0 plus the 
boost of 3 since you crossed hurdle 3. 
The return energy at the end is 3. 
Ã¢â¬â¹Example 2:
Input : 
original_energies[ ] = {1, 1, 1} 
hurdles_heights[ ] = {8, 4, 6}
Output :  Game Over
 
Your Task:
This is a function problem. The input is already taken care of by the driver code. You only need to complete the function game() that takes an array of original energy (original_energies), array of hurdles height (hurdles_heights), sizeOfArray (n), and return the remaining energy at the end if it is not possible then return -1. The driver code takes care of the printing.
Expected Time Complexity: O(N).
Expected Auxiliary Space: O(1).
 
Constraints:
1 ≤ N ≤ 10^{5}
0 ≤ A[i] ≤ 10^{7}

Starter code:
```python
#User function Template for python3



def game (arr, brr, n) : 

    #Complete the function
```
