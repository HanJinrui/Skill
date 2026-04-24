View Russian Translation

A wild chemist wants to prepare his mysterious mixture. 

The recipe is very simple, he has already mixed all the necessary powders and the only remaining thing is to add exactly m nanoliters of any liquids. 

In his lab he has n_1 bottles full of liquid called amulus of various capacities and n_2 bottles full of water, also of various capacities. He knows the capacity of each single bottle and he is curious if he can use the bottles he has to produce the mixture. If he decides to use any bottle, he has to use all the liquid inside it. 

Capacities of bottles of amulus are special, because for any two such bottles with capacities c_i and c_j, the following fact is true:

either 2 \cdot c_i ≤q c_j or 2 \cdot c_j ≤q c_i.

Help the chemist decide if he can prepare the mixture or not.

In one test file you have to handle T test cases.

Input format:

In the first line a single integer T is given denoting the number of test cases. Then descriptions of T test cases follow. In the first line of a description of a single test case there are three integers m, n_1 and n_2 ,denoting the number of nanoliliters of liquids needed for the mixture, the number of bottles of amulus available and the number of bottles of water available. In the second line there are n_1 space separated integers denoting capacities of bottles of amulus. In the third line there are n_2 integers denoting capacities of bottles of water.

Output format:

For each test case output either NO if the mixture cannot be produced, or output YES in the first line followed by the second line containing space separated capacities of bottles of amulus that can be used to achieve the goal in non-decreasing order of their capacities. If there are many possible solutions output the one with the greatest sum of capacities of used bottles of amulus, and in case when there are still many possible such solutions, print any of them.

Constraints:

1 ≤q T ≤q 10
1 ≤q m ≤q 10^{18}  
1 ≤q n_1 ≤q 60  
1 ≤q n_2 ≤q 15
1 ≤q capacity of any bottle ≤q 10^{17}
For any two bottles of amulus with capacities c_1 and c_2, either 2 \cdot c_i ≤q c_j or 2 \cdot c_j ≤q c_i

SAMPLE INPUT
2
7 2 2
2 4
1 3
11 2 2
2 4
1 3

SAMPLE OUTPUT
YES
2 4 
NO

Explanation

There are two test cases in the sample. In both of them we have there are two bottles of amulus with capacities 2 and 4, and two bottles of water with capacities 1 and 3. 

In the first test case a mixture of 7 nanoliters can be mixed using both bottles of amulus and a bottle of water with capacity 1. There are other possible solutions, but this one is the one with greatest sum of nanoliters of amulus used among them.

In the second test case there is no possible combination of bottles giving 11 nanoliters of mixture.
