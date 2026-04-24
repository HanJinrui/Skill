Given a string of lowercase alphabets and a number k, the task is to find the minimum value of the string after removal of ‘k’ characters. 
The value of a string is defined as the sum of squares of the count of each distinct character.
For example consider the string “geeks”, here frequencies of characters are g -> 1, e -> 2, k -> 1, s -> 1 and value of the string is 1^{2 }+ 2^{2 }+ 1^{2 }+ 1^{2} = 7
 
Example 1:
Input: S = "abccc", K = 1
Output: 6
Explanation: Remove one 'c', then frequency
will be a -> 1, b -> 1, c -> 2.
1^{2 }+ 1^{2 }+ 2^{2 }= 6
Ã¢â¬â¹Example 2:
Input: S = "aaab", K = 2
Output: 2
Explanation: Remove 2 'a's, then frequency
will be a -> 1, b -> 1.
1^{2 }+ 1^{2}^{ }= 2
Your Task:  
You don't need to read input or print anything. Your task is to complete the function minValue() which takes the string s as inputs and returns the answer.
Expected Time Complexity: O(K*log(|S|))
Expected Auxiliary Space: O(constant)
Constraints:
1 ≤ K, |S| ≤ 10^{4}

Starter code:
```python
#User function Template for python3
class Solution:
	def minValue(self, S, K):
		# code here
```
