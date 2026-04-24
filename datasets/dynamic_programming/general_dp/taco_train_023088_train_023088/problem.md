While switching buildings, he loses height $\boldsymbol{I}$ while jumping.

The second restriction is explained below with an example.

Assume $I=2$. Now Superman is in the 2^{nd} building 5^{th} floor ($B=2$, $F=5$). If he wants to switch to the fifth building ($B=5$), he will lose height ($I=2$), which means he will be at floor 3 at building 5 ($B=5$, $F=3$). He can jump freely from the current floor to the floor below on the same building . That is, suppose if he is at $(B=5,F=4)$, he can go to $(B=5,F=3)$ without any restrictions. He cannot skip a floor while jumping in the same building. He can go to the floor below the current floor of the same building or use his jumping power, switch building, and lose height $\boldsymbol{I}$.

Given the information about the occupied floors in each of the $N$ buildings, help Superman to determine the maximum number of people he can save in one single drop from the top to the bottom floor with the given restrictions.

Input Format

Input starts with three values:  the number of buildings $N$, the height of the buildings $\mbox{H}$, and the height Superman will lose when he switches buildings $\boldsymbol{I}$.

These are followed by $N$ lines. Each $i^{\mbox{th}}$ line starts with a non negative integer $\mbox{u}$ indicating how many people are in the $i^{\mbox{th}}$ building. Each of the following $\mbox{u}$ integers indicates that a person is at height $u_i$ in the $i^{\mbox{th}}$ buiding. Each of the following $\mbox{u}$ integers are given and repetitions are allowed which means there can be more than one person in a floor.

$\boldsymbol{i}$ indicates building number and $j$ indicates floor number. Building number will not be given; since $N$ lines follow the first line, you can assume that the $i^{\mbox{th}}$ line indicates the $i^{\mbox{th}}$ building's specifications.

Constraints 

$1\leq H,N\leq1900$ 

$1\leq I\leq450$ 

$0\leq u\leq1900$ (for each $\boldsymbol{i}$, which means the maximum number of people in a particular building will not exceed $\textbf{1900}$) 

$1\leq u_{ij}\leq H$

Output Format

Output the maximum number of people Superman can save.

Sample Input
4 15 2 
5 1 1 1 4 10
8 9 5 7 7 3 9 8 8
5 9 5 6 4 3
0   

Sample Output
12

Explanation

Input starts with $N=4$, $H=15$, $I=2$ .

$N$ lines follow. Each line describes building $\boldsymbol{i}$.

Each line begins with $\mbox{u}$, which denotes the number of persons in a particular building, followed by floor number, where each person resides. Floor number can repeat as any number of people can reside on a particular floor.  

I've attached a figure here to explain the sample test case.  

You can verify the first building's specifications with the figure. 

$u=5$ (Total number of persons in the first building), followed by 1 1 1 4 10(Floor numbers). 

$1\mbox{st}$ floor = 3 persons.

$4th$ floor = 1 person.

$10th$ floor = 1 person. 

Similarly, the specifications for the other three buildings follow. 

The connected line shows the path which Superman can use to save the maximum number of people. In this case, that number is $12$.

You can also note in the figure that when he switches from Building 2 to Building 3, he loses height $\boldsymbol{I}$ ($I=2$). Similarly, when he switches from Building 3 to Building 1 ,the same height loss happens as mentioned in the problem statement.
