Benny is given two strings S and T. The length of the string S is N and the length of the string T is M respectively. 

Also, imagine that alphabets are cyclic in nature: a-b-c-…-x-y-z-a-b.. and so on. The distance between two letters is the minimal distance between them in the alphabet cycle.  For example, distance between ‘a’ and ‘c’ is 2, when distance between ‘b’ and ‘z’ is 2.

Let’s call the process transformation when one letter turns to another one. The cost of the transformation is the distance between these letters.

She may perform some transformations in string T, but the total cost of these transformations should not exceed K.

Now, she wants to make a string T’ from the given string T such that S appears the most times in T’ as a substring.

For example, abc is a substring of ababc but bac is not a substring of ababc.

Output the maximal numbers of occurrences of string S in T’ after making transformations with total cost not more that K.

Input format

The first line contains three space separated integers N, M and K.

The next two lines contain strings S and and T respectively.

Output format

Print in a single line an answer to the problem.

Constraints
1 ≤ N, M ≤ 200
0 ≤ K ≤ 500

Note
Strings contain only lowercase English letters.

SAMPLE INPUT
3 5 3
aba
zbzbz

SAMPLE OUTPUT
2

Explanation

In the given sample case, she can make ababa from zbzbz. The cost of transformation is not more that K. The number of occurrences of aba in ababa are 2. Hence, the answer is 2.
