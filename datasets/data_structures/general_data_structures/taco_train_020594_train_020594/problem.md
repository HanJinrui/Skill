Given a singly linked list L_{0} -> L_{1} -> … -> L_{n-1} -> L_{n}. Rearrange the nodes in the list so that the new formed list is: L_{0} -> L_{n} -> L_{1} -> L_{n-1} -> L_{2} -> L_{n-2}.
Input:
You have to complete the method which takes 1 argument: the head of the  linked list. You should not read any input from stdin/console. There are multiple test cases. For each test case, this method will be called individually.
Output:
Your function should return a pointer to the rearranged list so obtained.
User Task:
The task is to complete the function inPlace() which should rearrange the given linked list as required.
Constraints:
1 <=T<= 50
1 <= size of linked lists <= 100
Example:
Input:
2
4
1 2 3 4
5
1 2 3 4 5 
Output:
1 4 2 3
1 5 2 4 3
Explanation:
Testcase 1: After rearranging the linked list as required, we have 1, 4, 2 and 3 as the elements of the linked list.

Starter code:
```python
#User function Template for python3

def inPlace(root):
    #code here
```
