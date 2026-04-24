A young mischievous boy Harsh, got into a trouble when his mechanical workshop teacher
told him to cut Iron rods.
The rod cutting algorithm is as follows:

Step 1.  If the rod can be divided into two equal parts, cut  it and choose any one of them.

Step 2.  Else cut  the rod into two parts having non-zero   integral  lengths such that 
               the difference  between the lengths of the two pieces is minimized, and then choose 
               the piece having smaller length.  

Step 3.  Repeat the above algorithm with the currently chosen piece. If the length of the currently chosen piece becomes 1 ,  stop the algorithm. 

There can be special rods which require Step 2 in every step of its cutting. Harsh want to find out the number of such special rods. Help Harsh to find out the answer. 

Input:
The first line of the input will contain T, the number of test-cases. 
Each subsequent T lines will contain an integer N, where N is the range of lengths of rods from 1 to N .

Output:
For each test-case print the required answer. 

Constraints:

1 ≤ T ≤ 1000
1 ≤ N ≤ 10^9

SAMPLE INPUT
2
3
2

SAMPLE OUTPUT
1
0

Explanation

In the first case there is only 1 such special iron rod,( which is of length 3 ).
A rod of length 3 cannot be divided into two equal parts, so we follow Step 2 and divide the rod into  2 and 1 length rod. ( See that the difference between the two rods obtained is minimum among all the possible choices).
 After that choose the rod having smaller length. Since the length of the currently rod is 1 , the algorithm stops. So we see that during the each step  of cutting (although, there is only 1 step involved in cutting ) we have to do mental calculations using Step 2.  There is no such rod , other than this in the range 1 and 3. So the answer is 1.
In the second case there is no such rod between 1 and 2 , so the answer is 0.
