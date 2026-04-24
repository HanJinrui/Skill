Given a long integer $\boldsymbol{x}$, count the number of values of $\class{ML__boldsymbol}{\boldsymbol{a}}$ satisfying the following conditions:  

$a\oplus x>x$
$0<a<x$

where $\class{ML__boldsymbol}{\boldsymbol{a}}$ and $\boldsymbol{x}$ are long integers and $\oplus$ is the bitwise XOR operator.  

You are given $\textit{q}$ queries, and each query is in the form of a long integer denoting $\boldsymbol{x}$. For each query, print the total number of values of $\class{ML__boldsymbol}{\boldsymbol{a}}$ satisfying the conditions above on a new line.

For example, you are given the value $x=5$.  Condition $2$ requires that $\class{ML__boldsymbol}{\boldsymbol{a}}<x$.  The following tests are run:  

$1\oplus5=4$ 

$2\oplus5=7$ 

$3\oplus5=6$ 

$4\oplus5=1$   

We find that there are $2$ values meeting the first condition: $2$ and $3$.  

Function Description  

Complete the theGreatXor function in the editor below.  It should return an integer that represents the number of values satisfying the constraints.  

theGreatXor has the following parameter(s):

x: an integer  

Input Format

The first line contains an integer $\textit{q}$, the number of queries. 

Each of the next $\textit{q}$ lines contains a long integer describing the value of $\boldsymbol{x}$ for a query.  

Constraints

$1\leq q\leq10^5$
$1\leq x\leq10^{10}$

Subtasks

For $50\%$ of the maximum score:

$1\leq q\leq10^3$
$1\leq x\leq10^4$

Output Format

For each query, print the number of values of $\class{ML__boldsymbol}{\boldsymbol{a}}$ satisfying the given conditions on a new line.

Sample Input 0
2
2
10

Sample Output 0
1
5

Explanation 0

We perform the following $q=2$ queries:

For $x=2$ the only value of $\class{ML__boldsymbol}{\boldsymbol{a}}$ satisfying $0<a<x$ is $1$. This also satisfies our other condition, as $1\oplus2=3$ and $3>x$. Because we have one valid $\class{ML__boldsymbol}{\boldsymbol{a}}$ and there are no more values to check, we print $1$ on a new line.

For $x=10$, the following values of $\class{ML__boldsymbol}{\boldsymbol{a}}$ satisfy our conditions:

$1\oplus10=11$ 

$4\oplus10=14$ 

$5\oplus10=15$ 

$6\oplus10=12$ 

$7\oplus10=13$

There are five valid values of $\class{ML__boldsymbol}{\boldsymbol{a}}$.

Sample Input 1
2
5
100

Sample Output 1
2
27

Explanation 1

In the first case: 

$2\oplus5=7$ 

$3\oplus5=6$ 

In the second case, the first 10 values are: 

$1\oplus100=101$ 

$2\oplus100=102$ 

$3\oplus100=103$ 

$8\oplus100=108$ 

$9\oplus100=109$ 

$10\oplus100=110$ 

$11\oplus100=111$ 

$\textbf{12}\oplus100=104$ 

$13\oplus100=105$ 

$14\oplus100=106$ 

$15\oplus100=107$
