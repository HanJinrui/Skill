Given an array arr consisting of integers of size n and 2 additional integers k and x, you need to find the number of subsets of this array of size k, where Absolute difference between the Maximum and Minimum number of the subset is at most x.
Note: As this number that you need to find can be rather large, print it Modulo 10^{9}+7
 
Example 1:
Input:
n = 5, k = 3, x = 5
arr[] = {1, 2, 3, 4, 5}
Output:
10
Explanation :
Possible subsets of size 3 are :-
{1,2,3} {1,2,4} {1,2,5} {1,3,4}
{1,3,5} {1,4,5} {2,3,4} {2,3,5}
{2,4,5} {3,4,5} having difference
of maximum and minimum
element less than equal to 5.
 
Example 2:
Input:
n = 8, k = 4, x = 6
arr[] = {2, 4, 6, 8, 10, 12, 14, 16}
Output:
5
Explanation :
Possible subsets of size 4 are:-
{2,4,6,8} {4,6,8,10} {6,8,10,12}
{8,10,12,14} {10,12,14,16} having
difference of maximum and minimum 
element less than equal to 6.
Your Task:
You don't have to print anything, printing is done by the driver code itself. Your task is to complete the function getAnswer() which takes the array arr[], its size n and two integers k and x as inputs and returns the required result, Modulo 10^{9}+7.
 
Expected Time Complexity: O(n. log(n))
Expected Auxiliary Space: O(n)
 
Constraints:
1 ≤ n ≤ 5×10^{5}
1 ≤ k ≤ n
1 ≤ arr[i], x ≤ 10^{9}

Starter code:
```python
#User function Template for python3



def getAnswer( arr, n, k, x):

    # Your code goes here
```
