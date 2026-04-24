Given an array, Arr of N numbers, and another number target, find three integers in the array such that the sum is closest to the target. Return the sum of the three integers.
Note: If there are multiple solutions, print the maximum one.
Example 1:
Input:
N = 6, target = 2
A[] = {-7,9,8,3,1,1}
Output: 2
Explanation: There is one triplet with sum
2 in the array. Triplet elements are -7,8,
1 whose sum is 2.
Example 2:
Input:
N = 4, target = 13
A[] = {5,2,7,5}
Output: 14
Explanation: There is one triplet with sum
12 and other with sum 14 in the array.
Triplet elements are 5, 2, 5 and 2, 7, 5
respectively. Since abs(13-12) ==
abs(13-14) maximum triplet sum will be
preferred i.e 14.
Your Task:
Complete threeSumClosest() function and return the expected answer.
Expected Time Complexity: O(N*N).
Expected Auxiliary Space: O(1).
Constraints:
3 ≤ N ≤ 10^{3}
-10^{5} ≤ A[i] ≤ 10^{5}
1 ≤ target ≤ 10^{5}

Starter code:
```python
#User function Template for python3



# arr    : list of integers denoting the elements of the array

# target : as specified in the problem statement



class Solution:

    def threeSumClosest (self, arr, target):

    # Your Code Here
```
