Bill Gates is on one of his philanthropic journeys to a village in Utopia. He has brought a box of packets of candies and would like to distribute one packet to each of the children.  Each of the packets contains a number of candies.  He wants to minimize the cumulative difference in the number of candies in the packets he hands out.  This is called the unfairness sum.  Determine the minimum unfairness sum achievable. 

For example, he brings $n=7$ packets where the number of candies is $packets=[3,3,4,5,7,9,10]$.  There are $k=3$ children.  The minimum difference between all packets can be had with $3,3,4$ from indices $\mathbf{0,1}$ and $2$.  We must get the difference in the following pairs: $\{(0,1),(0,2),(1,2)\}$.  We calculate the unfairness sum as:

packets candies				
0	3		indices		difference	result
1	3		(0,1),(0,2)	|3-3| + |3-4|	1 
2	4		(1,2)		|3-4|		1

Total = 2

Function Description

Complete the angryChildren function in the editor below.  It should return an integer that represents the minimum unfairness sum achievable.

angryChildren has the following parameter(s):

k: an integer that represents the number of children  
packets:  an array of integers that represent the number of candies in each packet  

Input Format

The first line contains an integer $n$. 

The second line contains an integer $\boldsymbol{\mbox{k}}$. 

Each of the next $n$ lines contains an integer $\textit{packets[i]}$.

Constraints

$2\leq n\leq10^5$ 

$2\leq k\leq n$ 

$0\leq p a c k ets[i]\leq10^9$  

Output Format

A single integer representing the minimum achievable unfairness sum.

Sample Input 0  

7
3
10
100
300
200
1000
20
30

Sample Output 0  

40

Explanation 0

Bill Gates will choose packets having 10, 20 and 30 candies.  The unfairness sum is $|10-20|+|20-30|+|10-30|=40$.  

Sample Input 1  

10
4
1
2
3
4
10
20
30
40
100
200

Sample Output 1  

10

Explanation 1  

Bill Gates will choose 4 packets having 1,2,3 and 4 candies. The unfairness sum i $|1-2|+|1-3|+|1-4|+|2-3|+|2-4|+|3-4|=10$.
