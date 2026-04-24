You are given an integer 'n' which denote the number of elements in an array a[ ] and an integer 'x'. You have to calculate the average of element a[i] and x and find out if that number exist in array or not. Do it for all the elements of array and store the count result in another array for each index i.
Note: Always take the floor value of the average.
Example 1:
Input : arr[ ] = {2, 4, 8, 6, 2} and X = 2
Output : 2 0 0 1 2
Explanation:
value of n is 5 and that of x is 2. 
The array is 2 4 8 6 2. We take x 
i.e. 2 and take average with a[0] 
whch is equal to 2. We found 2 resides 
in array at two positions (1st and 5th 
element) thus storing 2 in another 
array at 0th index. Similarly do for all 
elements and store the count in second 
array.
Example 2:
Input : arr[ ] = {9, 5, 2, 4, 0, 3} 
        and X = 3 
Output :  0 1 1 1 0 1 
 
Your Task:
This is a function problem. The input is already taken care of by the driver code. You only need to complete the function countArray() that takes an array (arr), sizeOfArray (n), an integer X, and return the resultant array in which you have to calculate the number of times the average of a[i] and x occurs in the array for each index i. The driver code takes care of the printing.
Expected Time Complexity: O(N^{2}).
Expected Auxiliary Space: O(1).
Constraints:
1 ≤ N ≤ 100
1 ≤ X ≤ 100
1 ≤ a[i] ≤ 100

Starter code:
```python
#User function Template for python3



class Solution:

    def countArray (self, arr, n, x) : 

        #Complete the function
```
