Read problem statements in [Hindi], [Bengali], [Mandarin Chinese], [Russian], and [Vietnamese] as well.

Сhef has assembled a football team! Now he needs to choose a name for his team. There are $N$ words in English that Chef considers *funny*. These words are $s_{1}, s_{2}, \dots, s_{N}$.

Chef thinks that a good team name should consist of two words such that they are not funny, but if we swap the first letters in them, the resulting words are funny. Note that under the given constraints, this means that a word is a non-empty string containing only lowercase English letters.

Can you tell Chef how many good team names there are?

------  Input ------
The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
The first line of each test case contains a single integer $N$.
The second line contains $N$ space-separated strings $s_{1}, s_{2}, \ldots, s_{N}$.

------  Output ------
For each test case, print a single line containing one integer — the number of ways to choose a good team name.

------  Constraints ------
$1 ≤ T ≤ 100$
$2 ≤ N ≤ 2 \cdot 10^{4}$
$2 ≤ |s_{i}| ≤ 20$ for each valid $i$
$s_{1}, s_{2}, \ldots, s_{N}$ contain only lowercase English letters
$s_{1}, s_{2}, \ldots, s_{N}$ are pairwise distinct
the sum of $N$ over all test cases does not exceed $2 \cdot 10^{4}$

------  Subtasks ------
Subtask #1 (20 points): $s_{1}, s_{2}, \ldots, s_{N}$ contain only letters 'a' and 'b'

Subtask #2 (80 points): original constraints

----- Sample Input 1 ------ 
3

2

suf mas

3

good game guys

4

hell bell best test
----- Sample Output 1 ------ 
2

0

2
----- explanation 1 ------ 
Example case 1: The good team names are ("muf", "sas") and ("sas", "muf").

Example case 2: There are no good team names because all funny words start with 'g'.

Example case 3: The good team names are ("hest", "tell") and ("tell", "hest").
