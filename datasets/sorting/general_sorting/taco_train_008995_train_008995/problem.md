In Insertion Sort Part 1, you inserted one element into an array at its correct sorted position. Using the same approach repeatedly, can you sort an entire array?

Guideline: You already can place an element into a sorted array. How can you use that code to build up a sorted array, one element at a time? Note that in the first step, when you consider an array with just the first element, it is already sorted since there's nothing to compare it to.

In this challenge, print the array after each iteration of the insertion sort, i.e., whenever the next element has been inserted at its correct position.  Since the array composed of just the first element is already sorted, begin printing after placing the second element.

Example. 

$n=7$ 

$arr=[3,4,7,5,6,2,1]$   

Working from left to right, we get the following output:

3 4 7 5 6 2 1
3 4 7 5 6 2 1
3 4 5 7 6 2 1
3 4 5 6 7 2 1
2 3 4 5 6 7 1
1 2 3 4 5 6 7

Function Description

Complete the insertionSort2 function in the editor below.  

insertionSort2 has the following parameter(s):  

int n: the length of $\textbf{arr}$  
int arr[n]: an array of integers  

Prints  

At each iteration, print the array as space-separated integers on its own line.  

Input Format

The first line contains an integer, $n$, the size of $\textbf{arr}$. 

 The next line contains $n$ space-separated integers $arr\left[i\right]$.  

Constraints

$1\leq n\leq1000$ 

$-10000\leq arr[i]\leq10000,0\leq i\lt n$ 

Output Format

Print the entire array on a new line at every iteration.

Sample Input
STDIN           Function
-----           --------
6               n = 6
1 4 3 5 6 2     arr = [1, 4, 3, 5, 6, 2]

Sample Output
1 4 3 5 6 2 
1 3 4 5 6 2 
1 3 4 5 6 2 
1 3 4 5 6 2 
1 2 3 4 5 6 

Explanation

Skip testing $\mbox{1}$ against itself at position $\mbox{0}$.  It is sorted. 

Test position $\mbox{1}$ against position $\mbox{0}$: $4>1$, no more to check, no change. 

Print $\textbf{arr}$ 

Test position $2$ against positions $\mbox{1}$ and $\mbox{0}$: 

$3<4$, new position may be $\mbox{1}$.  Keep checking.    
$3>1$, so insert $3$ at position $\mbox{1}$ and move others to the right.   

Print $\textbf{arr}$ 

Test position $3$ against positions $2,1,0$ (as necessary): no change. 

Print $\textbf{arr}$ 

Test position $\begin{array}{c}4\end{array}$ against positions $3,2,1,0$: no change. 

Print $\textbf{arr}$ 

Test position $5$ against positions $4,3,2,1,0$, insert $2$ at position $\mbox{1}$ and move others to the right. 

Print $\textbf{arr}$
