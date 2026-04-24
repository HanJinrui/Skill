Serialization is to store a tree in an array so that it can be later restored and Deserialization is reading tree back from the array. Now your task is to complete the function serialize which stores the tree into an array A[ ] and deSerialize which deserializes the array to the tree and returns it.
Note: The structure of the tree must be maintained. Multiple nodes can have the same data.
Example 1:
Input:
      1
    /   \
   2     3
Output: 2 1 3
Example 2:
Input:
         10
       /    \
      20    30
    /   \
   40  60
Output: 40 20 60 10 30
Your Task:
The task is to complete two functions serialize which takes the root node of the tree as input and stores the tree into an array and deSerialize which deserializes the array to the original tree and returns the root of it.
Expected Time Complexity: O(N).
Expected Auxiliary Space: O(N).
Constraints:
1 <= Number of nodes <= 1000
1 <= Data of a node <= 1000

Starter code:
```python
#User function Template for python3





'''

class Node:

    def __init__(self,val):

        self.data = val

        self.left = None

        self.right = None

'''



#Function to serialize a tree and return a list containing nodes of tree.

def serialize(root, A):

    #code here



#Function to deserialize a list and construct the tree.   

def deSerialize(A):

    #code here
```
