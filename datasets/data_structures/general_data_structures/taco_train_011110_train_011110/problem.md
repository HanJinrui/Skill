Ishaan has bought N lottery tickets each having an ID denoted by an array A. As a result comes out, Ishaan gets very lucky and gets to know that each one of his tickets has won some prize. But unfortunately, he can't claim all of his lottery tickets.
The "sum_id" of a lottery ticket is the sum of the individual digits of the ticket ID. For example, sum_id of a ticket with ID = 1234 is 1+2+3+4 = 10.
Ishaan can claim the prize of a ticket only if no other ticket with the same sum_id has been claimed by him yet (Refer to example for explanation).
Find out the maximum number of tickets he can claim.
Example 1:
Input:
arr[ ] = {123, 42, 45, 78, 12345}
Output : 3
Explanation:
sum_id of Ticket 1: 1+2+3 = 6 (claimed)
sum_id of Ticket 2: 4+2 = 6 (can't be claimed since Ticket 1, with same sum_id has already been claimed)
sum_id of Ticket 3: 4+5 = 9 (claimed),
sum_id of Ticket 4: 7+8 = 15 (claimed),
sum_id of Ticket 5: 1+2+3+4+5 = 15
(can't be claimed since Ticket 4 with the same sum_id has already been claimed)
Example 2:
Input: 
arr[ ] = {2, 3, 4, 6, 22, 8} 
Output: 5 
 
Your Task:
This is a function problem. The input is already taken care of by the driver code. You only need to complete the function lucky() that takes an array (arr), sizeOfArray (n), and return the maximum number of tickets he can claim. The driver code takes care of the printing.
Expected Time Complexity: O(N).
Expected Auxiliary Space: O(1).
Constraints :
1 ≤ N ≤ 5000
1 ≤ A[i] ≤ 10^{15}

Starter code:
```python
#User function Template for python3



def lucky (arr, n) : 

    #Complete the function
```
