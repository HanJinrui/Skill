Given a piece of code, the task is to remove all the comments from the code.
Note: 
Comments formats can be " /*...*/ " and " //... \n".
Comments cannot be nested.
Example 1:
Input:
code =
#include int main(int *argc,char **argv)
{ // First line of code\n 
printf("Hello World!!! "); return 0; }
Output:
#include int main(int *argc,char **argv)
{  printf("Hello World!!! "); return 0; }
Explanation: Removed the commented area
starting with // and ending with \n.
Example 2:
Input: 
code =
#include int main(int *argc,char **argv)
{ /* First line of code Printing
Hello World */ 
printf("Hello World!!! "); return 0; }
Output:
#include int main(int *argc,char **argv)
{  printf("Hello World!!! "); return 0; }
Explanation: Removed the commented area
starting with /* and ending with */.
Your Task:
You don't need to read input or print anything. Your task is to complete the function removeComments() which takes the string of code as input and returns the updated string of code after removing all the comments from it.
Expected Time Complexity: O(|code|)
Expected Auxiliary Space: O(1).
Constraints:
4 <= |code| <= 100000
|code| denotes the length of the string code.

Starter code:
```python
#User function Template for python3

class Solution:

	def removeComments (self, code):

		# your code here
```
