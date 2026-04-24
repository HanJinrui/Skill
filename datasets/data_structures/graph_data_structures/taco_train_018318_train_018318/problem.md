Read problems statements in Mandarin Chinese, Russian and Vietnamese as well. 

While vacationing in Egypt, Chef found a recipe of an ancient dish. The receipt is a sequence of hieroglyphs written on a magic paper - it survived for thousands of years! The sequence is written on a long scroll. Unfortunately, the scroll is split into pieces, and possibly, some pieces of the scroll are missing. Chef has a total of N pieces, numbered for convenience from 1 to N. He gave the pieces of a tape to his friend who studies hieroglyphs for analysis. Chef was happy to hear that there are some relations between the pieces. Some of the pieces may follow other pieces.
The informations about these relations is given as a list of M pairs (A_{i}, B_{i}). Such a pair means that the A_{i}^{th} piece can be immediately followed by the B_{i}^{th} one.
Chef is working on recovering the recipe to prepare this dish for his Egyptian friends. He wants to place all the pieces into lines such that any pair of consecutive pieces (L, R) in a line must be explicitly allowed by one of the M rules described above. In other words, for some i (1 ≤ i ≤ M), (A_{i}, B_{i}) = (L, R). It appears that in general, not all the pieces can be placed in a single line while following the rules. So, please help Chef find what is the minimum number of lines required for all the pieces to be placed acoording to the rules.

------ Input ------ 

The first line of the input contains an integer T denoting the number of test cases. The description of T test cases follows.
The first line of each test case contains two space-separated integers N and M denoting the number of pieces and number of relations of those N pieces. Next M lines contain two space-separated integers A and B denoting that piece number A can be followed by piece number B, all those pairs are guaraneed to be unique within a test case.

------ Output ------ 

For each test case, output a single line containing the minimum number of lines required for all the pieces to be placed acoording to the rules.

------ Constraints ------ 

$1 ≤ T ≤ 20$
$1 ≤ N ≤ 100$
$1 ≤ M ≤ N^{2}$
$1 ≤ A_{i} ≤ N$
$1 ≤ B_{i} ≤ N$
$There is no sequence S_{1}, S_{2}, ..., S_{k} such that the piece S_{i} can be immediately followed by the piece S_{i+1} for all i from 1 to k-1, and that piece S_{k} can be followed by piece S_{1}.$

----- Sample Input 1 ------ 
3

3 3

1 2

2 3

1 3

3 2

1 2

1 3

5 4

1 3

2 3

3 4

2 5
----- Sample Output 1 ------ 
1

2

2
