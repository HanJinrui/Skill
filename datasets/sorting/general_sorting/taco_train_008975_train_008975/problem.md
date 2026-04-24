There are N cans lying on the X-axis at points X_{i} (1 ≤ i ≤ N). Each of the N cans is associated with two values A_{i} and B_{i}.  Also, the segment between the points L and R (L ≤ R) is considered to be green zone including the points L and R. 
There are two types of operations - 

1. Select a can i out of the N cans and move it one unit in either direction along the axis, i.e. if before the operation can is at X_{i} then after the operation, it moves to either X_{i}+1 or X_{i}-1. This costs B_{i} coins and it can be performed any number of times for each of the cans.

2. Choose any integer k and shift the green zone to the segment between L' and R', where L' and R' are the mirror images of points R and L with respect to line X=k respectively. This operation should be performed exactly once. 

After all the operations, you get number of coins equal to sum of values of A_{i} of the cans which lie in the final green zone. 
We define the net coins as:  
\texttt{Number of coins you get - Number of coins spent}

Find the maximum possible net coins you can earn.

------ Input Format ------ 

- First line will contain T, number of testcases. Then the testcases follow.
- Each of the testcases consists of four lines.
- First lines consists of three integers N, L and R.
- Next line consist of N space separated integers X_{1}, X_{2}, ..., X_{N}.
- Next line consist of N space separated integers A_{1}, A_{2}, ..., A_{N}.
- Next line consist of N space separated integers B_{1}, B_{2}, ..., B_{N}.

------ Output Format ------ 

For each testcase, output in a single integer, the maximum number of net coins you can earn.

------ Constraints ------ 

$1 ≤ T ≤ 1000$
$1 ≤ N ≤ 3\cdot 10^{5}$
$1 ≤ A_{i}, B_{i} ≤ 10^{9}$
$-10^{9} ≤ L ≤  R ≤ 10^{9}$
$ -10^{9} ≤ X_{i} ≤ 10^{9}$
- Sum of $N$ over all test cases does not exceed $3\cdot 10^{5}$

----- Sample Input 1 ------ 
2
1 7 10
2
6
1
3 7 10
2 8 1
6 20 1
1 3 2

----- Sample Output 1 ------ 
6
22

----- explanation 1 ------ 
Test case $1$ : Lets choose the axis at $X=5$ and Shift the green zone in the range $[0,3]$, such that can lies in green zone. So, there is no need for operation of type $1$ and total number of coins earned is $A_{1}$, i.e. $6$. 

Test case $2$ : Choose the axis at $X=8$, so the new green zone lies in the region $[6,9]$. Move the can $1$ to $X=6$. Number of coins received is equal to $A_{1}+A_{2}$ and number of coins spent is $4\cdot B_{1}$. So, the net coins earned is $20+6-4=22$. This is also the maximum possible.
