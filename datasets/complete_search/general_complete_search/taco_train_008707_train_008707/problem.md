We define the following:

A subarray of array $a$ of length $n$ is a contiguous segment from $a[i]$ through $a[j]$ where $0\leq i\leq j<n.$.
The sum of an array is the sum of its elements.

Given an $n$ element array of integers, $a$, and an integer, $m$, determine the maximum value of the sum of any of its subarrays modulo $m$. 

Example 

$a=[1,2,3]$ 

$m=2$     

The following table lists all subarrays and their moduli:

		sum	%2
[1]		1	1
[2]		2	0
[3]		3	1
[1,2]		3	1
[2,3]		5	1
[1,2,3]		6	0

The maximum modulus is $unrecognized$.

Function Description

Complete the maximumSum function in the editor below.  

maximumSum has the following parameter(s):

long a[n]: the array to analyze   
long m: the modulo divisor   

Returns 

- long: the maximum (subarray sum modulo $m$)   

Input Format

The first line contains an integer $q$, the number of queries to perform.

The next $q$ pairs of lines are as follows:

The first line contains two space-separated integers $n$ and (long)$m$, the length of $a$ and the modulo divisor.  
The second line contains $n$ space-separated long integers $a[i]$.

Constraints

$2\leq n\leq10^{5}$  
$1\leq m\leq10^{14}$  
$1\leq a[i]\leq10^{18}$  
$2\leq\$ the sum of $n$ over all test cases $\leq\mathop{\mathrm{5}}\times10^{5}$   

Sample Input
STDIN       Function
-----       --------
1           q = 1
5 7         a[] size n = 5, m = 7
3 3 9 9 5

Sample Output
6

Explanation

The subarrays of array $a=[3,3,9,9,5]$ and their respective sums modulo $m=7$ are ranked in order of length and sum in the following list:


$1 .[9]\Rightarrow9\%7=2\mathrm{and}[9]\rightarrow9\%7=2 $
$[3]\Rightarrow3\%7=3\mathrm{and}[3]\rightarrow3\%7=3 $
$[5]\Rightarrow5\%7=5 $

$2. [9,5]\Rightarrow14\%7=0  $
$[9,9]\Rightarrow18\%7=4 $
$[3,9]\Rightarrow12\%7=5 $
$[3,3]\Rightarrow6\%7=6 $

$3. [3,9,9]\Rightarrow21\%7=0 $
$[3,3,9]\Rightarrow15\%7=1 $
$[9,9,5]\Rightarrow23\%7=2 $

$ 4.[3,3,9,9]\Rightarrow24\%7=3  $
$[3,9,9,5]\Rightarrow26\%7=5 $

$5[3,3,9,9,5]\Rightarrow29\%7=1$

The maximum value for $subarray sum \%7$ for any subarray is $6$.
