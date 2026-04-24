Given an array A of N elements, find the number of distinct possible sums that can be obtained by taking any number of elements from the array and adding them.

Note that 0 can always be obtained by taking none.

First line of the input contains number of test cases T.
Each test case  has two lines. First line has N, the number of elements in the array followed by N values which are elements of the array.
For each test case, print a single line, the distinct possible sums that can be obtained.

Constraints
1 ≤ T ≤ 10 
1 ≤ N ≤ 100
0 ≤ A[i] ≤ 100 for 0 ≤ i < N

SAMPLE INPUT
3
3
1 2 3
5
5 1 3 2 7
4
1 2 4 8 

SAMPLE OUTPUT
7
19
16

Explanation

For the test case 1: Possible values are 0, 1, 2, 3, 4, 5, 6.
For the test case 2: All numbers between 0 and 18 inclusive.
For the test case 3: All numbers between 0 and 15 inclusive.
