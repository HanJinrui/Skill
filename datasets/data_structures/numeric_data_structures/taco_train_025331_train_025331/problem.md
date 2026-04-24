Sid is a superior salesperson. So he gets a task from his boss. The task is that he will be given some number of products say k (All the products are same) and he has to travel N cities [1...N] to sell them. The main objective of the task is that he has to try to sell the product at higher price than previous city. For example if he sells a product at 100 Rs in one city then he has to try to sell the next product greater than 100 Rs in the next city and so on.
He travels all the cities and write down all the selling amounts. Now He wants to calculate maximum number of cities in which he could follow this increasing trend. And the maximum total prime money he could make in those cities. Help him in  finding this.
Note : Number of products will always be equal to number of cities. 
 
Example 1:
Input:
N = 9
A[] = {4, 2, 3, 5, 1, 6, 7, 8, 9}
Output:
5 7
Explanation:
5 cities are maximum number of 
cities in which the trend 
followed, And  amount in those 
cities were 1, 6, 7, 8, 9. 
Out of  these  amounts only 
7 is prime money.
 
Example 2:
Input:
N = 10
A[] = {2, 3, 5, 7, 4, 1, 6, 5, 4, 8}
Output:
4 17
Explanation:
4 cities are maximum number of 
cities in which the trend 
followed, And  amount in those 
cities were 2, 3, 5, 7. 
Out of  these amounts, maximum
total prime money is 2+3+5+7=17.
 
Example 3:
Input:
N = 5
A[] = {2, 2, 2, 2, 2}
Output:
1 2
Explanation:
He was successful in one city 
only, And maximum total prime 
money is 2.
 
Your Task:  
You don't need to read input or print anything. Your task is to complete the function primeMoney() which takes the array A[] and its size N as inputs and returns the maximum number of cities and maximum total prime money as a pair. 
Expected Time Complexity: O(N. sqrt(N))
Expected Auxiliary Space: O(N)
 
Constraints:
1 ≤ N ≤ 10^{5}
1 ≤ A[i] ≤ 10^{5 }

Starter code:
```python
#User function Template for python3

class Solution:
    def primeMoney(self, arr, n):
        # return (0,0)
```
