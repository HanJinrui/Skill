Consider an array, $\mbox{A}$, of $n$ integers ($A=a_0,a_1,...,a_{n-1}$). 
We take all consecutive subsequences of integers from the array that satisfy the following:
$\{a_i,a_{i+1},\ldots,a_{j-1},aj\},\text{where}\ 0\leq i\leq j<n$ 

For example, if $n=3$ our subsequences will be:

$\boldsymbol{a_0}$
$a_1$    
$a_2$    
$a_{0},a_{1}$
$a_{1},a_{2}$
$a_{0},a_{1},a_{2}$ 

For each subsequence, we apply the bitwise XOR ($\oplus$) operation on all the integers and record the resultant value. Since there are $n\times\frac{(n+1)}{2}$ subsequences, this will result in $n\times\frac{(n+1)}{2}$ numbers.   

Given array $\mbox{A}$, find the XOR sum of every subsequence of $\mbox{A}$ and determine the frequency at which each number occurs. Then print the number and its respective frequency as two space-separated values on a single line.  

Input Format

The first line contains an integer, $n$, denoting the size of the array. 

Each line $\boldsymbol{i}$ of the $n$ subsequent lines contains a single integer describing element $a_i$.

Constraints

$1\leq n\leq10^5$
$1\leq a_i<2^{16}$

Output Format

Print $2$ space-separated integers on a single line. The first integer should be the number having the highest frequency, and the second integer should be the number's frequency (i.e., the number of times it appeared). If there are multiple numbers having maximal frequency, choose the smallest one.

Sample Input 0
4
2
1
1
3

Sample Output 0
1 3

Explanation 0

Let's find the XOR sum for all consecutive subsequences. We'll refer to the frequency of some number $\boldsymbol{x}$ as $f(x)$, and keep a running sum for each frequency:  

$2=2$, frequencies: $f(2)=1$
$1=1$, frequencies: $f(1)=1$ and $f(2)=1$
$1=1$, frequencies: $f(1)=2$ and $f(2)=1$
$3=3$, frequencies: $f(1)=2$, $f(2)=1$, and $f(3)=1$
$2\oplus1=3$, frequencies: $f(1)=2$, $f(2)=1$, and $f(3)=2$
$1\oplus1=0$, frequencies: $f(0)=1$, $f(1)=2$, $f(2)=1$, and $f(3)=2$
$1\oplus3=2$, frequencies: $f(0)=1$, $f(1)=2$, $f(2)=2$, and $f(3)=2$
$2\oplus1\oplus1=2$, frequencies: $f(0)=1$, $f(1)=2$, $f(2)=3$, and $f(3)=2$  
$1\oplus1\oplus3=3$, frequencies: $f(0)=1$, $f(1)=2$, $f(2)=3$, and $f(3)=3$   
$2\oplus1\oplus1\oplus3=1$, frequencies: $f(0)=1$, $f(1)=3$, $f(2)=3$, and $f(3)=3$     

Our maximal frequency is $3$, and the integers $1$, $2$, and $3$ all have this frequency. Because more than one integer has this frequency, we choose the smallest one, which is $1$. We then print the respective smallest number having the maximal frequency and the maximal frequency as a single line of space-separated values.
