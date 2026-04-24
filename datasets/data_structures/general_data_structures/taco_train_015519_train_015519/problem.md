You are given an array arr[] of size N.
The array consists of a permutation of the set {1, 2, 3, … , N} for some positive integer N. You have to start at the position which has 1 in the array and then travel to the position which has 2. Then from 2, you travel to 3 and so on till you reach the position which has N.
When you travel from Arr[i] to Arr[j], the distance travelled is | i– j |.
Find the total distance you have to travel to reach N when you start from 1.
Example 1:
Input:
N = 5
Arr[] = {5, 1, 4, 3, 2}
Output: 7
Explanation: The numbers and their respective 
indices are given below:
1->1
2->4
3->3
4->2
5->0
Total distance =|4-1|+|3-4|+|2-3|+|0-2| 
= 3+1+1+2 = 7.
Example 2:
Input:
N = 6
Arr[] = {6, 5, 1, 2, 4, 3}
Output: 8
Explanation: 
Total distance = |2-3|+|3-5|+|5-4|+|4-1|+|1-0| 
= 1+2+1+3+1 = 8.
Your Task:
You don't need to read input or print anything. Your task is to complete the function distance() which takes the array of integers arr[] and its size n as input parameters and returns the total distance.
 
Expected Time Complexity: O(N)
Expected Auxiliary Space: O(N)
Constraints:
1 <= N <= 10^{7}
1<= Arr_{i }<= N

Starter code:
```python
#User function Template for python3



class Solution:

    def distance(self, arr, n):

        # code here
```
