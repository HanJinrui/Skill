Sophia has discovered several alien languages. Suprisingly, all of these languages have an alphabet, and each of them may contain thousands of characters! Also, all the words in a language have the same number of characters in it.

However, the aliens like their words to be aesthetically pleasing, which for them means that for the $i^{th}$ letter of an $n$-letter alphabet (letters are indexed $1\ldots n$):

if $2i>n$, then the $i^{th}$ letter may be the last letter of a word, or it may be immediately followed by any letter, including itself.

if $2i\leq n$, then the $i^{th}$ letter can not be the last letter of a word and also can only be immediately followed by $j^{th}$ letter if and only if $j\geq2i$.  

Sophia wants to know how many different words exist in this language. Since the result may be large, she wants to know this number, modulo $100000007(10^8+7)$.

Input Format

The first line contains $\boldsymbol{\boldsymbol{t}}$, the number of test cases. The first line is followed by $\boldsymbol{\boldsymbol{t}}$ lines, each line denoting a test case. Each test case will have two space-separated integers $n$, $m$ which denote the number of letters in the language and the length of words in this language respectively.

Constraints

$1\leq t\leq5$  
$1\leq n\leq10^5$  
$1\leq m\leq5\cdot10^5$  

Output Format

For each test case, output the number of possible words modulo $100000007(10^8+7)$.

Sample Input
3
1 3
2 3
3 2

Sample Output
1
3
6

Explanation

For the first test case, there's one letter ('a') and all the words consist of $3$ letters. There's only one possibility which is "aaa".  

For the second test case, there are two letters ('a' and 'b') and all the words are of $3$ letters. The possible strings are "abb", "bab", & "bbb". The words can end only with 'b' because $2\cdot\text{index}(b)=2\cdot2>2$ and for 'a', it's $2\cdot\text{index}(a)=2\cdot1\leq2$. "aab" is not allowed because 'a' can not be followed immediately by 'a'. For a word of length 4 and alphabet of size 2, "abab" would be allowed.

For the third test case, there are three letters ('a', 'b' and 'c') and all of the words are $2$ letters. The words can only end with 'b' or 'c'. The possible words are "ab", "ac", "bb", "cc", "bc", "cb".
