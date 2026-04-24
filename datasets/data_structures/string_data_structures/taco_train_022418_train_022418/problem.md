Read problems statements in [Hindi], [Mandarin Chinese], [Russian], [Vietnamese], and [Bengali] as well.

In Chefland, each person has their own non-empty personal string. When two people with personal strings $T_{1}$ and $T_{2}$ (possibly identical) become friends in Chefland, their strings are replaced by a new string $S = T_{1} + T_{1} + T_{2} + T_{2}$, where $+$ denotes string concatenation.

Chef recently became friends with Chefina. However, Chefina's personal string was her favourite and she got upset when it was replaced by $S$. She wanted her personal string back. Chef does not remember $T_{1}$ and $T_{2}$ now, he only knows $S$.

Find the number of ways in which Chef can retrieve valid strings $T_{1}$ and $T_{2}$ from the given string $S$. It is also possible that Chef does not remember $S$ correctly, in which case there is no way to retrieve $T_{1}$ and $T_{2}$.

------  Input ------
The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
The first and only line of each test case contains a single string $S$.

------  Output ------
For each test case, print a single line containing one integer ― the number of ways to retrieve $T_{1}$ and $T_{2}$ from $S$.

------  Constraints ------
$1 ≤ T ≤ 10^{4}$
$4 ≤ |S| ≤ 10^{5}$
$|S|$ is divisible by $2$
$S$ contains only lowercase English letters
the sum of $|S|$ over all test cases does not exceed $2 \cdot 10^{6}$

----- Sample Input 1 ------ 
3

abcd

aaaa

ababcdccdc
----- Sample Output 1 ------ 
0

1

1
----- explanation 1 ------ 
Example case 1: There is no way to choose $T_{1}$ and $T_{2}$.

Example case 2: Both $T_{1}$ and $T_{2}$ must be "a".
