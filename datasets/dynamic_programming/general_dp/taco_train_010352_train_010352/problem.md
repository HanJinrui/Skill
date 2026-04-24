There are $n$ gold mines along a river, and each mine $i$ produces $w_i$ tons of gold. In order to collect the mined gold, we want to redistribute and consolidate it amongst exactly $k$ mines where it can be picked up by trucks. We do this according to the following rules:

You can move gold between any pair of mines (i.e., $i$ and $j$, where $1\leq i<j\leq n$).
All the gold at some pickup mine $i$ must either stay at mine $j$ or be completely moved to some other mine, $j$.
Move $w$ tons of gold between the mine at location $x_i$ and the mine at location $x_j$ at a cost of $|x_i-x_j|\times w.$.

Given $n$, $k$, and the amount of gold produced at each mine, find and print the minimum cost of consolidating the gold into $k$ pickup locations according to the above conditions.

Input Format

The first line contains two space-separated integers describing the respective values of $n$ (the number of mines) and $k$ (the number of pickup locations). 

Each line $i$ of the $n$ subsequent lines contains two space-separated integers describing the respective values of $x_i$ (the mine's distance from the mouth of the river) and $w_i$ (the amount of gold produced in tons) for mine $ia$. 

Note: It is guaranteed that the mines are will be given in order of ascending location.

Constraints

$1\leq k<n\leq5000$
$1\leq w_{i},x_{i}\leq10^{6} $

Output Format

Print a single line with the minimum cost of consolidating the mined gold amongst $k$ different pickup sites according to the rules stated above.

Sample Input 0

3 1
20 1
30 1
40 1

Sample Output 0

20

Explanation 0 

We need to consolidate the gold from $n=3$ mines into a single pickup location (because $k=1$). The mines are all equidistant and they all produce the same amount of gold, so we just move the gold from the mines at locations $x=20$ and $x=40$ to the mine at $x=30$ for a minimal cost of $20$.

Sample Input 1

3 1
11 3
12 2
13 1

Sample Input 1

4

Explanation 1 

We need to consolidate the gold from $n=3$ mines into a single pickup location (because $k=1$). We can achieve a minimum cost of $4$ by moving the gold from mines $x=12$ and $x=13$ to the mine at $x=11$.

Sample Input 2

6 2
10 15
12 17
16 18
18 13
30 10
32 1

Sample Output 2

182

Explanation 2 

We need to consolidate the gold from $n=6$ mines into $k=2$ pickup locations. We can minimize the cost of doing this by doing the following:

Move the gold from the mines at locations $x=10$, $x=16$, and $x=18$ to the mine at $x=12$.   
Move the gold from the mine at location $x=32$ to the mine at $x=30$.
