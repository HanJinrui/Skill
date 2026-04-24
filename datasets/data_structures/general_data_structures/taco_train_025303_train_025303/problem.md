Given a circular linked list, your task is to complete the method printList() that prints the linked list.
Input:
The printList function takes a single argument as input the reference pointer to the head of the linked list.
There are multiple test cases and for each test, the function will be called separately. 
Output: You just need to print the LinkedList in the same line and the next line will be added by the Driver Code.
Example:
Input:
2
7
374 363 171 497 282 306 426
2
162 231
Output:
426 306 282 497 171 363 374
231 162
Note : Input items are inserted at the front of linked list that is why output is in reverse order.
Constraints:
1<=T<=50
1<=N<=50

Starter code:
```python
class Node: 

      

    # Constructor to create  a new node 

    def __init__(self, data): 

        self.data = data  

        self.next = None

  

class CircularLinkedList: 

      

    # Constructor to create a empty circular linked list 

    def __init__(self): 

        self.head = None

  

    # Function to insert a node at the beginning of a 

    # circular linked list 

    def push(self, data): 

        ptr1 = Node(data)

        ptr1.data=data

        temp = self.head 

          

        ptr1.next = self.head 

  

        # If linked list is not None then set the next of 

        # last node 

        if self.head is not None: 

            while(temp.next != self.head): 

                temp = temp.next 

            temp.next = ptr1 

  

        else: 

            ptr1.next = ptr1 # For the first node 

  

        self.head = ptr1  

  

    # Function to print nodes in a given circular linked list 

    def printList(self): 

        

        # Write your code here

        return
```
