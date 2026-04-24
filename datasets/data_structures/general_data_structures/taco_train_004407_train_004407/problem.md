Given a singly linked list of size N. Your task is to complete the function alternatingSplitList() that splits the given linked list into two smaller list. The sublists should be made from alternating elements from the original list.
Note: the sublist should in the order with respect to original list.
Input Format:
First line of input contains number of testcaes T. First line of each input contains length of the linked list and next line contains the elements of the linked list.
Output Format:
For each test case, in new lines, print the two sublists formed after the split.
User Task:
The task is to complete the function alternatingSplitList() which takes the head as parameter and splits the lists into two. The head of the first list should be stored in the provided variable a, and the head of the second should be stored in the provided variable b. The printing is done by the driver code.
Constraints:
1 <= T <= 100
1 <= N <= 100
Example:
Input:
2
6
0 1 0 1 0 1
5
2 5 8 9 6
Output:
0 0 0
1 1 1
2 8 6
5 9
Explanation:
Testcase 1: After forming two sublists of the given list as required, we have two lists as: 0->0->0 and 1->1->1.

Starter code:
```python
#User function Template for python3



'''

class Node:

    def __init__(self, data):

        self.data = data

        self.next = None



'''



'''

These are global variables to store heads of split lists

a --- store head of first list

b --- store head of second list

'''



def alternatingSplitList(head):

    global a,b

    #Your code here
```
