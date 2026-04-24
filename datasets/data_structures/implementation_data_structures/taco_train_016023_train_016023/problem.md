WizKid went on a trip to Wonderland with his classmates. Now, as you know, going on trips incurs costs including hotel costs, fooding, shopping, etc. And when many people go together, usually one person pays and it is expected that the others will pay back their share. But, after a few days people lost track of who owed whom how much and there was a lot of confusion. 
So WizKid set down to make a program which will help solve all these problems in future. He will record the details of all the people going on the trip and the details of each transaction made on the trip. 
Note: It is not necessary that all the people were present in all transactions. Only those present will share the amount. So he also has to note who all were present, who paid and the amount paid. 
Even after this, one more issue remained about what happens when the amount spent could not be divided equally integrally to each person. Well, he decided that the person who paid the bill will have to bear the little extra cost himself on each bill. 

Now, we need you to simulate the same and give the final summary for each person accordingly.

Input:
First line contains T which is the number of test cases.
First line of each test case consists of 2 integers N and Q where N is the number of people who went on the trip and Q is the number of transactions made. 
N lines follow, each containing the names of the N persons who went on the trip. Each name will be distinct and will be a single word consisting of lowercase or uppercase alphabets only.

Q transactions follow each containing the details of each transaction made.
The first line of each transaction contains the name of the person who paid for the transaction.
The second line of each transaction contains the amount paid by the person for the transaction.
The third line of each transaction contains the number of people(other than the person who paid) M between whom this amount is to be split.
M lines follow each containing the names of the people between whom this amount is to be split.
Output:
For each test case, print N lines containing the final dues for each person in the following manner : 

If a person X is supposed to get Y money from the others, then print "X is owed Y"
If a person X is supposed to pay Y money to the others, then print "X owes Y"
If a person X has no dues, then print "X neither owes nor is owed"

Constraints:

 1  ≤ T ≤ 10 
 2  ≤ N ≤ 50 
 1 ≤ Q ≤ 50  
 1 ≤ M ≤ N-1 
 1 ≤ length of each name ≤ 10  
 1 ≤ all amounts ≤ 1000 

Scoring:

 2 ≤ N ≤ 5, 1 ≤ Q ≤ 5 : (30 pts)
 2 ≤ N ≤ 10, 1 ≤ Q ≤ 10 : (30 pts)
Original Constraints : (40 pts)

SAMPLE INPUT
1
4 2
Alice
Bob
Daniel
Mike
Bob
97
1
Alice
Mike
24
2
Alice
Bob

SAMPLE OUTPUT
Alice owes 56
Bob is owed 40
Daniel neither owes nor is owed
Mike is owed 16

Explanation

After the first transaction, Bob pays 97 for Alice and himself. The share will have to divided as 49 for Bob and 48 for Alice. 
ALICE: Expenses = 48, Paid = 0 
BOB: Expenses = 49, Paid = 49

After the second transaction, Mike spends 24 on Alice, Bob and himself. The share will have to divided equally. So now, 
ALICE:  Expenses = 48+8 , Paid = 0  
BOB:  Expenses = 49+8, Paid = 97  
MIKE:  Expenses = 8, Paid = 24

Thus finally,
ALICE has to pay 56.
BOB will get back 97-49-8 = 40.
MIKE will get back 16.
DANIEL has no dues.
