Read problem statements in [Hindi], [Bengali], [Mandarin Chinese], [Russian], and [Vietnamese] as well.

Chef has been researching ant colonies for many years and finally discovered all their secrets.

An ant colony consists of $N$ distinct lines (numbered $1$ through $N$) that pass through a point $\mathsf{O}$, which is the queen's home. For each valid $i$, there are $M_{i}$ ants on the $i$-th line.

For each valid $i$ and $j$, the $j$-th ant on the $i$-th line initially has a non-zero coordinate $X_{i,j}$ with the following meaning:
The distance of this ant from $\mathsf{O}$ is $|X_{i,j}|$.
Let's choose a direction along the $i$-th line from $\mathsf{O}$. The exact way in which this direction is chosen does not matter here, it only needs to be the same for all ants on the same line.
If $X_{i,j}$ is positive, this ant is at the distance $|X_{i,j}|$ from $\mathsf{O}$ in the chosen direction. Otherwise, it is at this distance from $\mathsf{O}$ in the opposite direction.

In other words, two ants $j$ and $k$ on a line $i$ are at the same side of $\mathsf{O}$ if the signs of $X_{i,j}$ and $X_{i,k}$ are the same or on opposite sides if the signs are different.

All ants move with the same constant speed. Initially, all of them are moving towards $\mathsf{O}$. Whenever two or more ants meet (possibly at $\mathsf{O}$), all of these ants turn around and start moving in the opposite directions with the same speed. We call this a *collision*. Even if an ant reaches $\mathsf{O}$ without meeting an ant there, it keeps moving in the same direction. An ant may change direction multiple times.

Help Chef find the total number of collisions between ants. Note that even if more than two ants meet, it counts as only one collision.

------  Input ------
The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
The first line of each test case contains a single integer $N$.
$N$ lines follow. For each valid $i$, the $i$-th of these lines contains an integer $M_{i}$, followed by a space and $M_{i}$ space-separated integers $X_{i,1}, X_{i,2}, \ldots, X_{i,M_{i}}$.

------  Output ------
For each test case, print a single line containing one integer ― the number of collisions between ants.

------  Constraints ------
$1 ≤ T ≤ 1,000$
$1 ≤ N ≤ 2 \cdot 10^{5}$
$1 ≤ M_{i} ≤ 5 \cdot 10^{5}$ for each valid $i$
$1 ≤ |X_{i,j}| ≤ 10^{9}$ for each valid $i,j$
$X_{i,j} < X_{i,j+1}$ for each valid $i,j$
the sum of $N$ over all test cases does not exceed $2 \cdot 10^{5}$
the sum of $M_{1} + M_{2} + \ldots + M_{N}$ over all test cases does not exceed $10^{6}$

------  Subtasks ------
Subtask #1 (30 points): $N = 1$

Subtask #2 (70 points): original constraints

----- Sample Input 1 ------ 
1

2

2 -2 1

1 2
----- Sample Output 1 ------ 
2
----- explanation 1 ------ 
Example case 1: First, the ants on the first line collide at the coordinate $-1/2$ and change directions. Finally, ant $2$ on the first line collides with the only ant on the second line; this happens at $\mathsf{O}$. No collisions happen afterwards.
