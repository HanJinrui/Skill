Johnny is playing with a large binary number, $\mbox{B}$. The number is so large that it needs to be compressed into an array of integers, $\mbox{A}$, where the values in even indices ($0,2,4,\ldots$) represent some number of consecutive $1$ bits and the values in odd indices ($1,3,5,\ldots$) represent some number of consecutive $0$ bits in alternating substrings of $\mbox{B}$.       

For example, suppose we have array $A=\{4,1,3,2,4\}$. $\boldsymbol{A_0}$ represents $\text{"}1111\text{"}$, $\boldsymbol{A_1}$ represents $\text{"}0\text{"}$, $\boldsymbol{A_{2}}$ represents $\text{"}111"$, $A_3$ represents $\text{"00"}$, and $\boldsymbol{A}_4$ represents $\text{"}1111\text{"}$. The number of consecutive binary characters in the $i^{\mbox{th}}$ substring of $\mbox{B}$ corresponds to integer $A_i$, as shown in this diagram:

When we assemble the sequential alternating sequences of $1$'s and $0$'s, we get $B="11110111001111"$.

We define setCount($\mbox{B}$) to be the number of $1$'s in a binary number, $\mbox{B}$. Johnny wants to find a binary number, $\mbox{D}$, that is the smallest binary number $>B$ where setCount($\mbox{B}$) = setCount($\mbox{D}$). He then wants to compress $\mbox{D}$ into an array of integers, $\mbox{C}$ (in the same way that integer array $\mbox{A}$ contains the compressed form of binary string $\mbox{B}$).

Johnny isn't sure how to solve the problem. Given array $\mbox{A}$, find integer array $\mbox{C}$ and print its length on a new line. Then print the elements of array $\mbox{C}$ as a single line of space-separated integers.

Input Format

The first line contains a single positive integer, $\mathbf{T}$, denoting the number of test cases. Each of the $2T$ subsequent lines describes a test case over $2$ lines:

The first line contains a single positive integer, $n$, denoting the length of array $\mbox{A}$. 
The second line contains $n$ positive space-separated integers describing the respective elements in integer array $\mbox{A}$ (i.e., $A_0,A_1,\ldots,A_{n-1}$).

Constraints

$1\leq T\leq100$
$1\leq n\leq10$

Subtasks

For a $50\%$ score, $1\leq A_i\leq10^4$.
For a $\textbf{100\%}$ score, $1\leq A_i\leq10^{18}$.

Output Format

For each test case, print the following $2$ lines:  

Print the length of integer array $\mbox{C}$ (the array representing the compressed form of binary integer $\mbox{D}$) on a new line. 
Print each element of $\mbox{C}$ as a single line of space-separated integers.

It is guaranteed that a solution exists.

Sample Input 0
1
5
4 1 3 2 4

Sample Output 0
7
4 1 3 1 1 1 3

Explanation 0

$A=\{4,1,3,2,4\}$, which expands to $B=11110111001111$. We then find setCount($\mbox{B}$) $=11$. The smallest binary number $>B$ which also has eleven $\mbox{1}$'s is $D=11110111010111$. This can be reduced to the integer array $C=\{4,1,3,1,1,1,3\}$. This is demonstrated by the following figure:

Having found $\mbox{C}$, we print its length ($7$) as our first line of output, followed by the space-separated elements in $\mbox{C}$ as our second line of output.
