Rahul is a geek. Head is the lucky call for him. You have to make him lucky. You are provided N coins. If the coin is heads facing upwards it means he is lucky else unlucky, your task is to do an operation to make him lucky. Operation allowed is as follows :
Starting from first element, if you find any coin heads facing downwards (Tail), flip the coin at i^{th} index and (i+1)^{th} index.  
 
Example 1:
Input:
5
H T H T H
Output:
2
2 3
Explanation:
Coins at index 2 and 3 needs to
be flipped to make Rahul happy.
Example 1:
Input:
3
H H H
Output:
0
Explanation:
No index to be flipped.
 
 
Your Task:  
You don't need to read input or print anything. Your task is to complete the function flippedIndexes() which takes the char array A[], its size N and a getAnswer[]  array as inputs and returns the count of the number of indexes to be flipped and stores the indexes in the getAnswer[] array.
Note:- If count is zero, you don't need to store anything in the getAnswer[] array.
Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)
 
Constraints:
1 ≤ N ≤ 10^{7}
A[i] = {'H', 'T'}

Starter code:
```python
#User function Template for python3

class Solution:
    def flippedIndexes(self, a, n, getAnswer):
        # Your code goes here
```
