A number is non-decreasing if each of its digits is greater than or equal to the previous digit. For example, 223, 4455567, 899, are non-decreasing numbers. 
Given an integer N, find the total number of non-decreasing numbers that have N digits.
Example 1:
Input: N = 1
Output: 10
Explaination: All the single digit numbers 
are non-decreasing. So count is 10.
Example 2:
Input: N = 2
Output: 55
Explaination: For number starting with 1 there 
is 1 decreasing number 10, for number starting 
with 2 there are 2 decreasing numbers. 
Similarly numbers starting with 3, 4 . . . 9 
there are 3, 4 . . . 9 decreasing numbers. 
Total 45 decreasing numbers. Total possible 
numbers are 10^{2} = 100. So total number of 
non-decreasing numbers are 100-45 = 55.
Your Task:
You do not need to read input or print anything. Your task is to complete the function count() which takes the number N as input parameter and return the total number of non-decreasing numbers.
Expected Time Complexity: O(N)
Expected Auxiliary Space: O(N)
Constraints:
1 ≤ N ≤ 500

Starter code:
```python
#User function Template for python3



class Solution:

    def count(self, N):

        # code here
```
