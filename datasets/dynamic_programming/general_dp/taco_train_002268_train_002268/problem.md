Li and Lu have $n$ integers, $a_1,a_2,\ldots,a_n$, that they want to divide fairly between the two of them. They decide that if Li gets integers with indices $I=\{i_1,i_2,\ldots,i_k\}$ (which implies that Lu gets integers with indices $J=\{1,\ldots,n\}\setminus I$), then the measure of unfairness of this division is: 
$f(I)=\sum_{i\in I}\sum_{j\in J}|a_i-a_j|$

Find the minimum measure of unfairness that can be obtained with some division of the set of integers where Li gets exactly $\boldsymbol{\mbox{k}}$ integers. 

Note $A\setminus B$ means Set complement

Input Format

The first line contains two space-separated integers denoting the respective values of $n$ (the number of integers Li and Lu have) and $\boldsymbol{\mbox{k}}$ (the number of integers Li wants). 

The second line contains $n$ space-separated integers describing the respective values of $a_1,a_2,\ldots,a_n$.

Constraints

$1\leq k<n\leq3000$
$1\leq a_i\leq10^9$
For $15\%$ of the test cases, $n\leq20$.
For $45\%$ of the test cases, $n\leq40$.

Output Format

Print a single integer denoting the minimum measure of unfairness of some division where Li gets $\boldsymbol{\mbox{k}}$ integers.

Sample Input 0

4 2
4 3 1 2

Sample Output 0

 6

Explanation 0 

One possible solution for this input is $I=\{\text{{2,4}\}};\:J=\{\text{{1,3}\}}$. $|a_2-a_1|+|a_2-a_3|+|a_4-a_1|+|a_4-a_3|=1+2+2+1=6$

Sample Input 1   

4 1
3 3 3 1

Sample Output 1

2

Explanation 1 

The following division of numbers is optimal for this input: $I=\{1\};\:J=\{2,3,4\}$.
