Consider an $n$-integer sequence, $A=\{a_0,a_1,\ldots,a_{n-1}\}$. We perform a query on $\mbox{A}$ by using an integer, $\boldsymbol{d}$, to calculate the result of the following expression:

$\underset{0\leq i\leq n-d}{\text{min}}\left(\underset{i\leq j\lt i+d}{\text{max}}a_j\right)$

In other words, if we let $m_i=\text{max}(a_i,a_{i+1},a_{i+2},...,a_{i+d-1})$, then you need to calculate $\text{min}(m_0,m_1,\ldots,m_{n-d})$.  

Given $\textbf{arr}$ and $\textit{q}$ queries, return a list of answers to each query.

Example 

$arr=[2,3,4,5,6]$ 

$queries=[2,3]$  

The first query uses all of the subarrays of length $2$:  $[2,3],[3,4],[4,5],[5,6]$.  The maxima of the subarrays are $[3,4,5,6]$.  The minimum of these is $3$.  

The second query uses all of the subarrays of length $3$: $[2,3,4],[3,4,5],[4,5,6]$.  The maxima of the subarrays are $[4,5,6]$.  The minimum of these is $\begin{array}{c}4\end{array}$.  

Return $[3,4]$.  

Function Description   

Complete the solve function below.  

solve has the following parameter(s):  

int arr[n]: an array of integers  
int queries[q]: the lengths of subarrays to query  

Returns  

int[q]: the answers to each query   

Input Format

The first line consists of two space-separated integers, $n$ and $\textit{q}$. 

The second line consists of $n$ space-separated integers, the elements of $\textbf{arr}$. 

Each of the $\textit{q}$ subsequent lines contains a single integer denoting the value of $\boldsymbol{d}$ for that query. 

Constraints

$1\leq n\leq10^5$
$0\leq ar r[i]<10^6$
$1\leq q\leq100$
$1\leq d\leq n$

Sample Input 0
5 5
33 11 44 11 55
1
2
3
4
5

Sample Output 0
11
33
44
44
55

Explanation 0

For $\boldsymbol{d}=1$, the answer is $\text{min}(\text{max}(a_0),\text{max}(a_1),\text{max}(a_2),\text{max}(a_3),\text{max}(a_4))=11$. 

For $\boldsymbol{d}=2$, the answer is $\text{min}(\text{max}(a_0,a_1),\text{max}(a_1,a_2),\text{max}(a_2,a_3),\text{max}(a_3,a_4))=33$. 

For $\boldsymbol{d}=3$, the answer is $\text{min}(\text{max}(a_0,a_1,a_2),\text{max}(a_1,a_2,a_3),\text{max}(a_2,a_3,a_4))=44$. 

For $\boldsymbol{d}=4$, the answer is $\text{min}(\text{max}(a_0,a_1,a_2,a_3),\text{max}(a_1,a_2,a_3,a_4))=44$. 

For $\boldsymbol{d}=5$, the answer is $\text{min}(\text{max}(a_0,a_1,a_2,a_3,a_4))=55$.  

Sample Input 1
5 5
1 2 3 4 5
1
2
3
4
5

Sample Output 1
1
2
3
4
5

Explanation 1

For each query, the "prefix" has the least maximum value among the consecutive subsequences of the same size.
