Consider two non-negative long integers, $a$ and $\boldsymbol{b}$, where $a\leq b$. The bitwise AND of all long integers in the inclusive range between $a$ and $\boldsymbol{b}$ can be expressed as $a\ \text{&}\ (a+1)\ \text{&}\ \ldots\ \text{&}\ (b-1)\ \text{&}\ b$, where $\text{&}$ is the bitwise AND operator. 

Given $n$ pairs of long integers, $a[i]$ and $b[i]$, compute and print the bitwise AND of all natural numbers in the inclusive range between $a[i]$ and $b[i]$.

For example, if $\boldsymbol{a=10}$ and $b=14$, the calculation is $10\:\text{&}\:11\:\text{&}\:12\:\text{&}\:13\:\text{&}\:14=8$.  

Function Description  

Complete the andProduct in the editor below.  It should return the computed value as an integer.  

andProduct has the following parameter(s):  

a: an integer  
b: an integer  

Input Format

The first line contains a single integer $n$, the number of intervals to test. 

Each of the next $n$ lines contains two space-separated integers $a[i]$ and $b[i]$.

Constraints

$1\leq n\leq200$  
$0\leq a[i]\leq b[i]<2^{32}$

Output Format

For each pair of long integers, print the bitwise AND of all numbers in the inclusive range between $a[i]$ and $b[i]$ on a new line.

Sample Input 0
3
12 15
2 3
8 13

Sample Output 0
12
2
8

Explanation 0

There are three pairs to compute results for:

$\boldsymbol{a=12}$ and $\boldsymbol{b=15}$ 

$12~\text{&}~13~\text{&}~14~\text{&}~15~=12$, so we print $12$ on a new line.
$\boldsymbol{a}=2$ and $b=3$ 

$2\&3=2$
$\boldsymbol{a}=8$ and $b=13$ 

$8\:\text{&}\:9\:\text{&}\:10\:\text{&}\:11\:\text{&}\:12\&\:13\:=8$

Sample Input 1
2
17 23
11 15

Sample Output 1
16
8
