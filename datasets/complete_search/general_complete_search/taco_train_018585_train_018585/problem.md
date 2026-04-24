Given an array of integers, you must answer a number of queries. Each query consists of a single integer, $\boldsymbol{x}$, and is performed as follows:

Add $\boldsymbol{x}$ to each element of the array, permanently modifying it for any future queries.
Find the absolute value of each element in the array and print the sum of the absolute values on a new line.

Tip: The Input/Output for this challenge is very large, so you'll have to be creative in your approach to pass all test cases.

Function Description  

Complete the playingWithNumbers function in the editor below.  It should return an array of integers that represent the responses to each query.  

playingWithNumbers has the following parameter(s):  

arr: an array of integers  
queries: an array of integers  

Input Format

The first line contains an integer $n$ the number of elements in $\textbf{arr}$. 

The second line contains $n$ space-separated integers $arr\left[i\right]$. 

The third line contains an integer $\textit{q}$, the number of queries. 

The fourth line contains $\textit{q}$ space-separated integers $\boldsymbol{x}$ where $qumeries[j]=x$.    

Constraints

$1\leq n\leq5\times10^5$  
$1\leq q\leq5\times10^5$  
$-2000\leq arr[i]\leq2000$, where $0\leq i<n$.
$-2000\leq\textit{queries}[j]\leq2000$, where $0\leq j<q$

Output Format

For each query, print the sum of the absolute values of all the array's elements on a new line.

Sample Input
3
-1 2 -3
3
1 -2 3 

Sample Output
5
7
6

Explanation

Query 0: $x=1$ 

Array: $[-1,2,-3]\rightarrow[0,3,-2]$ 

The sum of the absolute values of the updated array's elements is $|0|+|3|+|-2|=0+3+2=5$.    

Query 1: $x=-2$ 

Array: $[0,3,-2]\rightarrow[-2,1,-4]$ 

The sum of the absolute values of the updated array's elements is $|-2|+|1|+|-4|=2+1+4=7$.   

Query 2: $x=3$ 

Array: $[-2,1,-4]\rightarrow[1,4,-1]$ 

The sum of the absolute values of the updated array's elements is $|1|+|4|+|-1|=1+4+1=6$.
