Given an array A of positive integers, find the smallest non-negative integer (i.e. greater than or equal to zero) that can be placed between any two elements of the array such that the sum of elements in the subarray occurring before it,  is equal to the sum of elements occurring in the subarray after it, with the newly placed integer included in either of the two subarrays.
 
Example 1:
Input : Arr[] = {3, 2, 1, 5, 7, 8}
Output : 4 5 1
Explanation:
The smallest possible number that we can 
insert is 4, at position 5 (i.e. between 
5 and 7) as part of first subarray so that 
the sum of the two subarrays becomes 
equal as, 3+2+1+5+4=15 and 7+8=15.
Example 2:
Input : Arr[] = {9, 5, 1, 2, 0}
Output : 1 2 2
Explanation:
The smallest possible number that we can 
insert is 1,at position 2 (i.e. between 9 
and 5) as part of second subarray in 
order to get an equal sum of 9.
 
Output:
For each test case there is only one line of input comprising of three space separated integers. First, the new number that can be inserted. Second, the position (starting from 2 to N-1 , because new number can only be inserted between any two existing elements) where it should be inserted. Third, the subarray in which it is included (1 or 2) to get equal sums. If the smallest integer to be inserted has more than one possible position in the array to get equal sums, print the smallest position out of all possibilities. In case equal sums are obtained without adding any new element, the value of new element will be zero, followed by the position number, and is always included in the first subarray.
Your Task:
This is a function problem. The input is already taken care of by the driver code. You only need to complete the function EqualSum() that takes an array (arr), sizeOfArray (n), and return the array of 3 values define in the output format. The driver code takes care of the printing.
Expected Time Complexity: O(n).
Expected Auxiliary Space: O(1).
Note: Position of first element of array should be considered as 1.
Constraints:
2 ≤ N ≤ 10^{4}
0 ≤ A[i] ≤ 10^{3}, where i is an integer such that 0 ≤ i

Starter code:
```python
#User function Template for python3

class Solution:
    def EqualSum(self,a,n):
        #Complete the function
```
