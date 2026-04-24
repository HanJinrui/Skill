Alice is a geeky girl. She has a lot of codes to execute but she always choose a lucky time to execute a code. 
Time is shown in 24 hour format as hh:mm:ss
Time is said to be lucky if all the 6 characters (except ':') are different.

Given the time when she completed the code find a lucky time to execute it so that Alice need to wait as little as possible.

Input :

First line contains T, the number of test cases. Each of next T lines contains time when she completes a code (in format described above).

Output:

For each test case, output a single line containing lucky time (in format described above)

Constraints :

0 ≤  hh < 24

0 ≤ mm < 60

0 ≤  ss  < 60

SAMPLE INPUT
3
00:00:00
12:59:59
23:59:59

SAMPLE OUTPUT
01:23:45
13:02:45
01:23:45
