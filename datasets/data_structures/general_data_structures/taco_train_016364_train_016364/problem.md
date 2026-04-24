Pasha has been very sick. His platelets went way down. Being a paranoid person, he consulted N doctors about the optimal range in which Platelet Count should lie. The i-th doctor suggested that the Platelet count should be between li and ri, inclusive, to be called normal.
Now, Pasha thinks that a Platelet count is Safe to have if at least K Doctors recommend it. Pasha now asks Q Queries. In each query- he will give an integer P (the platelet count). Pasha wants to know if the entered Platelet count is safe to have or not.
 
Example 1:
 
Input : 
V[] = {[1, 10], [5, 7], [7, 12], 
    [15, 25], [20, 25]}, K = 3, 
queries[] = {7, 5, 10, 16}
Output : 
Yes
No
Yes
No
Explanation:
The first query : 7 is in [1,10] , 
[5,10] , [7,12] So recommended by 3 
Doctors-YES
The second query : 5 is in [1,10] , 
[5,10] recommended by 2 doctors- "No"
The third query : 10 is in [1,10] , 
[5,10] , [7,12] recommended by 3 
doctors- "Yes"
The Fourth query : 16 is in [15,25]
recommended by 1 doctors- "No"
Your Task:
This is a function problem. The input is already taken care of by the driver code. You only need to complete the function QueryComputation() that takes the size of an array (N), a 2-d array (arr), integer K,  no. of queries q, an array of queries (queries), and return the boolean array that has true if the query is true else false. The driver code takes care of the printing.
Expected Time Complexity: O(N + Q).
Expected Auxiliary Space: O(N).
Constraints:
1 ≤ N,Q ≤ 2*10^{5}
1 ≤ Z ≤ N
1 ≤ Li ≤ Ri ≤ 2*10^{5}
1 ≤ P ≤ 2*10^{5}

Starter code:
```python
#User function Template for python3



def QueryComputation (n, arr, k, q, queries) : 

    #Complete the function
```
