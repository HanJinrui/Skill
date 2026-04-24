Read problems statements [Bengali] , [Mandarin chinese] , [Russian] and [Vietnamese] as well.

For her birthday, Rima got an integer sequence $A_{1}, A_{2}, \dots, A_{N}$. Each element of this sequence is either 1 or 2.

Let's call an integer $s$ ($1 ≤ s ≤ 2N$) a *summary integer* if there is a contiguous subsequence of $A$ such that the sum of its elements is equal to $s$.

Rima wants to count all the summary integers. Can you help her?

------  Input ------
The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
The first line of each test case contains a single integer $N$.
The second line contains $N$ space-separated integers $A_{1}, A_{2}, \dots, A_{N}$.

------  Output ------
For each test case, print a single line containing one integer — the number of summary integers.

------  Constraints  ------
$1 ≤ T ≤ 5$
$1 ≤ N ≤ 2 \cdot 10^{6}$
$1 ≤ A_{i} ≤ 2$ for each valid $i$

----- Sample Input 1 ------ 
1
3
2 1 2
----- Sample Output 1 ------ 
4
