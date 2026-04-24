The previous challenges covered Insertion Sort, which is a simple and intuitive sorting algorithm with a running time of $unrecognized$. In these next few challenges, we're covering a divide-and-conquer algorithm called Quicksort (also known as Partition Sort).  This challenge is a modified version of the algorithm that only addresses partitioning.  It is implemented as follows: 

Step 1: Divide 

Choose some pivot element, $unrecognized$, and partition your unsorted array, $unrecognized$, into three smaller arrays: $unrecognized$, $unrecognized$, and $unrecognized$, where each element in $unrecognized$, each element in $unrecognized$, and each element in $unrecognized$. 

Example 

$unrecognized$   

In this challenge, the pivot will always be at $unrecognized$, so the pivot is $unrecognized$.

$unrecognized$ is divided into $unrecognized$, $unrecognized$, and $unrecognized$. 

Putting them all together, you get $unrecognized$. There is a flexible checker that allows the elements of $unrecognized$ and $unrecognized$ to be in any order.  For example, $unrecognized$ is valid as well.    

Given $unrecognized$ and $unrecognized$, partition $unrecognized$ into $unrecognized$, $unrecognized$, and $unrecognized$ using the Divide instructions above. Return a 1-dimensional array containing each element in $unrecognized$ first, followed by each element in $unrecognized$, followed by each element in $unrecognized$.   

Function Description  

Complete the quickSort function in the editor below.     

quickSort has the following parameter(s):  

int arr[n]: $unrecognized$ is the pivot element    

Returns   

int[n]: an array of integers as described above   

Input Format

The first line contains $unrecognized$, the size of $unrecognized$. 

The second line contains $unrecognized$ space-separated integers $unrecognized$ (the unsorted array). The first integer, $unrecognized$, is the pivot element, $unrecognized$.

Constraints

$unrecognized$   
$unrecognized$ where $unrecognized$   
All elements are distinct.

Sample Input
STDIN       Function
-----       --------
5           arr[] size n =5
4 5 3 7 2   arr =[4, 5, 3, 7, 2]

Sample Output
3 2 4 5 7

Explanation

$unrecognized$ 
Pivot: $unrecognized$. 

$unrecognized$; $unrecognized$; $unrecognized$

$unrecognized$, so it is added to $unrecognized$. 

$unrecognized$; $unrecognized$; $unrecognized$

$unrecognized$, so it is added to $unrecognized$. 

$unrecognized$; $unrecognized$; $unrecognized$

$unrecognized$, so it is added to $unrecognized$. 

$unrecognized$; $unrecognized$; $unrecognized$

$unrecognized$, so it is added to $unrecognized$. 

$unrecognized$; $unrecognized$; $unrecognized$

Return the array $unrecognized$.

The order of the elements to the left and right of $unrecognized$ does not need to match this answer.  It is only required that $unrecognized$ and $unrecognized$ are to the left of $unrecognized$, and $unrecognized$ and $unrecognized$ are to the right.
