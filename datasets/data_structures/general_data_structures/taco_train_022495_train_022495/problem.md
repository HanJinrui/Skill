IPL 2021 knockouts are over, teams MI, CSK, DC, and RCB are qualified for the semis. 
Today is matchday 6 and it is between Delhi Capitals and Royal Challengers Banglore. Glenn Maxwell of RCB playing flawlessly. Rishabh Pant, the new captain of the team who is also a wicket-keeper wants to send a message to the bowler. But, he can't shout message directly as a batsman can hear. So, he decided to encrypt the message by putting '*'s in the message. And this is how the bowler decrypts the message. Bowler iterates over the message string from left to right, if he finds a '*', he removes it and adds all the letters read so far to the message. He keeps on doing this till he gets rid of all the '*'. Given a decrypted message in the form of the string, the task is to find the encrypted message.
Note: If the string can be encrypted in multiple ways, find the encrypted string of smallest length.
Example 1:
Input: s = "ababcababcd"
Output: ab*c*d
Explanation: We can encrypt the string 
in following way : "ababcababcd" -> 
"ababc*d" -> "ab*c*d"
Example 2:
Input: s = "zzzzzzz"
Output: z*z*z
Explanation: The string can be encrypted 
in 2 ways: "z*z*z" and "z**zzz". Out of 
the two "z*z*z" is smaller in length.
Your Task: 
You don't need to read input or print anything. Complete the function compress() which takes the message string s as input parameter and returns the shortest possible encrypted string.
Constraints: 
1 ≤ |s| ≤ 10^{5}

Starter code:
```python
#User function Template for python3



class Solution:

    def compress(self, s):

        # Your code goes here
```
