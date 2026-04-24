Mr K has a rectangular plot of land which may have marshes where fenceposts cannot be set. He wants you to find the perimeter of the largest rectangular fence that can be built on this land.

For example, in the following $m\times n=4\times4$ grid, $\boldsymbol{x}$ marks a marsh and $\boldsymbol{.}$ marks good land.

....
..x.
..x.
x...

If we number the rows and columns starting with $\mbox{1}$, we see that there are two main areas that can be fenced: $(1,1)-(3,2)$ and $(1,2)-(4,4)$.  The longest perimeter is $10$.  

Function Description

Complete the kMarsh function in the editor below.  It should print either an integer or impossible.

kMarsh has the following parameter(s):  

grid: an array of strings that represent the grid  

Input Format

The first line contains two space-separated integers $m$ and $n$, the grid rows and columns. 

Each of the next $m$ lines contains $n$ characters each describing the state of the land. 'x' (ascii value: 120) if it is a marsh and '.' ( ascii value:46) otherwise.  

Constraints

$2\leq m,n\leq500$ 

Output Format

Output contains a single integer - the largest perimeter. If the rectangular fence cannot be built, print impossible.

Sample Input 0

4 5
.....
.x.x.
.....
.....

Sample Output 0

14

Explanation 0  

The fence can be put up around the entire field. The perimeter is 
$2*(4-1)+2*(5-1)=14$.

Sample Input 1

2 2
.x
x.

Sample Output 1

impossible

Explanation 1

We need a minimum of 4 points to place the 4 corners of the fence. Hence, impossible. 

Sample Input 2

2 5
.....
xxxx.

Sample Output 2

impossible
