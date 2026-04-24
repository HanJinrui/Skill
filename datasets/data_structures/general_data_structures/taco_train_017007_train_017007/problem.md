Given a $6\times6$ 2D Array, $\textbf{arr}$: 

1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0

An hourglass in $\mbox{A}$ is a subset of values with indices falling in this pattern in $\textbf{arr}$'s graphical representation:

a b c
  d
e f g

There are $\mbox{16}$ hourglasses in $\textbf{arr}$. An hourglass sum is the sum of an hourglass' values. Calculate the hourglass sum for every hourglass in $\textbf{arr}$, then print the maximum hourglass sum.  The array will always be $6\times6$.

Example  

$ar r=$

-9 -9 -9  1 1 1 
 0 -9  0  4 3 2
-9 -9 -9  1 2 3
 0  0  8  6 6 0
 0  0  0 -2 0 0
 0  0  1  2 4 0

The $\mbox{16}$ hourglass sums are:

-63, -34, -9, 12, 
-10,   0, 28, 23, 
-27, -11, -2, 10, 
  9,  17, 25, 18

The highest hourglass sum is $28$ from the hourglass beginning at row $1$, column $2$:

0 4 3
  1
8 6 6

Note: If you have already solved the Java domain's Java 2D Array challenge, you may wish to skip this challenge.

Function Description

Complete the function hourglassSum in the editor below.  

hourglassSum has the following parameter(s):

int arr[6][6]: an array of integers  

Returns  

int: the maximum hourglass sum

Input Format

Each of the $\boldsymbol{6}$ lines of inputs $arr\left[i\right]$ contains $\boldsymbol{6}$ space-separated integers $ar r[i][j]$.

Constraints

$-9\leq arr[i][j]\leq9$  
$0\leq i,j\leq5$

Output Format

Print the largest (maximum) hourglass sum found in $\textbf{arr}$.

Sample Input
1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 2 4 4 0
0 0 0 2 0 0
0 0 1 2 4 0

Sample Output
19

Explanation

$\textbf{arr}$ contains the following hourglasses:

The hourglass with the maximum sum ($19$) is:

2 4 4
  2
1 2 4
