What if we Unite against the Difference between ourselves ?
Welcome into the Brother-Hood town. Citizens of Brother-Hood town are feeling very happy that you came for their help. But what is the problem they have ?

There is one very crucial problem in the town now. Years ago people of town were living together , and were much happy. It did not matter from which society they belong , the only thing matter was living united in Brother-Hood town. Then Polito , citizen of town does not wanted to see this United Bonding anymore. He started creating difference between the people of Brother-Hood.

And somehow he got success in achieving his dream. Now the current scenario is there is almost no Brother-Hood in town.

There are groups created in town. And citizen of town belong to none or more group. 

You will be given the details about these groups , like an integer M will tell the number of members in group and then array G[ ] will tell the Power of ith member in group. 

You can belong to any group who are willing to live united. But you must have the required Power so the Power of United Group is more than the Power of Intersected Group.

Given details about groups ,  tell how much Power you must have to keep the Brother-Hood Town United.

Input : First line will have integer N number of Groups. Next 2 * N will have values of M and G[ ]

Output : Produce required output in one line.

Note : Persons may have same Power ,  you should not consider duplicates. Required power can be negative also. Output may be larger so produce result as modulo 10^9

Constraints

1 ≤ N ≤ 100

1 ≤ M ≤ 10^5

0 ≤ G[i] ≤ 500

SAMPLE INPUT
3
5
1 1 2 3 7
5
3 5 2 1 6
5
1 5 7 8 9

SAMPLE OUTPUT
-1

Explanation

When we do Union of these set we will get 

1 2 3 5 6 7 8 9 

and on Difference we will get 

2 3 5 6 7 8 9 

Now the difference of them is , 40 - 41 = -1 .

Thus answer is -1
