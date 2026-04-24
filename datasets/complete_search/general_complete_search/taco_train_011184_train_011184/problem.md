The Tower of Hanoi is a famous game consisting of $3$ rods and a number of discs of incrementally different diameters. The puzzle starts with the discs neatly stacked on one rod, ordered by ascending size with the smallest disc at the top. The game's objective is to move the entire stack to another rod, obeying the following rules:

Only one disk can be moved at a time.
In one move, remove the topmost disk from one rod and move it to another rod.  
No disk may be placed on top of a smaller disk.

Gena has a modified version of the Tower of Hanoi. This game of Hanoi has $4$ rods and $n$ disks ordered by ascending size. Gena has already made a few moves following the rules above. Given the state of Gena's Hanoi, determine the minimum number of moves needed to restore the tower to its original state with all disks on rod $1$.  

Note: Gena's rods are numbered from $1$ to $4$. The radius of a disk is its index in the input array, so disk $1$ is the smallest disk with a radius of $1$, and disk $n$ is the largest with a radius of $n$.  

Example 

$posts=[4,3,2,1]$  

In this case, the disks are arranged from large to small across the four rods.  The largest disk, disk $4$, is already on rod $1$, so move disks $3,2$ and $1$ to rod $1$, in that order.  It takes $3$ moves to reset the game.  

$posts=[4,2,2,1]$  

The largest disk, disk $4$ with radius $4$, is already on rod $1$.  Disk $3$ is on rod $2$ and must be below disk $2$.  Move disk $2$ to rod $3$, disk $3$ to rod $1$ and disk $2$ to rod $1$.  Now move disk $1$ to rod $1$.  It takes $3$ moves to reset the game.  

Function Description   

Complete the hanoi function below.  

hanoi has the following parameters:  

int posts[n]: $posts[i]$ is the location of the disk with radius $\boldsymbol{i}$  

Returns  

int:  the minimum moves to reset the game to its initial state  

Input Format

The first line contains a single integer, $n$, the number of disks. 

The second line contains $n$ space-separated integers, where the $i^{\mbox{th}}$ integer is the index of the rod where the disk with diameter $\boldsymbol{i}$ is located.

Constraints

$1\leq n\leq10$

Sample Input
STDIN   Function
-----   --------
3       size of posts[] n = 3
1 4 1   posts = [1, 4, 1]

Sample Output
3

Explanation

$3$ moves are enough to build the tower. Here is one possible solution:
