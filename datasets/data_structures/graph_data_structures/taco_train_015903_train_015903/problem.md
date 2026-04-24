Dave recently mastered the problem of placing N queens on a chessboard so
that no two queens attack eachother.
Now he wants to see how many knights he can place on a chessboard so
that no two knights attack eachother.
Normally this would be a simple task, but some of the squares of the
chessboard have been marked as unusable and hence cannot have a knight placed
on them.
Recall that a knight can attack another knight if their vertical distance
is 2 and their horizontal distance is 1, or if their vertical distance is 1 and
their horizontal distance is 2.  Only one knight may be placed on each square
of the chessboard

------ Input ------ 

The first line of input contains an integer T (0
Each test case will begin with a line containing 2 integers M and N (0

------ Output ------ 

For each test case, output on a single line the maximum number of knights that may be placed
on the chessboard such that no two attack each other.

----- Sample Input 1 ------ 
2
2 4
....
....
5 5
..#..
#..#.
##...
...##
.....
----- Sample Output 1 ------ 
4
11
----- explanation 1 ------ 
The following image represents the chessboard and a possible solution to the second test case:
