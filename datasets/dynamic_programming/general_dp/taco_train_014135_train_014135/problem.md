We have an array a[] of N stones of various heights laid out in a row. By taking some consecutive section of the stones, we wish to form a pyramid, where the height of the stones start from 1, increase by 1, until it reaches some value x, then decreases by 1 until it reaches 1 again i.e. the stones should be 1, 2, 3, 4…x – 1, x, x – 1, x – 2 … 1. All other stones not part of the pyramid should have a height 0. We cannot move any of the stones from their current position, however, by paying a fee of 1, we can reduce the heights of the stones. We wish to minimize the cost of building a pyramid. Output the minimum cost to build this pyramid. Assume that always a pyramid would be made of the input elements.
 
Example 1: 
Input:
N = 6
a[] = {1, 2, 3, 4, 2, 1}
Output:
4
Explanation:
We can obtain the array {1, 2, 3, 2, 1, 0}
by substracting 2 out of 4, 1 out of 2,
and 1 out of 1. In total, we will substract 4.
Example 2: 
Input:
N = 3
a[] = {1, 2, 1}
Output:
0
Explanation:
The array is already in Pyramid form.
 
Your Task:
You don't need to read input or print anything. Your task is to complete the function pyramidForm() which takes an Integer N and an array a[] as input and returns the minimum cost.
 
Expected Time Complexity: O(1)
Expected Auxiliary Space: O(1)
 
Constraints:
1 <= N <= 10^{5}
1 <= a[i] <= 10^{5}

Starter code:
```python
#User function Template for python3



class Solution:

    def pyramidForm(self, a, N):

        # code here
```
