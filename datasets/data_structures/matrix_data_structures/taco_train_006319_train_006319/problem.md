An Encryption algorithm works in the following way
Message: eNEMYwILLaTTACK
Enrypted Form: eYLA NwaC EITK MLT
The way to do it is that the number of rows and the number of columns in the figure (formed from the alphabets of the Message) lie between floor (sqrt(len(message))) and ceil (sqrt(len(message))). It also states that the number of rows is less than or equal to the number of columns, and that the area of rectangle thus formed is minimum. Based on the this criteria, we have to choose a set of values for rows and columns.
For the string haveaniceday, we have floor(sqrt(len(message))) = 3 and ceil(sqrt(len(message))) = 4.
3 * 3 = 9 < len(message) = 15
3 * 4 = 12 = len(message)
4 * 3 = 12 = len(message)
4 * 4 = 16 > len(message)
Out of the 4 possible squares, we can see that, rows = 3 and columns = 4 is the best fit.
On building the figure, we get
have
anic
eday
So, the Encrypted form is "hae and via ecy".
 
Example 1:
Input:
S = "eNEMYwILLaTTACK"
Output:
eYLA NwaC EITK MLT
Explanation:
The encrypted form of the given String
is printed.
Example 2:
Input:
S = "SavetheMines"
Output:
Sti ahn vee eMs
Explanation:
The encrypted form of the given String
is printed.
 
Your Task:
You don't need to read input or print anything. Your task is to complete the function encryptString() which takes an String S as input and returns the encrypted form as a String.
 
Expected Time Complexity: O(|S|)
Expected Auxiliary Space: O(1)
 
Constraints:
1 <= |S| <= 10^{5}

Starter code:
```python
#User function Template for python3



class Solution:

    def encryptString(self, S):

        # code here
```
