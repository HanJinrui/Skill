There are $n$ variables and $m$ requirements. Requirements are represented as $\left(x\leq y\right)$, meaning that the $x^{th}$ variable must be less than or equal to the $y^{th}$ variable. 

Your task is to assign non-negative numbers smaller than $10$ to each variable and then calculate the number of different assignments satisfying all requirements. Two assignments are different if and only if at least one variable is assigned to a different number in both assignments. Print your answer modulo $10^3+7$.

Input Format

The first line contains $2$ space-separated integers, $n$ and $m$, respectively.
Each of the $m$ subsequent lines contains $2$ space-seperated integers describing the respective $\boldsymbol{x}$ and $y$ values for an $\left(x\leq y\right)$ requirement.

Constraints

$0<n<14$
$0\lt m\lt200$
$0\leq x,y<n$

Output Format

Print your answer modulo $10^3+7$.

Sample Input 0
6 7
1 3
0 1
2 4
0 4
2 5
3 4
0 2

Sample Output 0
1000

Explanation 0

There are $\boldsymbol{6}$ variables and $7$ requirements.

Let the variables be in the array $a\left[6\right]$.

Requirements are -
$a[1]<=a[3],a[0]<=a[1],a[2]<=a[4],a[0]<=a[4],a[2]<=a[5],a[3]<=a[4],a[0]<=a[2]$

One of the assignments is - $\{1,2,3,4,5,6\}$

Similarly there are $25168$ assignments possible.

Result = $25168\:\text{mod}\:1007=1000$.
