Given an array arr of N integers, write a function that returns true if there is a triplet (a, b, c) that satisfies a^{2} + b^{2} = c^{2}, otherwise false.
Example 1:
Input:
N = 5
Arr[] = {3, 2, 4, 6, 5}
Output: Yes
Explanation: a=3, b=4, and c=5 forms a
pythagorean triplet.
Example 2:
Input:
N = 3
Arr[] = {3, 8, 5}
Output: No
Explanation: No such triplet possible.
Your Task:
Complete the function checkTriplet() which takes an array arr, single integer n, as input parameters and returns boolean denoting answer to the problem. You don't to print answer or take inputs. 
Note: The driver will print "Yes" or "No" instead of boolean.
Expected Time Complexity: O(max(Arr[i])^{2})
Expected Auxiliary Space: O(max(Arr[i]))
Constraints:
1 <= N <= 10^{7}
1 <= Arr[i] <= 1000

Starter code:
```python
#User function Template for python3

class Solution:



	def checkTriplet(self,arr, n):

    	# code here
```
