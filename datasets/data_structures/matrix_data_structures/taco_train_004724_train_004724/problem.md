Given N and a N*N matrix containing 0’s and 1’s. Group all the row numbers (starting index 0) which are having 1’s at same position.
Example 1:
Input:
N=4
matrix= [0010
            0100
            0010
            0000]
Output:
0 1
Explanation:
In the above test case, 1st and 3rd row have
the 1's at same column,i.e., 2(starting index 
from 0) so group first and third row. And print 
the index of first row, i.e., 0 (starting index 
from 0).
For second row, as it is the only row with same 
indexing of 1's so print it's index , i.e., 1.
For forth row, 1 is not present in this row so 
didn't print anything.
Example 2:
Input:
N=1
matrix = [0]
Output:
-1
Explanation:
There is no row containing 1.
 
Your task:
You don't need to read input or print anything. Your task is to complete the function groupRows(), which takes  the matrix and an integer N as input parameters and returns a list of row numbers after grouping. If there is no row containing 1, return -1.
 
Expected Time Complexity: O(n*n)
Expected Auxiliary Space: O(n*n)
 
Constraints:
1<=N<=20

Starter code:
```python
#User function Template for python3



class Solution:

    def groupRows(self, M , n):

        #code here
```
