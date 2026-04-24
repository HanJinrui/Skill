5-year-old Shinchan had just started learning mathematics. Meanwhile, one of his studious classmates, Kazama, had already written a basic calculator which supports only three operations on integers: multiplication $\left(\times)$, addition $\left(+\right)$, and subtraction $\left({-}\right)$.  Since he had just learned about these operations, he didn't know about operator precedence, and so, in his calculator, all operators had the same precedence and were left-associative.

As always, Shinchan started to irritate him with his silly questions. He gave Kazama a list of $n$ integers and asked him to insert one of the above operators between each pair of consecutive integers such that the result obtained after feeding the resulting expression in Kazama's calculator is divisible by $\mathbf{101}$. At his core, Shinchan is actually a good guy, so he only gave lists of integers for which an answer exists.  

Can you help Kazama create the required expression? If multiple solutions exist, print any one of them.   

Input Format

The first line contains a single integer $n$ denoting the number of elements in the list. The second line contains $n$ space-separated integers $a_1,a_2,\ldots,a_n$ denoting the elements of the list.

Constraints

$2\leq n\leq10^4$
$1\leq a_i\leq100$
The length of the output expression should not exceed $\textbf{10n}$.

Output Format

Print a single line containing the required expressoin. You may insert spaces between operators and operands.

Note

You are not allowed to permute the list.
All operators have the same precedence and are left-associative, e.g., $a+b\times c-d\times e$ is interpreted as $((((a+b)\times c)-d)\times e)$
Unary plus and minus are not supported, e.g., statements like ${-a}$, $a\times-b$, or $-a\times b+c$ are invalid.

Sample Input 0
3
22 79 21

Sample Output 0
22*79-21

Explanation 0

Solution 1: $22\times79-21=1717$, where $1717\div101=17$, so it is perfectly divisible by $\mathbf{101}$. 

Solution 2: $22+79\times21=(22+79)\times21=2121$, which is also divisible by $\mathbf{101}$.

Sample Input 1
5
55 3 45 33 25

Sample Output 1
55+3-45*33-25

Explanation 1

$55+3-45\times33-25=((((55+3)-45)\times33)-25)=404$ which is divisible by $\mathbf{101}$.
