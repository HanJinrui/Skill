Siddhant made a special series and named it as G.F Series. The series follows this trend  T_{n}=(T_{n-2})^{2}-(T_{n-1})  in which the first and the second term are 0 and 1 respectively. Help Siddhant to find the first N terms of the series.
Note: Print a white space (" ") after every integer and a newline character after every testcase. The generated output is white space sensitive, do not add extra spaces on unnecessary newline characters.
Example 1:
Input:
N = 3
Output:
0 1 -1
Explanation:
First-term is given as 0 and the second 
term is 1. So the T_{3} = (T_{3-2})^{2} - (T_{3-1}) 
= T_{1}^{2} - T_{2} = 0^{2} - 1 = -1
Example 2:
Input:
N = 6
Output:
0 1 -1 2 -1 5  
Explanation:
T_{1} : 0
T_{2} : 1
T_{3} : -1
T_{4} = (1)^{2} - (-1) = 2
T_{5} = (-1)^{2} - (2) = 1 - 2 = -1
T_{6} = (2)^{2} - (-1) = 4 + 1 = 5 
Your Task:  
You don't need to read input. Your task is to complete the function gfSeries() which takes an integer N as an input parameter and print first N term of the series.
Expected Time Complexity: O(N)
Expected Auxiliary Space: O(N)
Constraints:
2 <= N <= 15

Starter code:
```python
class Solution:

    def gfSeries(self, N : int) -> None:

        # code here
```
