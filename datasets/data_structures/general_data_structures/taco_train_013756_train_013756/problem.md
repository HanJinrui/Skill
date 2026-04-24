Given a singly linked list of size N containing only English Alphabets. Your task is to complete the function arrangeC&V(), that arranges the consonants and vowel nodes of the list it in such a way that all the vowels nodes come before the consonants while maintaining the order of their arrival.
Input:
The function takes a single argument as input, the reference pointer to the head of the linked list. There will be T test cases and for each test case the function will be called separately.
Output:
For each test case output a single line containing space separated elements of the list.
User Task:
The task is to complete the function arrange() which should arrange the vowels and consonants as required.
Constraints:
1 <= T <= 100
1 <= N <= 100
Example:
Input:
2
6
a e g h i m
3
q r t
Output:
a e i g h m
q r t
Explanation:
Testcase 1: Vowels like a, e and i are in the front, and consonants like g, h and m are at the end of the list.

Starter code:
```python
#User function Template for python3



"""

# Node Class



class node:

    def __init__(self, val):

        self.data = val

        self.next = None



"""



class Solution:

    #Function to reverse a linked list.

    def arrangeCV(self, head):

        # Code here
```
