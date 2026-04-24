Geek wants to distribute gifts to N students. He buys N gifts and asks his students to make a list of gifts arranged in order of their preference. Each student has a unique rank based on their performance in Geek's class. The gifts are distributed based on a student's rank and gift preference. The list submitted by a student with a better rank is given more importance. Find what gift each student gets. 
Example 1:
Input:
N = 3
Arr[][] = { {Preference list of student 1},
            {Preference list of student 2},
            {Preference list of student 3},}
        = {{1, 3, 2}, {2, 1, 3}, {3, 1, 2}}
Output: 1 2 3
Explanation: According to the gift preference 
of child with rank 1, he gets gift 1. Rank 2 
prefers gift 2 and gets that. Rank 3 prefers 
gift 3 and gets that.
Example 2:
Input:
N = 3
Arr[][] = { {Preference list of student 1},
            {Preference list of student 2},
            {Preference list of student 3},}
        = {{1, 2, 3}, {3, 2, 1}, {1, 2, 3}}
Output: 1 3 2
Explanation: According to the gift preference 
of child with rank 1, he gets gift 1. Rank 2 
prefers gift 3 and gets that. Rank 3 prefers 
gift 1 but that was given to student with rank 1. 
Second on his list is gift 2 so he gets that.
Your Task:
You don't need to read input or print anything. Your task is to complete the function distributeGift() which takes the 2D array of integers arr and n as input parameters and returns an array of integers of size N denoting the gift that each student got in order of their ranks.
Expected Time Complexity: O(N^{2})
Expected Auxiliary Space: O(1)
Constraints:
1 <= N <= 10^{3}
Preference of each child is a permutation [1, N]

Starter code:
```python
#User function Template for python3



class Solution:

    def distributeGift(self, arr, n):

        # code here
```
