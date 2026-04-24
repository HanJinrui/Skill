A Sumo wrestling championship is scheduled to be held this winter in the HackerCity where N wrestlers from different parts of the world are going to participate. The rules state that two wrestlers can fight against each other if and only if the difference in their height is less than or equal to K, 

(i.e) wrestler A and wrestler B can fight if and only if |height(A)-height(B)|<=K.  

Given an array H[], where H[i] represents the height of the i^{th} fighter, for a given l, r where 0 <= l <= r < N, can you count the number of pairs of fighters between l and r (both inclusive) who qualify to play a game?

Input Format 

The first line contains an integer N and K  separated by a single space representing the number of Sumo wrestlers who are going to participate and the height difference K. 

The second line contains N integers separated by a single space, representing their heights H[0] H[1] ... H[N - 1]. 

The third line contains Q, the number of queries. This is followed by Q lines each having two integers l and r separated by a space.  

Output Format 

For each query Q, output the corresponding value of the number of pairs of fighters for whom the absolute difference of height is not greater that K.  

Constraints 

1 <= N <= 100000 

0 <= K <= $10^{9} $

0 <= H[i] <= $10^{9} $

1 <= Q <= 100000 

0 <= l <= r < N  

Sample Input

5 2
1 3 4 3 0
3
0 1
1 3
0 4

Sample Output  

1
3
6

Explanation 

Query #0: Between 0 and 1 we have i,j as (0,1) and |H[0]-H[1]|=2 therefore output is 1. 

Query #1: The pairs (H[1],H[2]) (H[1],H[3]) and (H[2],H[3]) are the pairs such that |H[i]-H[j]| <=2. Hence output is 3. 

Query #2: Apart from those in Query #1, we have (H[0],H[1]), (H[0], H[3]), (H[0], H[4]), hence 6.  

Timelimits

Timelimits are given here
