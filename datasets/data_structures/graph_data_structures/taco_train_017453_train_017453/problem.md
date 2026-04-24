Due to the second wave of Gorona virus, Geekland imposed another lockdown and Geek has gained some wieght. Now Geek has decided to exercise.
There are N intersections in the city numbered from 0 to N-1 and M bidirectional roads each road connecting two intersections. All the intersections are connected to each-other through some set of roads, i^{th} road connect intersections A[i][0] and A[i][1] and is of length A[i][2].
Every morning Geek will start at intersection src and will run/walk upto intersection dest. Geek only has one hour in the morning so he will choose to cover the shortest path from src to dest.
After planning his exercising schedule, Geek wants to buy the perfect shoes to walk/run in the morning. He goes to Neeman's Shoe factory which is the National Shoe factory of Geekland. 
Geek sees that there are two types of shoes "Neeman's Wool Joggers" and "Neeman's Cotton Classics", "Neeman's Wool Joggers" are good for running and "Neeman's Cotton Classics" are good for walking.
Geek is confused which shoes to buy, so he comes up with a strategy. If the distance he has to cover in the morning is less than or equal to X, then he will walk the distance, therefore he will buy "Neeman's Cotton Classics". If the distance is greater than X, he will buy "Neeman's Wool Joggers". Geek is too lazy to calculate the shortest distance between two intersections src and dest. Help him decide which shoes to buy.
 
Example 1: 
Input:
N = 3, M = 2, src = 0, dest = 2, X = 5
A[][] = {{0, 1, 3},
         {1, 2, 3}}
Output:
Neeman's Wool Joggers
Explanation: 
Shortest path from src to dest is 6 
which is greater than X, hence Geek will
buy "Neeman's Wool Joggers".
 
Example 2: 
Input: 
N = 3, M = 2, src = 0, dest = 2, X = 6 
A[][] = {{0, 1, 3},
         {1, 2, 3}} 
Output: 
Neeman's Cotton Classics 
Explanation: 
Shortest path from src to dest is 6
which is not greater than X, hence Geek 
will Ã¢â¬â¹buy "Neeman's Cotton Classics".
Your Task:
You don't need to read input or print anything. Your task is to complete the function exercise( ) which takes N, M, A[ ][ ], src, dest and X as input parameters and returns string representing the shoes he selects. Either "Neeman's Wool Joggers" or "Neeman's Cotton Classics".
Expected Time Complexity: O((N + M) * Log(M))
Expected Auxiliary Space: O(N + M)
Constraints:
2 ≤ N ≤ 10^{4}
1 ≤ M ≤ min((N*(N-1))/2, 2*10^{5})
0 ≤ A[i][0], A[i][1] < N
0 ≤ src, dest < N
1 ≤ A[i][2], X ≤ 10^{9}

Starter code:
```python
#User function Template for python3

class Solution:
    def exercise(self, N, M, A,src, dest,X):
        # code here
```
