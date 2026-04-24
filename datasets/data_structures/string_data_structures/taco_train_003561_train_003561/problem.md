You are given an array of size N. You need to find elements which appear prime number of times in the array with minimum K frequency (frequency >= K).
Example 1:
Input : 
N = 13, K = 2
arr[ ] = {11, 11, 11, 23, 11, 37, 51, 
          37, 37, 51, 51, 51, 51}
Output : 37 51
Explanation:
11's count is 4, 23 count 1, 37 count 3, 
51 count 5. 37 and 51 are two number that 
appear prime number of time and frequencies 
greater than or equal to K=2.
Example 2:
Input : arr[ ] = {11, 22, 33} 
Output :  -1
Your Task:
This is a function problem. The input is already taken care of by the driver code. You only need to complete the function primeOccurences() that takes an array (arr), sizeOfArray (n), integer value K, and return the array of the elements that have prime frequency with their frequency >=K in sorted form. The driver code takes care of the printing.
Expected Time Complexity: O(N*SQRT(N)).
Expected Auxiliary Space: O(N).
 
Constraints:
1 ≤ N ≤ 10^{5}
1 ≤ K ≤ 100
1 ≤ A[i] ≤ 10^{5}

Starter code:
```python
#User function Template for python3



def primeOccurences (arr, n, k) : 

    #Complete the function
```
