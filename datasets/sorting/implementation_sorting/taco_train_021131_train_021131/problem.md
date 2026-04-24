Shil got an array of N integers as a present on his birthday. But he didn't liked it. Shil wants to make this array beautiful. Shil considers an array A1,A2,A3 . . . AN beautiful if  A1 > AN. Inorder to make it beautiful Shil can swap any two  numbers in the array. Also Shil can perform this operation any number of times on any adjacent pairs of integers in the array A.Find the number of ways in which Shil can make this array beautiful.Two ways are considered same if resulting array after making all the swaps have same A1 and AN.

Input
First line of input contains an integer N denoting the number of elements in an array A. Next line of input contains N space separated integers denoting A1,A2,A3 . . . AN respectively.  

Output
Number of ways in which you can make given array beautiful.

Constraints
1 ≤ N ≤ 10^6
1 ≤ Ai ≤ 10^6

Warning
Prefer to use fast I/O methods.

SAMPLE INPUT
5
1 4 3 2 5

SAMPLE OUTPUT
10

Explanation

Total number of ways are (5,1),(4,1),(3,1),(2,1),(5,2),(4,2),(3,2),(5,3),(4,3),(5,4).
First number in above pair is A[1] and second number is A[N].Note that two ways are considered same if A[1] and A[N] are same in resulting array after swaps.
