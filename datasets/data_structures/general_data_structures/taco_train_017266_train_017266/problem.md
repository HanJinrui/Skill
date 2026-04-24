Given an array arr[] and a number k. The task is to delete k elements which are smaller than next element (i.e., we delete arr[i] if arr[i] < arr[i+1]) or become smaller than next because next element is deleted.
Example 1:
Ã¢â¬â¹Input : arr[ ] = {20, 10, 25, 30, 40} 
        and K = 2
Output : 25 30 40
Explanation:
First we delete 10 because it follows 
arr[i] < arr[i+1]. Then we delete 20 
because 25 is moved next to it and it 
also starts following the condition.
Ã¢â¬â¹Example 2:
Input : arr[ ] = {3, 100, 1} and K = 1
Output :  100 1 
 
Your Task:
This is a function problem. The input is already taken care of by the driver code. You only need to complete the function deleteElement() that takes an array (arr), sizeOfArray (n), an integer K and return the array arr[] after deleting the k elements from the array if possible, else print the left array as it is. The driver code takes care of the printing.
Expected Time Complexity: O(N).
Expected Auxiliary Space: O(N).
 
Constraints:
2 ≤ N ≤ 10^{5}
1 ≤ K < N

Starter code:
```python
#User function Template for python3



def deleteElement (arr, n, k) : 

    #Complete the function
```
