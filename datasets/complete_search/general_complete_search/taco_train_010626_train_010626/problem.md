Two friends like to pool their money and go to the ice cream parlor.  They always choose two distinct flavors and they spend all of their money.

Given a list of prices for the flavors of ice cream, select the two that will cost all of the money they have.  

Example. 
$m=6$
$cost=[1,3,4,5,6]$

The two flavors that cost $\mbox{I}$ and $5$ meet the criteria.  Using $\mbox{1}$-based indexing, they are at indices $\mbox{1}$ and $\begin{array}{c}4\end{array}$.  

Function Description

Complete the icecreamParlor function in the editor below.    

icecreamParlor has the following parameter(s):  

int m: the amount of money they have to spend  
int cost[n]: the cost of each flavor of ice cream  

Returns   

int[2]:  the indices of the prices of the two flavors they buy, sorted ascending 

Input Format

The first line contains an integer, $\boldsymbol{\boldsymbol{t}}$, the number of trips to the ice cream parlor.   The next $\boldsymbol{\boldsymbol{t}}$ sets of lines each describe a visit.  

Each trip is described as follows:

The integer $m$, the amount of money they have pooled. 
The integer $n$, the number of flavors offered at the time. 
$n$ space-separated integers denoting the cost of each flavor: $cost[cost[1],cost[2],...,cost[n]]$.  

Note:  The index within the cost array represents the flavor of the ice cream purchased.  

Constraints

$1\leq t\leq50$  
$2\leq m\leq10^4$   
$2\leq n\leq10^4$   
$1\leq c o s t[i]\leq10^4$, ∀ $i\in[1,n]$   
There will always be a unique solution.

Sample Input
STDIN       Function
-----       --------
2           t = 2
4           k = 4
5           cost[] size n = 5
1 4 5 3 2   cost = [1, 4, 5, 3, 2]
4           k = 4
4           cost[] size n = 4
2 2 4 3     cost=[2, 2,4, 3]

Sample Output
1 4
1 2

Explanation

Sunny and Johnny make the following two trips to the parlor:

The first time, they pool together $m=4$ dollars. Of the five flavors available that day, flavors $\mbox{1}$ and $\begin{array}{c}4\end{array}$ have a total cost of $1+3=4$.  
The second time, they pool together $m=4$ dollars. Of the four flavors available that day, flavors $\mbox{1}$ and $2$ have a total cost of $2+2=4$.
