Geek is given a task to select at most 10 employees for a company project. Each employee is represented by a single digit ID number which is unique for all the selected employees for the project. Geek has a technical problem in his system which printed ID number multiple times. You are given array a[ ] of N elements having all printed IDs. Help him to get rid of the repeated IDs.
Example 1:
Input:
N = 5
a[ ] = {8, 8, 6, 2, 1}
Output:
8 6 2 1
Example 2:
Input:
N = 6
a[ ] = {7, 6, 7, 4, 2, 7}
Output:
7 6 4 2
Your Task:  
You don't need to read input or print anything. Your task is to complete the function uniqueId() which takes the array a[] and its size N as input parameters and returns the list containing non repeated IDs of employees in the same sequence they appear.
Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)
Constraints:
1 ≤ N ≤ 1000
0 ≤ a[i] ≤ 9

Starter code:
```python
#User function Template for python3

def uniqueId( a, n):
```
