Hattori is very much inspired by the way GMAIL works. He decides to build his own simple version of GMAIL. He divides the mails into 3 categories ,namely : UNREAD , READ and TRASH.
UNREAD:the messages that haven't been read.
READ:The messages that is read by the user.
TRASH: The messages deleted by the user.
Now, At any point of time, The user can READ an UNREAD message , Move an UNREAD message to TRASH , Move a READ message to TRASH or restore a deleted message back to READ category.Now , Hattori requires your help in determining the messages left in all the categories aligned in the order of their arrival in that category.
Formally: You are given N messages , with ID from 1 to N. Initially all the messages are in the UNREAD section of the mail.Now, Q queries are given in the form as shown below:
1 X : Move the message with ID X from UNREAD to READ.
2 X : Move the message with ID X from READ to TRASH.
3 X : Move the message with ID X from UNREAD to TRASH.
4 X : Move the message with ID X from TRASH to READ.
Given that all the queries are valid, Help Hattori in Determining the messages in all the 3 sections. There are N mails initially having id's from 1 to N. Then there are total Q querieseach in the form mentioned in the question. The queries are mentioned in a list query where ith query is represented by (2*i)thand (2*i+1)th value of the list.Example 1:Input: N = 10, Q = 7query = {1, 2, 1, 5, 1, 7, 1, 9,         2, 5, 2, 7, 4, 5}Output: UNREAD - 1 3 4 6 8 10READ - 2 9 5TRASH - 7Explaination: Initial:UNREAD section: 1 2 3 4 5 6 7 8 9 10READ section : EMPTYTRASH section : EmptyQuery 1 : 1 2UNREAD section: 1 3 4 5 6 7 8 9 10READ section : 2TRASH section : EmptyQuery 2 : 1 5UNREAD section: 1 3 4 6 7 8 9 10READ section : 2 5TRASH section : EmptyQuery 3 : 1 7UNREAD section: 1 3 4 6 8 9 10READ section : 2 5 7TRASH section : EmptyQuery 4 : 1 9UNREAD section: 1 3 4 6 8 10READ section : 2 5 7 9TRASH section : EmptyQuery 5 : 2 5UNREAD section: 1 3 4 6 8 10READ section : 2 7 9TRASH section : 5Query 6 : 2 7UNREAD section: 1 3 4 6 8 10READ section : 2 9TRASH section : 5 7Query 7 : 4 5UNREAD section: 1 3 4 6 8 10READ section : 2 9 5TRASH section : 7Your Task:
You do not need to read input or print anyting. Your task is to complete the function mailDesign() which takes N, Q and query as input parameters and returns a list containing the starting pointer of the three linked lists unread, read and trash. If any linked list is empty pass a null pointer as the head of that list.Expected Time Complexity: O(Q*N)
Expected Auxiliary Space: O(N)Constraints:
1 < N, Q < 1000

Starter code:
```python
#User function Template for python3
# Given below is the structure of Node class
# list moves from left to right
# class node:
#     def __init__(self):
#         self.data = None
#         self.left = None
#         self.right = None

class Solution:
    def mailDesign(self, N, Q, query):
        # code here
```
