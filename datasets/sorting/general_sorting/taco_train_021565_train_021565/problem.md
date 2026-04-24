Given two arrays X and Y of positive integers, find the number of pairs such that x^{y} > y^{x} (raised to power of) where x is an element from X and y is an element from Y.
Example 1:
Input: 
M = 3, X[] = [2 1 6] 
N = 2, Y[] = [1 5]
Output: 3
Explanation: 
The pairs which follow x^{y} > y^{x} are 
as such: 2^{1} > 1^{2},  2^{5} > 5^{2} and 6^{1} > 1^{6 .}
Example 2:
Input: 
M = 4, X[] = [2 3 4 5]
N = 3, Y[] = [1 2 3]
Output: 5
Explanation: 
The pairs for the given input are 
2^{1 }> 1^{2} , 3^{1} > 1^{3 }, 3^{2} > 2^{3} , 4^{1} > 1^{4} , 
5^{1} > 1^{5 }.
Your Task:
This is a function problem. You only need to complete the function countPairs() that takes X, Y, M, N as parameters and returns the total number of pairs.
Expected Time Complexity: O((N + M)log(N)).
Expected Auxiliary Space: O(1).
Constraints:
1 ≤ M, N ≤ 10^{5}
1 ≤ X[i], Y[i] ≤ 10^{3}

Starter code:
```python
#User function Template for python3



class Solution:

    

     #Function to count number of pairs such that x^y is greater than y^x.     

    def countPairs(self,a,b,M,N):

        #code here
```
