Given a string, $\mbox{A}$, we define some operations on the string as follows:

a. $reverse(A)$ denotes the string obtained by reversing string $\mbox{A}$. Example: $\text{reverse()abc''})=\text{"cba''}$ 

b. $shuffle(A)$ denotes any string that's a permutation of string $\mbox{A}$. Example: $\textsf{shuffle("good^n)}\:\in\:\:['\textsf{good'},\:\:'\textsf{gdo'},\:\:\textsf{'cgd'},\:\:\textsf{'oddg'},\:\:\textsf{'dgo'},\:\:\textsf{'dog'}]$ 

c. $\textit{merge}(A1,A2)$ denotes any string that's obtained by interspersing the two strings $A\mathbf{1}$ & $A2$, maintaining the order of characters in both. For example, $\textbf{A1}=\textbf{"abc''}$ & $\textbf{A2}=\textbf{"def"}$, one possible result of $\textit{merge}(A1,A2)$ could be $\textbf{"abcdef"}$, another could be $\textbf{"abdef"}$, another could be $\textbf{"adbecf"}$ and so on.  

Given a string $\boldsymbol{\mathrm{~S~}}$ such that $\textbf{s}\in\textbf{merge(reverse(A)},\:\textbf{shuffle(A)})$ for some string $\mbox{A}$, find the lexicographically smallest $\mbox{A}$.

For example, $s=a b a b$.  We can split it into two strings of $\boldsymbol{ab}$.  The reverse is $\textbf{ba}$ and we need to find a string to shuffle in to get $\boldsymbol{abab}$.  The middle two characters match our reverse string, leaving the $\boldsymbol{\alpha}$ and $\boldsymbol{b}$ at the ends.  Our shuffle string needs to be $\boldsymbol{ab}$.  Lexicographically $ab<ba$, so our answer is $\boldsymbol{ab}$.  

Function Description

Complete the reverseShuffleMerge function in the editor below.  It must return the lexicographically smallest string fitting the criteria.  

reverseShuffleMerge has the following parameter(s):

s: a string

Input Format

A single line containing the string $\boldsymbol{\mathrm{~S~}}$.

Constraints

$\boldsymbol{\mathrm{~S~}}$ contains only lower-case English letters, ascii[a-z]  
$1\leq|s|\leq10000$  

Output Format

Find and return the string which is the lexicographically smallest valid $\mbox{A}$.

Sample Input 0
eggegg

Sample Output 0
egg

Explanation 0

Split "eggegg" into strings of like character counts: "egg", "egg" 

reverse("egg") = "gge" 

shuffle("egg") can be "egg" 

"eggegg" belongs to the merge of ("gge", "egg")

The merge is: $\boldsymbol{\mathrm{~e~}}$gge$\mbox{gg}$.

'egg' < 'gge'

Sample Input 1
abcdefgabcdefg

Sample Output 1
agfedcb

Explanation 1

Split the string into two strings with like characters: $abcdefg$ and $abcdefg$. 

Reverse $abcdefg$ = $gfeedcba$ 

Shuffle $gfeedcba$ can be $bcdefga$ 

Merge to $\boldsymbol{\alpha}$bcdefga$bcdefg$    

Sample Input 2
aeiouuoiea

Sample Output 2
aeiou

Explanation 2

Split the string into groups of like characters: $a e i o u$ 

Reverse $a e i o u$ = $u o iea$ 

These merge to $a e i o u$uoiea
