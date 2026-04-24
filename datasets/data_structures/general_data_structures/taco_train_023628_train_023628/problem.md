One of the most important skills a programmer needs to learn early on is the ability to pose a problem in an abstract way. This skill is important not just for researchers but also in applied fields like software engineering and web development.  

You are able to solve most of a problem, except for one last subproblem, which you have posed in an abstract way as follows: Given an array consisting of $n$ integers $[a_1,a_2,\ldots,a_n]$, define $f(l,r)=\text{gcd}(a_l,a_{l+1},\ldots,a_r)\cdot\left(\left(\sum\limits_{i=l}^r a_i\right)-\text{max}(a_l,a_{l+1},\ldots,a_r)\right).$

For example, for an input array [ 10, -5, 5, 20 ], a subsegment $f(1,1)$ would be computed as follows: 

What is $\max\limits_{1\leq l\leq r\leq n}f(l,r)$, i.e., the maximum value of $f(l,r)$ among all subsegments $[l,r]$?  

Complete the function maximumValue which takes an integer array as input and returns the maximum value of $\mbox{f}$ among all subsegments $[l,r]$.

Note that:

$\text{gcd}(x,y)=\text{gcd}(|x|,|y|)$
$\text{gcd}(x,0)=\text{gcd}(0,x)=|x|$

Input Format

The first line contains a single integer $n$

The second line contains $n$ space-separated integers $a_1,a_2,\ldots a_n$

Constraints

$1\leq n\leq50000$ 

$-10^6\leq a_i\leq10^6$  

Output Format

Print a single integer denoting the answer

Sample Input 0
4
10 -5 5 20

Sample Output 0
50

Explanation 0

The maximum value occurs at $f(1,4)=50$ as shown below. 

Sample Input 1
5
7 12 24 6 5

Sample Output 1
144

Explanation 1

The maximum value occurs at $f(2,3)=144$.
