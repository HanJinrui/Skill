Xander Cage has a list of cities he can visit on his new top-secret mission. He represents each city as a tuple of $(latitude,longitude,height,points)$. The values of $latitude$, $longitude$, and $height$ are distinct across all cities.

We define a mission as a sequence of cities, $c_1,c_2,c_3,\ldots,c_k$, that he visits. We define the total $\text{points}$ of such a mission to be the sum of the $\text{points}$ of all the cities in his mission list.

Being eccentric, he abides by the following rules on any mission:

He can choose the number of cities he will visit (if any).
He can start the mission from any city.
He visits cities in order of strictly increasing $height$.
The absolute difference in $latitude$ between adjacent visited cities in his mission must be at most $d_l\textbf{at}$.
The absolute difference in $longitude$ between adjacent visited cities in his mission must be at most $d_long$.

Given $\boldsymbol{d\text{_lat}}$, $d\text{_long}$, and the definitions for $n$ cities, find and print the maximum possible total $\text{points}$ that Xander can earn on a mission.

Input Format

The first line contains three space-separated integers describing the respective values of $n$, $\boldsymbol{d\text{_lat}}$, and $d\text{_long}$. 

Each line $\boldsymbol{i}$ of the $n$ subsequent lines contains four space-separated integers denoting the respective $latitude$, $longitude$, $height$, and $\text{points}$ for a city.

Constraints

$1\leq n\leq2\times10^5$  
$1\leq d\_\textit{lat},d\textit{long}\leq2\times10^5$  
$1\leq latitude,longitude,height\leq2\times10^5$  
$-2\times10^5\leq\textit{points}\leq2\times10^5$

Output Format

Print a single integer denoting the maximum possible $\text{points}$ that Xander can earn on a mission.

Sample Input 0
3 1 1
1 1 1 3
2 2 2 -1
3 3 3 3

Sample Output 0
5

Explanation 0

Xander can start at city $1$, then go to city $2$, and then go to city $3$ for a maximum value of total $points=3+-1+3=5$  

Note that he cannot go directly from city $1$ to city $3$ as that would violate his rules that the absolute difference in $latitude$ between adjacent visited cities be $\leq d\text{_lat}$ and the absolute difference in $longitude$ between adjacent visited cities be $\leq d\text{_long}$. Because $d\textit{_lat}=1$ and $d\textit{_long}=1$, he cannot directly travel between those cities.
