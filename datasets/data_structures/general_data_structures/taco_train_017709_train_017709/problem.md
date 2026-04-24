A left rotation operation on an array of size $n$ shifts each of the array's elements $1$ unit to the left. Given an integer, $\boldsymbol{d}$, rotate the array that many steps left and return the result.  

Example 

$\boldsymbol{d}=2$ 

$arr=[1,2,3,4,5]$  

After $2$ rotations, $ar r'=[3,4,5,1,2]$.

Function Description  

Complete the rotateLeft function in the editor below.  

rotateLeft has the following parameters:  

int d:  the amount to rotate by  
int arr[n]: the array to rotate  

Returns  

int[n]: the rotated array

Input Format

The first line contains two space-separated integers that denote $n$, the number of integers, and $\boldsymbol{d}$, the number of left rotations to perform. 

The second line contains $n$ space-separated integers that describe $\mbox{arr}[]$.  

Constraints

$1\leq n\leq10^5$  
$1\leq d\leq n$  
$1\leq a[i]\leq10^6$

Sample Input
5 4
1 2 3 4 5

Sample Output
5 1 2 3 4

Explanation

To perform $\boldsymbol{d}=4$ left rotations, the array undergoes the following sequence of changes: 

$[1,2,3,4,5]\to[2,3,4,5,1]\to[3,4,5,1,2]\to[4,5,1,2,3]\to[5,1,2,3,4]$
