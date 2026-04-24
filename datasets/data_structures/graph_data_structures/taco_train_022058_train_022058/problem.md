Influenced by Social Networking sites, Rahul launches his own site Friendsbook. Each user in Friendsbook is given a unique number, first user being numbered 1. There are N users in Friendsbook numbered from 1 to N. In Friendsbook, i th user can make j th user his friend without becoming his friend himself, i.e. in Friendsbook, there is a one-way link rather than a two-way link as in Facebook. Moreover i th user can make j th user his friend iff i>j. Also one user should have no more and no less than one friend except user 1 who will have no friend. Rahul wants to modify Friendsbook and find out whether one user is somehow linked to some other user. Help Rahul do so.
Print all possible connections between the users in the following format: 
4 2 2 means 4 is linked to 2 via 2 connections.
5 2 3 means 5 is linked to 2 via 3 connections, and so on.
The order of display should be as follows:
Print all possible connections starting from user 2 to user N with other users starting from 1 to The Current User Number - 1. In case one user is not connected at all with another user, that connection should not be printed.
 
Example 1:
Input: 
N = 3
arr[] = {1, 2}
Output:
2 1 1 3 1 2 3 2 1
Explanation:
2 is directly linked to 1 and hence 2 is
linked to 1 via 1 connection. 3 is directly
linked to 2 which in turn is directly
linked to 1. Hence 3 is linked to 1 via 
2 connections and to 2 via 1 connection.
Example 2:
Input: 
N = 3
arr[] = {1, 1}
Output:
2 1 1 3 1 1
Explanation:
Both 2 and 3 are directly linked to 1.
Hence both 2 and 3 are linked to 1 via
1 connection.
 
Your Task:
You don't need to read input or print anything. Your task is to complete the function socialNetwork() which takes an Integer N and an array arr[] of N-1 integers as input and returns s string representing the answer.
 
Expected Time Complexity: O(N^{2})
Expected Auxiliary Space: O(N^{2})
 
Constraints:
2 <= N <= 500
1 <= arr[i] <= i

Starter code:
```python
#User function Template for python3

class Solution:
    def socialNetwork(self, arr, N):
        # code here
```
