Read problem statements in [Hindi], [Bengali], [Mandarin Chinese], [Russian], and [Vietnamese] as well.

For an array $B$, while it has more than one element, you can apply an operation on it - you choose any two elements $x,y$  (they may be the same value, but they should have different indices), delete them, and add an element $g(x, y)$ instead. 

Here $g(x, y)$ denotes the highest set bit in $x \oplus y$, or $0$ if they are equal. In other words, $g(x, y) = \max 2^{k}$, such that $2^{k} ≤ (x \oplus y)$ for $x \neq y$, and $g(x,y)=0$ if $x = y$. For example, $g(1,1) = 0, g(1,2) = 2, g(2,4)=4, g(13,17)=16$.

Given an array $B$, we try to apply the operations repeatedly in such a way that when we are left with only one element at the end, that element is as small as possible. Let's denote this smallest possible value of the element at the end as $f(B)$.

You are given an array $A$ with $N$ elements, you need to find the sum of $f(A_{l \ldots r})$ among all subsegments $1 ≤ l ≤ r ≤ N$.

The answer may be large, so you need to find it modulo $998\,244\,353$.

------ Input: ------
The first line contains one integer $N$.
The second line contains $N$ integers $A_{1}, A_{2}, \ldots, A_{N}$.

------ Output: ------
In a single line, print the sum, modulo $998\,244\,353$.

------ Constraints  ------
$1 ≤ N ≤ 300\,000$
$0 ≤ A_{i} < 2^{30}$

------ Subtasks ------
10 points : $1 ≤ N ≤ 10$
10 points : $1 ≤ N ≤ 500$
10 points : $1 ≤ N ≤ 5000$
70 points : $1 ≤ N ≤ 300\,000$

----- Sample Input 1 ------ 
10  

0 1 2 3 4 5 6 7 8 9
----- Sample Output 1 ------ 
160
