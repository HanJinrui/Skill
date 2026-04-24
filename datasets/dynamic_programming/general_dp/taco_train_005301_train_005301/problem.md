You are given n days and for each day (d_{i}) you can select one of the following options:
	perform no task 
	perform a high effort task (h_{i}) only if its the first day or if you chose no-task on the previous day
	perform a low effort task (l_{i})
Write a program to find the maximum amount of tasks you can perform within these n days. 
Example 1:
Input:
n = 3
hi[] = {2,8,1}
li[] = {1,2,1}
Output: 9
Explanation:
Options on 1st day: hi[0]=2, li[0]=1 or no-task
Select no-task.
Options on 2nd day: hi[1]=8, li[2]=1 or no-task
Select high-effort task as no-task was selected 
the previous day.  
Options on 3rd day: hi[2]=1, li[2]=1 or no-task
Select low-effort task as selecting high-effort 
task is only possible if you chose no-task on 
previous day.
Example 2:
Input:
n = 5
hi[] = {3,6,8,7,6}
li[] = {1,5,4,5,3}
Output: 20
Explanation: Perform high-effort task on first 
day and low-effort task on all remaining days.
 
Your Task:
You don't need to read input or print anything. Your task is to complete the function maxAmt() which accepts an integer n and two arrays li[] and hi[] as input parameter and returns the maximum amount of tasks you can perform within these n days.
Expected Time Complexity: O(n)
Expected Auxiliary Space: O(n)
Constraints:
1 <= n <= 10^{6}

Starter code:
```python
#User function Template for python3

class Solution:
    def maxAmt(self, n, hi, li): 
        # code here
```
