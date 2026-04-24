Utkarsh lives in a strange country. The cities of the country are present on x axis. He is currently at a city at x = 0. He needs to reach another city at x = N.
Utkarsh can move only in the positive x direction. Also due to massive traffic in the one dimensional country, at any time = T seconds, a person can make one of the following things.
Stay at his current position 
Make a jump of length T. (i.e. move from x = cur to x = cur+T)

You need to tell the minimum time Utkarsh will take to reach his destination.

INPUT
First line contains an integer T, the number of test cases.
Each test case contains a single integer N on separate line.

OUTPUT
For each test case print the minimum time to reach the city at x = N.

CONSTRAINTS
1 ≤ T ≤ 10^5 
1 ≤ N ≤ 10^{18}  

SAMPLE INPUT
2
2
3

SAMPLE OUTPUT
2
2

Explanation

For testcases:
Stay at x=0 at time = 1; Move to x=2 at time = 2
Move to x=1 at time = 1; Move to x=3 at time = 2
