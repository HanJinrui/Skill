Alice gives Bob a board composed of $1\times1$ wooden squares and asks him to find the minimum cost of breaking the board back down into its individual squares. To break the board down, Bob must make cuts along its horizontal and vertical lines. 

To reduce the board to squares, Bob makes horizontal and vertical cuts across the entire board.  Each cut has a given cost, $cost\text{_}y[i]$ or $cost\text{_}x[j]$ for each cut along a row or column across one board, so the cost of a cut must be multiplied by the number of segments it crosses.  The cost of cutting the whole board down into $1\times1$ squares is the sum of the costs of each successive cut.   

Can you help Bob find the minimum cost?  The number may be large, so print the value modulo $10^9+7$.

For example, you start with a $2\times2$ board.  There are two cuts to be made at a cost of $cost\text{_}y[1]=3$ for the horizontal and $cost\text{_}x[1]=1$ for the vertical.  Your first cut is across $1$ piece, the whole board.  You choose to make the horizontal cut between rows $1$ and $2$ for a cost of $1\times3=3$.  The second cuts are vertical through the two smaller boards created in step $\mbox{I}$ between columns $1$ and $2$.  Their cost is $2\times1=2$.  The total cost is $3+2=5$ and $5\%(10^9+7)=5$.

Function Description  

Complete the boardCutting function in the editor below.  It should return an integer.  

boardCutting has the following parameter(s):  

cost_x: an array of integers, the costs of vertical cuts  
cost_y: an array of integers, the costs of horizontal cuts  

Input Format

The first line contains an integer $\textit{q}$, the number of queries.

The following $\textit{q}$ sets of lines are as follows:

The first line has two positive space-separated integers $m$ and $n$, the number of rows and columns in the board.    
The second line contains $m-1$ space-separated integers cost_y[i], the cost of a  horizontal cut between rows $\left[i\right]$ and $\left[i+1\right]$ of one board.
The third line contains $n-1$ space-separated integers cost_x[j], the cost of a vertical cut between columns $\left[j\right]$ and $[j+1]$ of one board.

Constraints

$1\leq q\leq20$  
$2\leq m,n\leq1000000$       
$0\leq c o s t\text{_}y[i],cost\text{_}x[j]\leq10^9$   

Output Format

For each of the $\textit{q}$ queries, find the minimum cost ($minCost$) of cutting the board into $1\times1$ squares and print the value of $minCost\%(10^9+7)$.

Sample Input 0

1
2 2
2
1

Sample Output 0

4

Explanation 0 

We have a $2\times2$ board, with cut costs $cost\text{_}y[1]=2$ and $cost\text{_}x[1]=1$. Our first cut is horizontal between $y[1]$ and $y[2]$, because that is the line with the highest cost ($2$). Our second cut is vertical, at $x[1]$. Our first cut has a $totalCost$ of $2$ because we are making a cut with cost $cost\text{_}y[1]=2$ across $1$ segment, the uncut board. The second cut also has a $totalCost$ of $2$ but we are making a cut of cost $cost\text{_}x[1]=1$ across $2$ segments. Our answer is $minCost=((2\times1)+(1\times2))\ \text{\%}\ (10^9+7)=4$.

Sample Input 1

1
6 4
2 1 3 1 4
4 1 2

Sample Output 1  

42

Explanation 1 

Our sequence of cuts is: $y[5]$, $x[1]$, $y[3]$, $y[1]$, $x[3]$, $y[2]$, $\boldsymbol{y}\left[4\right]$ and $x[2]$. 

Cut 1: Horizontal with cost $\text{cost}_{-}y[5]=4$ across $1$ segment. $totalCost=4\times1=4$. 

Cut 2: Vertical with cost $cost\text{_}x[1]=4$ across $2$ segments. $totalCost=4\times2=8$. 

Cut 3: Horizontal with cost $cost\text{_}y[3]=3$ across $2$ segments. $totalCost=3\times2=6$. 

Cut 4: Horizontal with cost $cost\text{_}y[1]=2$ across $2$ segments. $totalCost=2\times2=4$. 

Cut 5: Vertical with cost $cost\text{_}x[3]=2$ across $4$ segments. $totalCost=2\times4=8$. 

Cut 6: Horizontal with cost $cost\text{_}y[2]=1$ across $3$ segments. $totalCost=1\times3=3$. 

Cut 7: Horizontal with cost $cost\text{_}y[4]=1$ across $3$ segments. $totalCost=1\times3=3$. 

Cut 8: Vertical with cost $cost\text{_}x[2]=1$ across $\boldsymbol{6}$ segments. $totalCost=1\times6=6$.      

$totalCost=4+8+6+4+8+3+3+6=42$. We then print the value of $42\%(10^9+7)$.
