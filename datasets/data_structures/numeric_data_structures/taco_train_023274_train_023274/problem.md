Your are given N students with some goodies to be distrubuted among them such that student at i^{th} index gets exactly i amount of goodies (considering no wastage). The goodies has already been distributed by some other. Your task is to check if it can be redistributed such that student at i^{th} index gets i amount of goodies. 
 
Example 1:
Input:
N = 5
Arr = {7, 4, 1, 1, 2}
Output:
YES
Explanation:
Since, all the goods can be
redistributed as 1 2 3 4 5 
(i^{th} students get i number of 
goodies).So, output is YES.
 
Example 2:
Input:
N = 5
Arr = {1, 1, 1, 1, 1}
Output:
NO
 
Your Task:  
You don't need to read input or print anything. Your task is to complete the function leftIndex() which takes the array Arr[] and its size N as inputs and returns  true if we can redistribute in the requried way, otherwise false .
Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)
Constraints:
1 <= N <= 10^{7}
0 <= A_{i} <= 10^{18}

Starter code:
```python
#User function Template for python3



class Solution:

    def possible(self, arr, n):

        #code here.
```
