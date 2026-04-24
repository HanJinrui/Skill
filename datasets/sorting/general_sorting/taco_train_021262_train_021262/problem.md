Puchi hates to carry luggage, but unfortunately he got a job to carry the luggage of his N friends in office. Each day,  one of his N friends, gives him the luggage of a particular weight to carry. You will be given the weight of luggage of each friend in the array Weight, where Weighti is the weight of luggage of i^th friend carried by Puchi on i^th day. It is given that all the luggages carried by Puchi are distinct in their weights. 
As Prateek assigned this job to Puchi, so for each day, he wants to know the number of days in future when Puchi will have to carry the luggage , having  weight less than the weight of luggage of current day.
Please help Prateek for the same.

Input:
The first line contains a single integer T, denoting the number of test cases. In each test case, the following input will be present: 
First line contains an integer N, where N represents the number of friends.
Next N line contains N integers, where i^th line contains i^th integer, which represents Weighti.   

Output:
Output exactly T lines. Each line contains N integer separated by a space, where i^th integer represents the number of luggage of future, which are less than the weight of luggage of the current day.

Constraints:

Subtask 1:
1 ≤ T ≤ 30
1 ≤ N ≤ 10^4
1 ≤ Weighti ≤ 10^6 
Subtask 2:
1 ≤ T ≤ 10
1 ≤ N ≤ 10^5
1 ≤ Weighti ≤ 10^6

SAMPLE INPUT
1
4
2
1
4
3

SAMPLE OUTPUT
1 0 1 0

Explanation

In sample input, given T =1 in first line and N = 4 in next line. In next 4 lines, Weighti i.e weight of luggage of each friend on i^th day is given.

For weight on first day i.e 2 ,future weights smaller than 2 are   {1} . Therefore output for this weight will be 1.
For weight on second day i.e 1, no future weights are smaller than 1. So output for this weight will be 0.
For weight on third day i.e 4, future weights smaller than  4 are {3}. So output for this weight will be 1.
For weight on fourth day i.e 3, no future weights are smaller than 3. So output for this weight will be 0.
So the final output is {1, 0, 1, 0}.
