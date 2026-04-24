In a galaxy far away, there is a constant battle between the republic and the droid army. The droid army decided to launch their final attack on the republic. They have N space-fighters. 

Initially the $i^{th}$ fighter is located at (x_{i}, y_{i}). All of the space-fighters move with constant velocity V units/sec in the positive X direction. 
i.e., fighter at (x_{i}, y_{i}) moves to (x_{i}+V, y_{i}) in 1 second. 
The $ i^{th} $ space-fighter broadcasts enemy information at a frequency f_{i}.

The republic is not scared of the artificially intelligent droid force as they have Yoda. Yoda has a special power, at any time T he can choose a region of the droid army and block one specific frequency F. This power has one constraint; it can be applied only in the form of a two sided unbounded axis parallel rectangular box open towards the both the directions across X axis (refer image below for clarity). If a frequency (F) is blocked all the space-fighters in the region having the frequency F can’t communicate.

Given the initial positions of the space-fighters, and their velocity, you are to answer queries of the following form:

YU YD T

where YU, YD are the bounds on y-axis inside which YODA can block a frequency at time T. 
In the region described by the query, after a time T seconds from the start, if Yoda can chose one frequency (F) he wishes to, what is the maximum number of communications he can block?

Input Format 

Each test case is described as follows; the first line contains 3 space separated integers N - the number of space-fighters, Q - the number of queries you have to answer, and V - the velocity of the space-fighters separated by a single space. 

N lines follow, each containing 3 space separated integers x_{i}, y_{i}, and f_{i}, denoting the x co-ordinate, y co-ordinate and the frequency at which the $ i^{th} $ ship broadcasts respectively. Each of the next Q lines contain 3 space separated integers representing YU, YD, T respectively. Refer the figure for more clarity

Note: Points on the boundaries should be counted as well.

Output Format 

For each query you are to output a single integer denoting the result.

Constraints 

1 <= N <= 50000

1 <= Q <= 30000

1 <= V <= 10000

 $-10^{9}  $<= x_{i} <=  $10^{9} $

 $-10^{9} $ <= y_{i} <=  $10^{9} $

1 <= f_{i} <=  $10^{9} $

 $-10^{9} $ <= YU <= $ 10^{9} $

 $-10^{9}  $<= YD <=  $10^{9} $

1 <= T <= 10000

YU >= YD

Sample Input

5 5 82
-4 1 4
-3 -2 2
-3 5 1
0 -5 2
1 -1 2
1 -1 57
-2 -5 11
5 -5 40
-1 -5 16
5 -1 93

Sample Output

1
2
3
3
1

Explanation
Consider the points ships in the Y-range 1 to -1, they are the (-4, 1) and (1, -1), and both operate on different frequencies, hence the most times a frequency is repeated is once.
