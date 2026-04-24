Given a array, write a program to construct a triangle where last row contains elements of given array, every element of second last row contains sum of below two elements and so on.
Example 1:
Input:
A[] = {4, 7, 3, 6, 7};
Output:
81 40 41 21 19 22 11 10 9 13 4 7 3 6 7
Explanation:
       81
     40  41
   21  19  22
 11  10   9   13
4   7   3   6    7 
 
Example 2:
Input:
A[] = {5, 8, 1, 2, 4, 3, 14}
Output:
200 98 102 55 43 59 34 21 22 37 22
12 9 13 24 13 9 3 6 7 17 5 8 1 2 4 3 14 
 
Your Task:  
You don't need to read input or print anything. Your task is to complete the function getTriangle() which takes the array A[] and its size N as inputs and returns the sum triangle.
 
Expected Time Complexity: O(N^{2})
Expected Auxiliary Space: O(N^{2})
 
Constraints:
1<=N<=1000
1<=Ai<=1000
Elements in the triangle will not exceed 10^{18}

Starter code:
```python
#User function Template for python3

def getTriangle( arr, n):
```
