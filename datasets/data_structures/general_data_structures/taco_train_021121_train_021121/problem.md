Consider a permutation, $p_i$, of integers from $1$ to $n$. Let's determine the $distance$ of $p_i$ to be the minimum absolute difference between any $2$ consecutive integers in $p_i$: 
$distance(p_i)=\underset{0\le j<n-1}{\text{min}}\big|\ p_i[j]-p_i[j+1]\ |\ \text{if}\ n>1,\text{or}\ 0\ \text{if}\ n=1$

Generate a lexicographically sorted list of all permutations of length $n$ having a maximal distance between all permutations of the same length. Print the lexicographically $k^{th}$ permutation.

Input Format

The first line contains an integer, $\boldsymbol{\boldsymbol{t}}$ (the number of test cases).

The $\boldsymbol{\boldsymbol{t}}$ subsequent lines each contain two space-separated integers, $n_i$ (the permutation length) and $k_i$ (the 1-based index in the list of permutations having a maximal distance), respectively. The $i^{\mbox{th}}$ line corresponds to the $i^{\mbox{th}}$ test case. 

Note: It is guaranteed that the sum of all $n_i$ does not exceed $10^{6}$.

Constraints

$1\leq t\leq10$
$1\leq n_i\leq10^6$
$1\leq k_i\leq10^{18}$

Output Format

For each test case: if the list of permutations having maximal distance has at least $\boldsymbol{\mbox{k}}$ elements, print the $k^{th}$ permutation as sequential (i.e.: from $1$ to $n$) space-separated integers on a new line; otherwise, print $-1$.

Sample Input
3
3 5
4 2
4 3

Sample Output
3 1 2
3 1 4 2
-1

Explanation

For $n=3$ and $k=5$: 

$p_1=[1,2,3];distance(p_1)=min(~|1-2|,|2-3|~)=min(1,1)=1$ 

$p_2=[1,3,2];distance(p_2)=min(~|1-3|,|3-2|~)=min(2,1)=1$ 

$p_3=[2,1,3];distance(p_3)=min(~|2-1|,|1-3|~)=min(1,2)=1$ 

$p_4=[2,3,1];distance(p_4)=min(\:|2-3|,|3-1|\:)=min(1,2)=1$ 

$p_5=[3,1,2];distance(p_5)=min(~|3-1|,|1-2|~)=min(2,1)=1$ 

$p_6=[3,2,1];distance(p_6)=min(\:|3-2|,|2-1|\:)=min(1,1)=1$           

Each of the $\boldsymbol{6}$ permutations has distance $1$. We choose the fifth one (because $k=5$), and print 3 1 2 on a new line.

For $n=4$ and $k=2$: 

The maximal distance in the list of permutations of integers from $1$ to $\begin{array}{c}4\end{array}$ is $2$, and the only permutations having that distance are $P_{11}=[2,4,1,3]$ and $P_{14}=[3,1,4,2]$. We choose the second one (because $k=2$), and print 3 1 4 2 on a new line.
