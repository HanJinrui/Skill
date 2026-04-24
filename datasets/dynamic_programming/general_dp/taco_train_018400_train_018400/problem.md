Given two strings S1 and S2 of lower alphabet characters of length N1 and N2, we need to find the number of ways to insert a character in the first string S1 such that length of LCS of both strings increases by one.
Example 1:
Input:
N1 = 4
S1 = abab
N2 = 3
S2 = abc
Output:
3
Explanation:
LCS length of given two 
strings is 2. There are 3 
ways of insertion in str1,to 
increase the LCS length by 
one which are enumerated below, 
str1 = “abcab” str2 = “abc” LCS length = 3 
str1 = “abacb” str2 = “abc” LCS length = 3 
str1 = “ababc” str2 = “abc” LCS length = 3
Example 2:
Input:
N1 = 6
S1 = abcabc
N2 = 4
S2 = abcd
Output:
4
Explanation:
LCS length of given two
strings is 3. There are 4
ways of insertion in str1,to
increase the LCS length by
one which are enumerated below,
str1 = “abcdabc” str2 = “abcd” LCS length = 4
str1 = “abcadcb” str2 = “abcd” LCS length = 4
str1 = “abcabdc” str2 = “abcd” LCS length = 4
str1 = “abcabcd” str2 = “abcd” LCS length = 4
Your Task:
You don't need to read input or print anything. Your task is to complete the function waysToIncreaseLCSBy1() which take string S1 and string S2 of length N1 and N2 respectively as input parameters and returns the number of ways to insert a character in the first string S1 such that length of LCS of both strings increases by one.
Expected Time Complexity: O(N1 * N2) 
Expected Space Complexity: O(N1 * N2)
Constraints:
1<= N1, N2 <=100
S1 and S2 contains lower case English character

Starter code:
```python
#User function Template for python3


class Solution:
    def waysToIncreaseLCSBy(self,N1,S1,N2,S2):
        # code here
```
