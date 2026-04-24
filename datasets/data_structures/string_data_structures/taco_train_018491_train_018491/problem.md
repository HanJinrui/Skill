Trie is an efficient information retrieval data structure. Use this data structure to store Strings and search strings. Your task is to use TRIE data structure and search the given string A. If found print 1 else 0.
Example 1:
Input:
N = 8
key[] = {the,a,there,answer,any,by,
         bye,their}
search = the
Output: 1
Explanation: the is present in the given
string "the a there answer any by bye
their"
Example 2:
Input:
N = 8
key[] = {the,a,there,answer,any,by,
         bye,their}
search = geeks
Output: 0
Explanation: geeks is not present in the
given string "the a there answer any by
bye their"
Your Task:
Complete insert and search function and return true if key is present in the formed trie else false in the search function. (In case of true, 1 is printed and false, 0 is printed by the driver's code.
Expected Time Complexity: O(M+|search|).
Expected Auxiliary Space: O(M).
M = sum of the length of all strings which is present in the key[] 
|search| denotes the length of the string search.
Constraints:
1 <= N <= 10^{4}
1 <= |input strings|, |A| <= 100

Starter code:
```python
#User function Template for python3



"""

class TrieNode: 

      

    def __init__(self): 

        self.children = [None]*26

  

        # isEndOfWord is True if node represent the end of the word 

        self.isEndOfWord = False

"""

#Function to insert string into TRIE.

def insert(root,key):

    

    #code here



#Function to use TRIE data structure and search the given string.

def search(root, key):

    

    #code here
```
