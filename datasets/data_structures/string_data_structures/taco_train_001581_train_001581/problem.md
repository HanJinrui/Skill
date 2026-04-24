Given an input stream of N integers (alongwith the operation on these integers), the task is to print the number of the distinct elements in the stream after each operation.
The array is will be having positive and negative values. Positive value meaning you have to append it into your database and Negative value means you have to remove it from your database if present and at every step you have to count the number of distinct character in your database.
Example 1:
Input: A[] = {5, 5, 7, -5, -7, 1, 2, -2}
Output: 1 1 2 2 1 2 3 2
Explanation:
Here you can see we have an array of integer as 
stated that positive number means we will adding 
it to our database and negative means we will be 
deleting one occurence of that number from our database.
So, [5, 5, 7, -5, -7, 1, 2, -2] 
Add 5, Unique Value in Data Base is 1 -> [5]
Add 5, Unique Value in Data Base is 1 -> [5, 5]
Add 7, Unique Value in Data Base is 2 -> [5, 5, 7]
Removing 5, Unique Value in Data Base is 2 -> [5, 7]
Removing 7, Unique Value in Data Base is 1 -> [5]
Add 1, Unique Value in Data Base is 2 -> [5, 1]
Add 2, Unique Value in Data Base is 3 -> [5, 1, 2]
Removing 2, Unique Value in Data Base is 2 -> [5, 1]
Your Task:
This is a function problem. The input is already taken care of by the driver code. You only need to complete the function maxDistinctNum() that takes an array (arr), sizeOfArray (n), and return the number of unique value at every instance. The driver code takes care of the printing.
Expected Time Complexity: O(N).
Expected Auxiliary Space: O(N).
 
Input:
First line of the input contains an integer T denoting the number of test cases. Then T test case follows. First line of each test case contains an integer N denoting the number of operations to be performed on a stream. Next N lines two space separated elements, the operation to be performed and the key element.
Constraints:
1 ≤ N ≤ 10^{6}
-10^{6} ≤ A[] ≤ 10^{6}

Starter code:
```python
#User function Template for python3



def maxDistinctNum (self, arr,  n) : 

    # Complete the function
```
