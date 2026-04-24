A $10\times10$ Crossword grid is provided to you, along with a set of words (or names of places) which need to be filled into the grid.  Cells are marked either + or -.  Cells marked with a - are to be filled with the word list.  

The following shows an example crossword from the input $crossword$ grid and the list of words to fit, $words=[PLAND,LHASA,SPAIN,INDIA]$:

Input 	   		Output

++++++++++ 		++++++++++
+------+++ 		+POLAND+++
+++-++++++ 		+++H++++++
+++-++++++ 		+++A++++++
+++-----++ 		+++SPAIN++
+++-++-+++ 		+++A++N+++
++++++-+++ 		++++++D+++
++++++-+++ 		++++++I+++
++++++-+++ 		++++++A+++
++++++++++ 		++++++++++
POLAND;LHASA;SPAIN;INDIA

Function Description

Complete the crosswordPuzzle function in the editor below.  It should return an array of strings, each representing a row of the finished puzzle.

crosswordPuzzle has the following parameter(s):  

crossword: an array of $10$ strings of length $10$ representing the empty grid  
words: a string consisting of semicolon delimited strings to fit into $crossword$  

Input Format

Each of the first $10$ lines represents $crossword[i]$, each of which has $10$ characters, $crossword[i][j]$.

The last line contains a string consisting of semicolon delimited $words[i]$ to fit.  

Constraints

$1\leq|words|\leq10$ 

$crossword[i][j]\in\{+,-\}$ 

$words[i][j]\in ascii[A-Z]$  

Output Format

Position the words appropriately in the $10\times10$ grid, then return your array of strings for printing.  

Sample Input 0
+-++++++++
+-++++++++
+-++++++++
+-----++++
+-+++-++++
+-+++-++++
+++++-++++
++------++
+++++-++++
+++++-++++
LONDON;DELHI;ICELAND;ANKARA

Sample Output 0
+L++++++++
+O++++++++
+N++++++++
+DELHI++++
+O+++C++++
+N+++E++++
+++++L++++
++ANKARA++
+++++N++++
+++++D++++

Sample Input 1
+-++++++++
+-++++++++
+-------++
+-++++++++
+-++++++++
+------+++
+-+++-++++
+++++-++++
+++++-++++
++++++++++
AGRA;NORWAY;ENGLAND;GWALIOR

Sample Output 1
+E++++++++
+N++++++++
+GWALIOR++
+L++++++++
+A++++++++
+NORWAY+++
+D+++G++++
+++++R++++
+++++A++++
++++++++++

Sample Input 2
++++++-+++
++------++
++++++-+++
++++++-+++
+++------+
++++++-+-+
++++++-+-+
++++++++-+
++++++++-+
++++++++-+
ICELAND;MEXICO;PANAMA;ALMATY

Sample Output 2
++++++I+++
++MEXICO++
++++++E+++
++++++L+++
+++PANAMA+
++++++N+L+
++++++D+M+
++++++++A+
++++++++T+
++++++++Y+
