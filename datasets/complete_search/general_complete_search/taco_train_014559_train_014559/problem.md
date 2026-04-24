There are N coins and K people. Each of them can propose a method of distribution of the coins amongst themselves when their chance comes and a vote will occur in favour or against his distribution method between all those members. The person proposing that method of distribution wins the vote if he gets equal or more votes in favour than in against his proposal else he loses. Loosing he would be eliminated and then the next member will now propose his method of distribution amongst the remaining members.
Each person while proposing his method of distribution wants to get the maximum number of coins as well as win the vote.
Each person is smart and knows all the possibilities that may occur from their vote and will cast their vote accordingly.
The first proposal will always be given by 1 if he loses will be followed by 2 and so on (till the Kth person).
In the distribution of the 1^{st} person print the amount of coins each of K people is proposed to get so that he wins the vote.
Example 1:
Input:
N = 100 and K = 2
Output: 100 0
Explanation:
To get the maximum coins the 1^{st} person will propose the 
distribution 100,0 when the vote occurs he will obviously
vote for himself and the second person against him. 
The result of the vote will be 1-1 which means he will 
survive (tie here means victory) the vote.
 
Example 2:
Input:
N = 100 and K = 1
Output: 100
Your Task:  
You don't need to read input or print anything. Your task is to complete the function coinsGame() which takes the integer N and an integer K as input parameters and returns the K space-separated Integers denoting the distribution proposed by the 1^{st} person.
Expected Time Complexity: O(K)
Expected Auxiliary Space: O(1)
 
Constraints:
1<=N<=10^{9}
1<=K<=10^{4}
N>=K

Starter code:
```python
#User function Template for python3





class Solution:

    def coinsGame (self, N, K):

        # code here
```
