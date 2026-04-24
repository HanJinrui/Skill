Given a text, text. The task is to count the number of sentences and words in the text. 
Definition of a sentence :- Sentences are defined as contiguous space-separated strings of characters ending with a sentence punctuation (' . ',  ' ! ' or ' ? ') or the last contiguous set of space-separated strings, even if they don't end with a punctuation mark.
Definition of a word :- Words are defined as a string of alphabetic characters i.e. any upper or lower case characters a-z or A-Z.
Example 1:
Input: text = "Sentences"
Output: 1 1
Explaination: There is only one word and 
sentence in the given text.
Example 2:
Input: text = "many??? Sentences are"
Output: 2 3
Explaination: There are two sentences and 
three words.
Your Task:
You do not need to read input or print anything. Your task is to complete the function sentenceWord() which takes text as input parameters and returns a list containing number of sentences and words respectively.
Expected Time Complexity: O(|text|)
Expected Auxiliary Space: O(1)
Constraints:
1 ≤ |text| ≤ 250

Starter code:
```python
#User function Template for python3

class Solution:
    def sentenceWord(self, text):
        # code here
```
