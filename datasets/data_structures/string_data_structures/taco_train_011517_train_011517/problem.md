Given a string S. Let k be the maximum number of partitions possible of the given string with each partition starts with a distinct letter. The task is to find the number of ways string S can be split into k partition (non-empty) such that each partition starts with a distinct letter. Print number modulo 1000000007.
Note : S consists of lowercase letters only.
 
Example 1:
Input:
S = "abb"
Output:
2
Explanation:
 "abb" can be maximum split into 2 partitions
{a, bb} with distinct starting letter, for k = 2.
And, the number of ways to split "abb"
into 2 partitions with distinct starting letter
are 2 {a, bb} and {ab, b}.
Example 2:
Input:
S = "abbcc"
Output:
4
Explanation:
"abbcc" can be maximum split into 3 partitions
with distinct letter, so k=3. Thus the number
of ways to split "abbcc" into 3 partitions with
distinct letter is 4 i.e. {ab, b, cc},
{ab, bc, c},{a, bb, cc} and {a, bbc, c}. 
 
Your Task:
You don't need to read input or print anything. Your task is to complete the function waysToSplit() which takes a String S and returns the answer.
 
Expected Time Complexity: O(|S|)
Expected Auxiliary Space: O(|1|)
 
Constraints:
1 <= |S| <=10^{5}

Starter code:
```python
#User function Template for python3



class Solution:

    def waysToSplit(self, S):

        # code here
```
