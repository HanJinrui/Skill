A binary string of length N is a string of N characters, where each character is either 0 or 1. 

Wet Shark makes a list binStrings, consisting of all 2^N N-digit binary strings. For each string X in binStrings, Wet Shark runs a function ZeroShark(X), defined as follows (psuedocode):

bool ZeroShark(x):
//note the zero indexing
n = length(x)
counter = 0
FOR i = 1 to n-1
    IF x[i] == '0' and x[i - 1] == '0'
        INCREMENT counter
        END IF
ENDFOR
return (counter == 1)

Wet Shark stores an element X in a new list, binTrues  if ZeroShark(X) returns True for that X . In otherwords, binTrues consists of all the elements X in binStrings such that ZeroShark(X) returns True.

Given T testcases, where each testcase consists of integer N, calculate the length of binTrues for each N. Because the lists can get large, output your answer modulo 10^9+7=1000000007

INPUT

The first line of the input contains a single integer T, the number of such N.

The next T lines of the input contain a single integer N, as described in the problem.

OUTPUT

Output T separate lines, each containing the number of elements in the resulting list binTrues for each N in the input. The lists may be large, so output the answer modulo 10^9+7=1000000007

CONSTRAINTS

1 ≤ T ≤ 10

1 ≤ N ≤ 10^5

SAMPLE INPUT
2
2
3

SAMPLE OUTPUT
1
2

Explanation

When N=2, the list binStrings is equal to ['00', '01', '10', '11'].

Calling ZeroShark on each element in binStrings, the function only returns true when X is equal to 00. When X = 01, 10, 11, the counter in ZeroShark is equal to 0. 

Therefore, binTrues is equal to ['00'], and has a length of 1.

When N=3, the list binStrings is equal to ['000', '001', '010', '100', '011', '101', '110', '111'].

Calling ZeroShark on each element in binStrings, the function only returns true when X is equal to 001 or 100. 

Therefore, binTrues is equal to ['001', '100'], and has a length of 2.
