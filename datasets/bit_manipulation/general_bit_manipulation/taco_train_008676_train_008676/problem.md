The Wingman gains the attention of a prospective partner for their friend, by tapping them on the shoulder, and then stating only the line "Haaaaave you met Ted?" (substituting the name of "Ted", the main protagonist of the show, with the name of the single person), and then walking away, leaving the newly acquainted pair to continue a conversation.

Welcome to the world of 2030, where the process has undergone a technical twist. The people now contact only through systems that use unsigned 31-bit passkeys. The entire arrangement is rather simple, to be honest and the passkeys are just binary representations of unique ids attached to each system.  

So, as to establish a connection analogous to the random tap  on the shoulder, you must join the two ids. This joining takes time equal to the hamming distance (Read the PS) between the passkeys.

Find the minimum time in which any two systems can get connected. All the ids are stored in form of a set S.

S is characterized by following properties:
The xor operation is closed in the set, i.e. for any a,b belonging to S, their xor, c=a^b also belongs to S
None of the numbers are repeated.

Input Format:
First line contains T, the number of test cases
Each test case contains two lines. The first line has a single integer N. The second line contains N space separated integers representing the set S.

Output Format:
A single line for each test case containing the answer as explained in the statement.

Constraints:
1 ≤ n ≤ 10^5
s[i] is an unsigned 31 bit integer.
1 ≤ T ≤ 3  

Notes:
1. None of the numbers are repeated in the set S.
2. S does not contain 0.

PS: http://en.wikipedia.org/wiki/Hamming_distance

SAMPLE INPUT
2
3
1 2 3
7
1 2 3 4 5 6 7 


SAMPLE OUTPUT
1
1

Explanation

The set contains 3 numbers.
S = {1, 2, 3}
Now, 1 ^ 2= 3, exists in set
           1 ^ 3 = 2, exists in set
           2 ^ 3 = 1, exists in set

Thus, the stated property holds.
Now, the passkeys are as follows:
- For system with id = 1 : passkey = 01
- For system with id = 2 : passkey = 10
- For system with id = 3 : passkey = 11

(Note that all passkeys have equal length i.e. 31 the prefix zeroes are not displayed for clarity)

We consider all pairs, now... 
id = 1 and id = 2, hamming distance = 2
id = 1 and id = 3, hamming distance = 1
id = 3 and id = 2, hamming distance = 1

Thus, the required answer is 1.
