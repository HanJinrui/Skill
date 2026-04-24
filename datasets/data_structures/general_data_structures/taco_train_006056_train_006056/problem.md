Consider a sequence, $c_0,c_1,\ldots c_{n-1}$, and a polynomial of degree $1$ defined as $Q(x)=a\cdot x+b$. You must perform $\textit{q}$ queries on the sequence, where each query is one of the following two types:

1 i x: Replace $c_i$ with $\boldsymbol{x}$.
2 l r: Consider the polynomial $P(x)=c_l\cdot x^0+c_{l+1}\cdot x^1+\cdots+c_r\cdot x^{r-l}$ and determine whether $P(x)$ is divisible by $Q(x)=a\cdot x+b$ over the field $Z_p$, where $p=10^9+7$. In other words, check if there exists a polynomial $R(x)$ with integer coefficients such that each coefficient of $P(x)-R(x)\cdot Q(x)$ is divisible by $\boldsymbol{p}$. If a valid $R(x)$ exists, print Yes on a new line; otherwise, print No.

Given the values of $n$, $\class{ML__boldsymbol}{\boldsymbol{a}}$, $\boldsymbol{b}$, and $\textit{q}$ queries, perform each query in order.

Input Format

The first line contains four space-separated integers describing the respective values of $n$ (the length of the sequence), $\class{ML__boldsymbol}{\boldsymbol{a}}$ (a coefficient in $Q(x)$), $\boldsymbol{b}$ (a coefficient in $Q(x)$), and $\textit{q}$ (the number of queries). 

The second line contains $n$ space-separated integers describing $c_0,c_1,\ldots c_{n-1}$. 

Each of the $\textit{q}$ subsequent lines contains three space-separated integers describing a query of either type 1 or type 2.

Constraints

$1\leq n,q\leq10^5$
For query type 1: $0\leq i\leq n-1$ and $0\leq x<10^9+7$.
For query type 2: $0\leq l\leq r\leq n-1$.
$0\leq a,b,c_i<10^9+7$
$a\neq0$

Output Format

For each query of type 2, print Yes on a new line if $Q(x)$ is a divisor of $P(x)$; otherwise, print No instead.

Sample Input 0
3 2 2 3
1 2 3
2 0 2
1 2 1
2 0 2

Sample Output 0
No
Yes

Explanation 0

Given $Q(x)=2\cdot x+2$ and the initial sequence $c=\{1,2,3\}$, we perform the following $q=3$ queries:

$Q(x)=2\cdot x+2$ is not a divisor of $P(x)=1+2\cdot x+3\cdot x^2$, so we print No on a new line.
Set $c_2$ to $1$, so $c=\{1,2,1\}$.
After the second query, $P(x)=1+2\cdot x+1\cdot x^2$. Because $(2\cdot x+2)\cdot(500000004\cdot x+500000004)\text{mod}(10^9+7)=1+2\cdot x+1\cdot x^2=P(x)$, we print Yes on a new line.
