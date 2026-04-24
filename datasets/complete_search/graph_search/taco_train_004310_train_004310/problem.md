Alfie was a prisoner in mythland. Though Alfie was a witty and intelligent guy.He was confident of escaping prison.After few days of observation,He figured out that the prison consists of (N × N) cells.i.e The shape of prison was (N × N) matrix. Few of the cells of the prison contained motion detectors.So Alfie planned that while escaping the prison he will avoid those cells containing motion detectors.Yet before executing his plan,Alfie wants to know the total number of unique possible paths which he can take to escape the prison.Initially Alfie is in cell  
(1,1) while the exit of the cell (N,N).  

note:->Alfie can move in all four direction{ if his current location is  (X,Y), he can move to either 
(X+1,Y), (X-1,Y), (X,Y+1), (X,Y-1) }. If the first cell (1,1) and the last cell(N,N) contain motion detectors,then Alfie can't break out of the prison.

INPUT: 

The first line contain number of test cases "T".T test cases follow.The first line of each test case contains an integer "N",(i.e the size of the (N × N) matrix).The next n lines contain N space separated values either 0 or 1."1" represents a cell containing motion detectors. 

OUTPUT: 

output total number of unique possible paths which he can take to escape the prison.  

Constraint:

1 ≤  T ≤ 20

1 ≤ N ≤ 20

SAMPLE INPUT
3
4
0 1 1 0 
0 0 1 0 
0 0 0 0 
0 1 1 0 
4
0 0 0 1 
0 0 0 0 
1 1 1 0 
1 0 0 0 
4
0 1 1 0 
0 0 1 1 
0 0 0 0 
0 1 0 0 
 
SAMPLE OUTPUT
2
4
4
