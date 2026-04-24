Consider a string, $S$, of $n$ lowercase English letters where each character, $s_i$ ($0\leq i<n)$, denotes the letter at index $\boldsymbol{i}$ in $S$. We define an $(a,b,c,d)$ palindromic tuple of $S$ to be a sequence of indices in $S$ satisfying the following criteria:

$\boldsymbol{s_{a}}=\boldsymbol{s_{d}}$, meaning the characters located at indices $a$ and $d$ are the same.
$s_b=s_c$, meaning the characters located at indices $b$ and $c$ are the same.
$0\leq a\lt b\lt c\lt d\lt|s|$, meaning that $a$, $b$, $c$, and $d$ are ascending in value and are valid indices within string $S$.

Given $S$, find and print the number of $(a,b,c,d)$ tuples satisfying the above conditions. As this value can be quite large, print it modulo $(10^9+7)$.  

Function Description 

Complete the function shortPalindrome in the editor below.  

shortPalindrome has the following paramter(s): 

- string s: a string  

Returns 

- int: the number of tuples, modulo $(10^9+7)$  

Input Format

A single string, $S$. 

Constraints

$1\leq|s|\leq10^6$
It is guaranteed that $S$ only contains lowercase English letters.  

Sample Input 0

kkkkkkz

Sample Output 0

15

Explanation 0

The letter z will not be part of a valid tuple because you need at least two of the same character to satisfy the conditions defined above. Because all tuples consisting of four k's are valid, we just need to find the number of ways that we can choose four of the six k's. This means our answer is $\binom{6}{4}\mod(10^9+7)=15$.

Sample Input 1

ghhggh

Sample Output 1

4

Explanation 1

The valid tuples are:

$(0,1,2,3)$
$(0,1,2,4)$
$(1,3,4,5)$
$(2,3,4,5)$

Thus, our answer is $4\:\:\:\text{mod}\:(10^9+7)=4$.

Sample Input 0

kkkkkkz

Sample Output 0

15

Sample Input 1

abbaab

Sample Output 1

4

Sample Input 2
akakak

Sample Output 2
2

Explanation 2

Tuples possible are $(1,2,4,5)~and~(0,1,3,4)$
