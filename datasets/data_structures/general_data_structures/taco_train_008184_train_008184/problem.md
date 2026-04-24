Given a sorted array A[] of N distinct integers from 0 to 99999. Find all the integer intervals missing from the given list.
Note: There is always atleast 1 number missing.
Example 1:
Input:
N = 4
A = {1,5,67,88}
Output:
0,2-4,6-66,68-87,89-99999
Explanation:
All the missing Intervals are printed.
Example 2: 
Input:
N = 6
A = {4,55,77,89,91,99} 
Output:
0-3,5-54,56-76,78-88,90,92-98, 100-99999
Your Task:  
You don't need to read input or print anything. Your task is to complete the function printMissingIntervals() which takes Integer N and an Array A[] as input and returns a array of elements with 2*x elements where x is the number of missing intervals and each pair in the array is the range missing. arr={1,3,97,100} would mean the intervals missing are 1-3 and 97-100. Suppose only the number 1 is missing ,then arr={1,1}.
 
Expected Time Complexity: O(N)
Expected Auxiliary Space: O(N)
 
Constraints:
1 ≤ N ≤ 10^{5}
0 ≤ A_{i} < 10^{5}

Starter code:
```python
#User function Template for python3

class Solution:
    def printMissingIntervals(self, a , n):
        # code here
```
