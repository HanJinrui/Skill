Read problem statements in [Bengali], [Mandarin Chinese], [Russian], and [Vietnamese] as well.

In Chefland, the speed of light is $c\ \mathrm{m}/\mathrm{s}$, and acceleration due to gravity is $g\ \mathrm{m}/\mathrm{s}^2$. 

Find the smallest height (in meters) from which Chef should jump such that during his journey down only under the effect of gravity and independent of any air resistance, he achieves the speed of light and verifies Einstein's theory of special relativity.

Assume he jumps at zero velocity and at any time, his velocity ($v$) and depth of descent ($H$) are related as
$$v^{2} = 2 \cdot g \cdot H.$$

------  Input ------

The first line contains an integer $T$, the number of test cases. Then the test cases follow.
Each test case contains a single line of input, two integers $g$, $c$.

------  Output ------
For each test case, output in a single line the answer to the problem. We can show that under the constraints, the answer is an integer.

----- Sample Input 1 ------ 
3
7 1400
5 1000
10 1000
----- Sample Output 1 ------ 
140000
100000
50000
----- explanation 1 ------ 
Test Case $1$: For Chef to achieve the speed of light, the minimum height required is $\frac{c^{2}}{2 \cdot g}$ = $\frac{1400 \cdot 1400}{14}$ = $140000$ meters.

Test Case $3$: For Chef to achieve the speed of light, the minimum height required is $\frac{c^{2}}{2 \cdot g}$ = $\frac{1000 \cdot 1000}{20}$ = $50000$ meters.
