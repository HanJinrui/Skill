Nina received an odd New Year's present from a student: a set of $n$ unbreakable sticks. Each stick has a length, $\boldsymbol{l}$, and the length of the $i^{\mbox{th}}$ stick is $\boldsymbol{l_{i-1}}$. Deciding to turn the gift into a lesson, Nina asks her students the following:

How many ways can you build a square using exactly $\boldsymbol{6}$ of these unbreakable sticks? 

Note: Two ways are distinct if they use at least one different stick. As there are $\left(\begin{matrix}n\\ 6\end{matrix}\right)$ choices of sticks, we must determine which combinations of sticks can build a square.

Input Format

The first line contains an integer, $n$, denoting the number of sticks. The second line contains $n$ space-separated integers $l_0,l_1,\ldots,l_{n-2},l_{n-1}$ describing the length of each stick in the set.

Constraints

$6\leq n\leq3000$
$1\leq l_i\leq10^7$

Output Format

On a single line, print an integer representing the number of ways that $\boldsymbol{6}$ unbreakable sticks can be used to make a square.

Sample Input 0

8
4 5 1 5 1 9 4 5 

Sample Output 0

3

Sample Input 1

6
1 2 3 4 5 6 

Sample Output 1

0    

Explanation

Sample 0 

Given $8$ sticks ($l=4,5,1,5,1,9,4,5$), the only possible side length for our square is $5$. We can build square $\mbox{S}$ in $3$ different ways:

$S=\{l_0,l_1,l_2,l_3,l_4,l_6\}=\{4,5,1,5,1,4\}$ 

$S=\{l_0,l_1,l_2,l_4,l_6,l_7\}=\{4,5,1,1,4,5\}$

$S=\{l_0,l_2,l_3,l_4,l_6,l_7\}=\text{{4,1,5,1,4,5}\}$

In order to build a square with side length $5$ using exactly $\boldsymbol{6}$ sticks, $l_{0},l_{2},l_{4},$ and $l_{6}$ must always build two of the sides. For the remaining two sides, you must choose $2$ of the remaining $3$ sticks of length $5$ ($l_1,l_3,$ and $l_{7}$).

Sample 1 

We have to use all $\boldsymbol{6}$ sticks, making the largest stick length ($\boldsymbol{6}$) the minimum side length for our square. No combination of the remaining sticks can build $3$ more sides of length $\boldsymbol{6}$ (total length of all other sticks is $1+2+3+4+5=15$ and we need at least length $3*6=18$), so we print $\mbox{0}$.
