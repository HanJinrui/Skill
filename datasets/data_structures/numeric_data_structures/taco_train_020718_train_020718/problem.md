Given two integers X and N, you have to find an array such that it contains the frequency of index numbers occurring in (X^{1} X^{2} .... X^{N-1} X^{N}) . 
Example 1:
Input:
X = 15, N = 3
Output: 0 1 2 2 0 3 0 1 0 0
Explanation: 15^1, 15^2, 15^3 ==> 15, 225, 3375
An array which displays the frequency of 
its index numbers occuring in 15, 225 and 3375
Frequency of '0' = 0
Frequency of '1' = 1 (only once in 15)
Frequency of '2' = 2 (twice in 225)
Frequency of '3' = 2 (twice in 3375)
Frequency of '4' = 0
Frequency of '5' = 3 (thrice in '15', '225' and '3375')
Frequency of '6' = 0
Frequency of '7' = 1 (only once in '3375')
Frequency of '8' = 0
Frequency of '9' = 0
Resultant array:
0 1 2 2 0 3 0 1 0 0
Example 2:
Input:
X = 2, N = 4
Output: 0 1 1 0 1 0 1 0 1 0
Your Task:
You don't need to read input or print anything. Your task is to complete the function getFreq() which takes the two integers x and n as parameters and returns an array of integers denoting the answer.
Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)
Constraints:
1 <= X <= 15
1 <= N <= 15

Starter code:
```python
#User function Template for python3





def getFreq(x, n):

    # code here
```
