Bob and Alice like to play the game tower of Hanoi. One day Alice challenges Bob to build the tallest tower from a
set of disks of different height and radius. The tower of Hanoi can be built by stacking disks on top of each other. In order to put disk A on top of disk B, the radius and height of A must be strictly smaller than those of B.  Help Bob to win the challenge.

Input:
First line of input contains number of test cases T.
First line of each test case contains value of  N, the number of disks. The next N lines contains two positive integer number Ri and Hi corresponding to the radius and height of i^th Disk respectively.

Output:
For each test case print the maximum height of the tower possible.  

Constraints:
1 ≤ T ≤ 10
1 ≤ N ≤ 200
1 ≤ Ri, Hi ≤ 10^9

SAMPLE INPUT
2
3
4 3
1 4
3 2
5
5 6
4 3
1 2
7 5
3 4SAMPLE OUTPUT
5
12
