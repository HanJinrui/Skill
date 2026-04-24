You are given two positive integers $\class{ML__boldsymbol}{\boldsymbol{a}}$ and $\boldsymbol{b}$ in binary representation. You should find the following sum modulo $10^9+7$:

$\sum\limits_{i=0}^{314159}\left(a\:x or\left(b\:s h l\:i\right)\right)$

where operation $\boldsymbol{x}\textbf{or}$ means exclusive OR operation, operation $\mbox{shl}$ means binary shift to the left.

Please note, that we consider ideal model of binary integers. That is there is infinite number of bits in each number, and there are no disappearings (or cyclic shifts) of bits.

Input Format

The first line contains number $\class{ML__boldsymbol}{\boldsymbol{a}}$ $(1\leq a<2^{10^{5}})$ in binary representation. The second line contains number $\boldsymbol{b}$ $(1\leq b<2^{10^{5}})$ in the same format. All the numbers do not contain leading zeros.

Output Format

Output a single integer $-$ the required sum modulo $10^9+7$.

Sample Input
10
1010

Sample Output
489429555
