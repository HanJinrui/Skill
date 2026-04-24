Kamar-taj is a place where "The Ancient One" trains people to protect earth from other dimensions.
The earth is protected by N sanctums, destroying any of it will lead to invasion on earth.
The sanctums are connected by M bridges.
Now , you being on dormammu's side , want to find the number of sanctum destroying which will disconnect the sanctums.
Example 1:
Input:
N = 5, M = 5
arr[] = {{1,2},{1,3},{3,2},{3,4},{5,4}}
Output : 2
Explanation:
1.Removing 1 will not make graph disconnected
(2--3--4--5).
2.Removing 2 will also not make 
graph disconnected(1--3--4--5).
3.Removing 3 makes graph disconnected 
(1--2 and 4--5).
4.Removing 4 makes graph disconnected 
(1--2--3--1 and 5).
5.Removing 5 also doesn't makes 
graph disconnected(3--1--2--3--4).
6. Therefore,there are two such vertices,
3 and 4,so the answer is 2.
Example 2:
Input : 
N = 2, M = 1 
arr[] = {{1, 2}}
Output : 0
Your Task:
This is a function problem. The input is already taken care of by the driver code. You only need to complete the function doctorStrange() that takes a number of nodes (N), a number of edges (M), a 2-D matrix that contains connection between nodes (graph), and return the number of sanctums when destroyed will disconnect other sanctums of Earth. 
Expected Time Complexity: O(N + M).
Expected Auxiliary Space: O(N + M).
 
Constraints:
1 ≤ n ≤ 30000
1 ≤ m ≤ 30000
1 ≤ u, v ≤ n

Starter code:
```python
#User function Template for python3





class Solution:

    def doctorStrange (self,n, k, g) : 

        #Complete the function
```
