The evil forest is guarded by vicious mandragoras. Garnet and her pet must make a journey through.  She starts with $1$ health point ($\boldsymbol{\mathrm{~S~}}$) and $0$ experience points.    

As she encouters each mandragora, her choices are:

Garnet's pet eats mandragora $\boldsymbol{i}$. This increments $\boldsymbol{\mathrm{~S~}}$ by $1$ and defeats mandragora $\boldsymbol{i}$.  
Garnet's pet battles mandragora $\boldsymbol{i}$. This increases $\boldsymbol{p}$ by $s\times H[i]$ experience points and defeats mandragora $\boldsymbol{i}$. 

Once she defeats a mandragora, it is out of play.  Given a list of mandragoras with various health levels, determine the maximum number of experience points she can collect on her journey.  

For example, as always, she starts out with $s=1$ health point and $p=0$ experience points.  Mandragoras have the following health values: $H=[3,2,5]$.  For each of the beings, she has two choices, $\boldsymbol{\mathrm{~e~}}$at or $\boldsymbol{b}$attle.  We have the following permutations of choices and outcomes:

Action  s   p
_______ _   __
e, e, e 4   0
e, e, b 3   15
e, b, b 2   14
b, b, b 1   10
b, b, e 2   10
b, e, e 3   9
b, e, b 2   16
e, b, e 3   6

Working through a couple of rows, first, her pet can eat all three and she does not gain any experience points.  In the second row, her pet eats the first two to have $1+2=3$ health points, then battles the beast with $5$ heatlth points to gain $3*5=15$ experience points.  We see that the best option is to eat the beast with $2$ points and battle the others to achieve $2\times(3+5)=16$ experience points.

Function Description  

Complete the mandragora function in the editor below.  It must return an integer that denotes the maximum number of experience points that Garnet can earn.

mandragora has the following parameter(s):  

H: an array of integers that represents the health values of mandragoras  

Input Format

The first line contains an integer, $\boldsymbol{\boldsymbol{t}}$, denoting the number of test cases. Each test case is described over two lines:

The first line contains a single integer $n$, the number of mandragoras in the forest. 
The second line contains $n$ space-separated integers describing the respective health points for the mandragoras $H[H[1],H[2]...H[n]]$.    

Constraints

$1\leq t\leq10^5$   
$1\leq n\leq10^5$   
$1\leq H[i]\leq10^7$, where $1\leq i\leq n$   
The sum of all $n$s in a single test case is $\leq10^{6}$  

Output Format

For each test case, print a single line with an integer denoting the maximum number of experience points that Garnet can earn.

Sample Input
1
3
3 2 2

Sample Output
10 

Explanation

There are $n=3$ mandragoras having the following health points: $H=[3,2,2]$. Initially, $s=1$ and $p=0$. The following is an optimal sequence of actions for achieving the maximum number of experience points possible:  

Eat the second mandragora ($H[2]=2$). $\boldsymbol{\mathrm{~S~}}$ is increased from $1$ to $2$, and $\boldsymbol{p}$ is still $0$. 
Battle the first mandragora ($H[1]=3$). $\boldsymbol{\mathrm{~S~}}$ remains the same, but $\boldsymbol{p}$ increases by $s\times H[1]=2\times3=6$ experience points. 
Battle the third mandragora ($H[3]=2$). $\boldsymbol{\mathrm{~S~}}$ remains the same, but $\boldsymbol{p}$ increases by $s\times H[3]=2\times2=4$ experience points. 

Garnet earns $p=6+4=10$ experience points.
