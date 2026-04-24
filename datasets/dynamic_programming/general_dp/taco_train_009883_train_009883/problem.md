You are given a grid having N rows and M columns. A grid square can either be blocked or empty. Blocked squares are represented by a '#' and empty squares are represented by '.'. Find the number of ways to tile the grid using L shaped bricks. A L brick has one side of length three units while other of length 2 units. All empty squares in the grid should be covered by exactly one of the L shaped tiles, and blocked squares should not be covered by any tile. The bricks can be used in any orientation (they can be rotated or flipped).

Input Format

The first line contains the number of test cases T. T test cases follow. Each test case contains N and M on the first line, followed by N lines describing each row of the grid.

Constraints

1 <= T <= 50 

1 <= N <= 20 

1 <= M <= 8 

Each grid square will be either '.' or '#'.

Output Format

Output the number of ways to tile the grid. Output each answer modulo 1000000007.

Sample Input
3  
2 4  
....  
....  
3 3  
...  
.#.  
...  
2 2  
##  
##

Sample Output
2  
4  
1

Explanation

NOTE: 

If all points in the grid are blocked the number of ways is 1, as in the last sample testcase.
