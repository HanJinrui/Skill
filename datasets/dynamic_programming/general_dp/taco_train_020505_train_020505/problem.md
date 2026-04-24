In the middle of a nightmare, Maxine suddenly finds herself in a mysterious room with the following items: 

A piece of paper with the word score and the integer $\mbox{0}$ written on it.
A map of the castle where the room is located.
There are $N$ rooms uniquely labeled from $\mbox{1}$ to $N$.  
There are $N$ bidirectional corridors connecting pairs of rooms. The value of score changes every time she travels up or down a corridor, and this value differs depending on her direction of travel along the corridor. Each corridor can be traveled any number of times in either direction.
Every room is reachable from every other room.  
Maxine is located in the room labeled $\mbox{S}$.  
The exit is located in the room labeled $\boldsymbol{E}$. Once this room is reached, score is reduced modulo $\mbox{M}$ and Maxine can (but is not required to) exit that level! 

Assume some corridor $\boldsymbol{i}$ (where $1\leq i\leq N$) is associated with an integer, $x_i$, and connects rooms $a_i$ and $b_i$. Then:

Traveling corridor $\boldsymbol{i}$ from room $a_i$ to room $b_i$ increases score by $x_i$.
Traveling corridor $\boldsymbol{i}$ from room $b_i$ to room $a_i$ decreases score by $x_i$. 

There are $\mbox{Q}$ levels to Maxine's nightmare castle, and each one has a different set of values for $\mbox{S}$, $\boldsymbol{E}$, and $\mbox{M}$. Given the above information, help Maxine by finding and printing her maximum possible score for each level. Only you can help her wake up from this nightmare!

Note: Recall that the result of a modulo operation is always non-negative.  For example, $(-8)\:\text{mod}\:5=2$.  

Input Format

The first line contains a single integer, $N$, denoting the number of rooms. 

Each of the $N$ subsequent lines describes a corridor in the form of three space-separated integers denoting the respective values for $a_i$, $b_i$, and $x_i$. 

The next line contains a single integer, $\mbox{Q}$, denoting the number of queries. 

Each of the $\mbox{Q}$ subsequent lines describes a level in the form of three space-separated integers denoting its respective $\mbox{S}$, $\boldsymbol{E}$, and $\mbox{M}$ values. 

Constraints

$1\leq N\leq10^5$  
$1\leq a_i,b_i\leq N$, $a_i\neq b_i$  
$1\leq x_i\leq10^9$  
$1\leq Q\leq10^5$  

For each level:

The room layout is the same
$1\leq S,E\leq N$  
$1\leq M\leq10^9$  

Subtask

$1\leq N,Q,M\leq300$ for $30\%$ of max score.

Output Format

For each of the $\mbox{Q}$ levels, print the maximum possible score for that level on a new line.

Sample Input
3
1 3 5
2 3 8
2 1 31
1
1 2 13

Sample Output
12

Explanation

The Sample Input represents the following setup:  

We want to travel from room $\mbox{1}$ to room $2$ while maximizing the value of score. There are at least two ways to achieve the maximum score value of $12$:  

Travel through corridors $5$ times: $1\rightarrow3\rightarrow2\rightarrow1\rightarrow3\rightarrow2$  

$score=(5-8+31+5-8)\ \text{mod}\ 13=25\ \text{mod}\ 13=12$.  

Travel through corridors $\textbf{34}$ times: $1\rightarrow2\rightarrow3\rightarrow1\rightarrow2\rightarrow3\rightarrow1\rightarrow2\rightarrow\text{...}\rightarrow3\rightarrow1\rightarrow2\rightarrow3\rightarrow1\rightarrow2$ 

$score=-339\ \text{mod}\ 13=12$, because $12$ is the smallest non-negative integer $\boldsymbol{x}$ such that $13$ divides $(-339-x)$.
