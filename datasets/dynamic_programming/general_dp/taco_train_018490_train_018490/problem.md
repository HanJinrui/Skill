Moving ahead, Gudi now enters a room where the floor is divided into  N x M square tiles, forming a grid with N rows and M columns.
Each square in the grid contains a number of Magical Orbs that Gudi has to absorb if she steps on it. Each Orb increases her Kii power, which is needed to fight the demons. Gudi enters the room on (1, 1) with Zero Kii power and has to makes her way to the exit gate on  (N, M), absorbing the Orbs on the way.  From the current cell, she can move only to the adjacent cell in East, South or South-East direction i.e. from (i, j) to either (i, j+1) , (i+1, j) or (i+1, j+1).
However, her capacity for the Orbs is limited. If she absorbs more than K Orbs, she will explode with the large amount of Kii energy! Help her find a way to absorb as any many Orbs as she can, without exploding.  

Input
The first line contains T. T testcases follow.
First line of each testcase contains 3 space-separated integers, N, M, K. 
Each of the following N  lines contain M space-separated integers, describing the grid.  

Output
Print the maximum number of Orbs that she can absorb without exploding or "-1" (without the quotes) if it can not be done i.e. if there does not exist such a path.  Print the answer to each testcase in a new line.  

Constraints:
 1 ≤ T ≤ 10
 1 ≤ N,M ≤ 100
 1 ≤ K ≤ 500
1 ≤ Values in the Grid ≤ 50

SAMPLE INPUT
2
3 3 7
2 3 1
6 1 9
8 2 3
3 4 9
2 3 4 1
6 5 5 3
5 2 3 4

SAMPLE OUTPUT
6
-1

Explanation

In the first testcase, she can move on squares (1,1) , (2,2) and (3,3) to complete her journey with 6 Orbs.
In the second testcase, every possible path leads to the absorption of more than 9 Orbs.
