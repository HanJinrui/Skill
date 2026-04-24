A Professor conducts a Computer Science paper for N students. He had strictly instructed all students to sit according to their roll numbers. However when he started checking the papers, he found out that all the papers were randomly ordered because the students had sat randomly during the exam instead of sitting according to their roll numbers. The order is given in list of integers roll[ ]. The professor became very angry and he wanted to teach the students a lesson.
He decided to sort the papers according to roll numbers by Bubble Sort and count the number of swaps required for each and every student and deduct as many marks of a student as were the number of swaps required for that student. The marks of every student is given in list of integers marks[ ] in the order in which they were sitting. However he also has to maintain the class average greater than or equal to a set minimum avg, else he may lose his job. The Professor wants to know whether he should punish the students or save his job.
Example 1:
Input:
N = 5 
avg = 68
roll[] = {3, 2, 4, 1, 5}
marks[] = {50, 67, 89, 79, 58}
Output: 0
Explanation: Overall number of swaps required 
is 8. Hence the class average would become
(50 + 67 + 89 + 79 + 58 - 8) / 5 = 67
Since 67 is less than the required minimum (68),
he will not punish the class to save his Job.
Example 2:
Input:
N = 6 
avg = 67.5
roll[] = {5, 4, 1, 3, 2, 6}
marks[] = {78, 98, 86, 67, 78, 79}
Output: 1
Explanation: Overall number of swaps required 
is 16. Hence the class average would become
(78 + 98 + 86 + 67 + 78 + 79 - 16) / 6 = 78.33.
Since 78.33 is greater than the required 
minimum (67.5), he will punish the class and 
deduct the marks.
Your Task:
You don't need to read input or print anything. Your task is to complete the function shouldPunish() which takes the array roll[] describing the order of students while sitting for the exam, the array marks[] describing the marks of the students, an integer N denoting the number of students and an avg denoting the required minimum average that is to be maintained as input parameters and returns 1 if the professor will punish the students or 0 otherwise.
Expected Time Complexity: O(N^{2}).
Expected Auxiliary Space: O(1).
Constraints:
1 ≤ N ≤ 1000

Starter code:
```python
#User function Template for python3



class Solution:

    def shouldPunish (self, roll, marks, n, avg):

        #  your code here
```
