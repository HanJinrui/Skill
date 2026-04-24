There are N trees in a circle. Each tree has a fruit value associated with it. A bird has to sit on a tree for 0.5 sec to gather all the fruits present on the tree and then the bird can move to a neighboring tree. It takes the bird 0.5 seconds to move from one tree to another. Once all the fruits are picked from a particular tree, she cant pick any more fruits from that tree. The maximum number of fruits she can gather is infinite.
Given N and M (the total number of seconds the bird has), and an array arr[] containing the fruit values of the trees. Maximize the total fruit value that the bird can gather. The bird can start from any tree.
 
Example 1:
Input:
N=7 M=3
arr[] = { 2 ,1 ,3 ,5 ,0 ,1 ,4 }
Output: 9
Explanation: 
She can start from tree 1 and move
to tree2 and then to tree 3.
Hence, total number of gathered fruits
= 1 + 3 + 5 = 9.
 
Example 2:
Input:
N=6 M=2
arr[] = { 1, 6, 2, 5, 3, 4 }
Output: 8
Explanation: 
She can start from tree 1 and move 
to tree 2. In this case she will gather
6 + 2 = 8 fruits. She can also start 
from tree 3 and move to tree 4. In this
case, too, she will gather 5 + 3 = 8 
fruits.
 
Your Task:
You don't need to read input, or print anything. You just need to complete the function maxFruits() that takes array arr, integer N and integer M as parameters and returns the maximum number of fruits she can gather.
 
Expected Time Complexity: O(N).
Expected Auxiliary Space: O(1).
 
Constraints:
2 ≤ N ≤ 10^{6}

Starter code:
```python
#User function Template for python3



class Solution:

    def maxFruits(self,arr,n,m):
```
