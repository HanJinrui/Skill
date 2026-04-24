You have N rods with you. The i-th rod has a length of A_{i} and a beauty of B_{i}.

You'd like to arrange these rods side-by-side in some order on the number line, starting from 0.  

Let x_{i} be the starting position of the i-th rod in an arrangement. The beauty of this arrangement is

\sum_{i=1}^N x_{i}\cdot B_{i}

What is the maximum beauty you can attain?

Note that the left endpoint of the first rod you place must be 0, and you cannot leave any space between rods.

------ Input Format ------ 

- The first line of input contains an integer T, denoting the number of test cases.
- Each test case consists of three lines of input.
- The first line of each test case contains a single integer N, the number of rods.
- The second line of each test case contains N space-separated integers A_{1}, A_{2}, \ldots, A_{N}
- The third line of each test case contains N space-separated integers B_{1}, B_{2}, \ldots, B_{N}

------ Output Format ------ 

- For each test case print on a new line the answer: the maximum value of \sum_{i=1}^N x_{i} B_{i} if the order of rods is chosen optimally.

------ Constraints ------ 

$1 ≤ T ≤ 10^{3}$
$1 ≤ N ≤ 10^{5}$
$1 ≤ A_{i} ≤ 10^{4}$
$1 ≤ B_{i} ≤ 10^{4}$
- The sum of $N$ across all testcases won't exceed $10^{5}$.

----- Sample Input 1 ------ 
2
2
1 2
4 6
4
2 8 9 11
25 27 100 45
----- Sample Output 1 ------ 
8
2960
----- explanation 1 ------ 
Test case $1$: Place the second rod followed by the first one. This makes $x_{2} = 0$ and $x_{1} = 2$, giving us a beauty of $2\cdot 4 + 0\cdot 6 = 8$, which is the maximum possible.

Test case $2$: Place the rods in the order $[2, 4, 3, 1]$. This gives us $x = [28, 0, 19, 8]$, and the beauty is $28\cdot 25 + 0\cdot 27 + 19\cdot 100 + 8\cdot 45 = 2960$.
