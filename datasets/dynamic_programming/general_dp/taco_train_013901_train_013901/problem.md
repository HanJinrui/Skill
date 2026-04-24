Let's play Fairy Chess!

You have an $n\times n$ chessboard. An $\boldsymbol{\mathrm{~S~}}$-leaper is a chess piece which can move from some square $(x_0,y_0)$ to some square $(x_{1},y_{1})$ if $abs(x_0-x_1)+abs(y_0-y_1)\leq s$; however, its movements are restricted to up ($\uparrow$), down ($\downarrow$), left ($\leftarrow\right.$), and right ($\rightarrow$) within the confines of the chessboard, meaning that diagonal moves are not allowed. In addition, the leaper cannot leap to any square that is occupied by a pawn.

Given the layout of the chessboard, can you determine the number of ways a leaper can move $m$ times within the chessboard?

Note: $abs(x)$ refers to the absolute value of some integer, $\boldsymbol{x}$.

Input Format

The first line contains an integer, $\textit{q}$, denoting the number of queries. Each query is described as follows:

The first line contains three space-separated integers denoting $n$, $m$, and $\boldsymbol{\mathrm{~S~}}$, respectively.
Each line $\boldsymbol{i}$ of the $n$ subsequent lines contains $n$ characters. The $j^{th}$ character in the $i^{\mbox{th}}$ line describes the contents of square $(i,j)$ according to the following key:
. indicates the location is empty.
P indicates the location is occupied by a pawn.
L indicates the location of the leaper.

Constraints

$1\leq q\leq10$
$1\leq m\leq200$
There will be exactly one L character on the chessboard.
The $\boldsymbol{\mathrm{~S~}}$-leaper can move up ($\uparrow$), down ($\downarrow$), left ($\leftarrow\right.$), and right ($\rightarrow$) within the confines of the chessboard. It cannot move diagonally.

Output Format

For each query, print the number of ways the leaper can make $m$ moves on a new line. Because this value can be quite large, your answer must be modulo $10^9+7$.

Sample Input 0
3
4 1 1
....
.L..
.P..
....
3 2 1
...
...
..L
4 3 2
....
...L
..P.
P...

Sample Output 0
4
11
385

Explanation 0

You must perform two queries, outlined below. The green cells denote a cell that was leaped to by the leaper, and coordinates are defined as $(row,column)$.

The leaper can leap to the following locations: 

Observe that the leaper cannot leap to the square directly underneath it because it's occupied by a pawn. Thus, there are $4$ ways to make $1$ move and we print $4$ on a new line. 
The leaper can leap to the following locations: 

Thus, we print $\mbox{11}$ on a new line.

Note: Don't forget that your answer must be modulo $10^9+7$.
