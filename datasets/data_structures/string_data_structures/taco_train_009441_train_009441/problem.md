Sardar Singh has many men fighting for him, and he would like to calculate the power of each of them to better plan for his fight against Ramadhir.

The power of a string S of lowercase English alphabets is defined to be 

\sum_{i = 1}^{|S|} i\cdot ord(S_{i})

where ord(S_{i}) is the position of S_{i} in the alphabet, i.e, ord('a') = 1, ord('b') = 2, \dots, ord('z') = 26.

Each of Sardar Singh's men has a name consisting of lowercase English alphabets. The power of a man is defined to be the maximum power over all possible rearrangements of this string.

Find the power of each of Sardar Singh's men.

------ Input Format ------ 

- The first line of input contains an integer T, denoting the total number of Sardar Singh's men.
- Each of the next T lines contains a single string S_{i}, the name of Sardar Singh's i-th man.

------ Output Format ------ 

- Output T lines, each containing a single integer. The i-th of these lines should have the power of the i-th of Sardar Singh's men.

------ Constraints ------ 

$1 ≤ T ≤ 60$
$1 ≤ |S_{i}| ≤ 100$ 
$S_{i}$ consists of lowercase english alphabets only.

----- Sample Input 1 ------ 
1
faizal
----- Sample Output 1 ------ 
273
----- explanation 1 ------ 
The rearrangement with maximum power is $aafilz$. Its power can be calculated as
$$
1\cdot ord('a') + 2\cdot ord('a') + 3\cdot ord('f') + 4\cdot ord('i') + 5\cdot ord('l') + 6\cdot ord('z')
$$
which equals $273$.
It can be verified that no rearrangement gives a larger power.
