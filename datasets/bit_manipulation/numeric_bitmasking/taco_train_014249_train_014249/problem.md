Xenny had N cubes. Each cube had six faces and each face had a Latin character on each of it's sides. 
Xenny's friend Asdoc had an interesting activity in mind. He gave Xenny a string S and asked him to use the cubes to form that string. Xenny being a very lazy person, just wanted to randomly roll the cubes and then arrange a subset of them, to form the string S. Xenny relied on probability to get the desired string from the characters on the cubes.
Given the character on each face of each of the cubes, find out the the number of ways in which Xenny is able to make string S using the upward facing characters.

Input:

The first line of input consists of 2 space-separated integers - N and K - the number of cubes and the length of string S respectively.
N lines follow. Each line contains 6 space-separated characters, with i^th line representing the characters on the 6 faces of the  i^th cube.
Last line of input contains string S.

Output:

Output the required number of ways MOD 10^9 + 7.

Constraints:

1 ≤ N ≤ 10
1 ≤ K ≤ N
S consists of lower-case Latin characters

SAMPLE INPUT
5 4
a a a a a a
a a a a a a
b b b b b b
c c c c c c
d d d d d d
abcd

SAMPLE OUTPUT
2592

Explanation

Lets number the cubes:
 1. a a a a a a
 2. a a a a a a
 3. b b b b b b
 4. c c c c c c
 5. d d d d d d
We want to form the string: "abcd"

The possible arrangements of cubes are: 1-3-4-5 and 2-3-4-5.
In arrangement 1-3-4-5, there are 6 ways to get 'a', 6 ways to get 'b', 6 ways to get 'c' and 6 ways to get 'd'.
The same number of ways are possible for the arrangement 2-3-4-5.
Hence, total number of ways = 6^4 + 6^4 = 2592.
