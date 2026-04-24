Fatal Eagle has finally teamed up with Arjit to take on this weird army of zombies and vampires. And they are coming up with strategies to beat these guys on a roll. The simple thing they figured out is that these creatures attack everything by the method of brute force - i.e., the total power they have while attacking is the sum of their individual powers.

Bangalore City has two entrances which are located adjacent to each other. And the members of enemy's army are going to rush over to both the entrances to attack the city. 

The heroes, though, know that they will be facing N enemies who have different individual powers from Power1 to Powern. The enemies attack at a particular entrance if they see a hero standing on that entrance. So basically, the heroes can manipulate an enemy into attacking one particular entrance. 

All the enemies attack one by one, and whenever they see someone standing on one particular entrance, they run attack that particular entrance. Our heroes need to know the number of ways in which they can trick the enemies and beat them!

Fatal Eagle and Arjit have to make sure that the enemies are tricked in such a way - that the sum of the powers of enemies on the 1^st entrance of the city is NEVER greater  than the 2^nd entrance of the city. The number of such ways possible is the number of ways in which they can defeat the enemies.

In any case, if the sum of the powers of the enemies (Brute force!) is greater than or equal to the number of ways in which they can be defeated, print "Got no way out!" otherwise "We will win!" needs to be printed.

Input format:
The first line contains an integer N denoting the number of enemies. On the next line, there will be N integers denoting the individual powers of the N enemies.

Output format:
On the first line of the output print two integers separated by a space, the first one denoting the number of ways in which the task can be performed, the second one denoting the total power the enemies have while attacking. In the next line of the output, you've to print the message as We will win! or Got no way out! accordingly.

Constraints: 
0 ≤ N ≤ 8
0 ≤ Poweri ≤ 500

SAMPLE INPUT
3
1 2 13

SAMPLE OUTPUT
15 16
Got no way out!

Explanation

The thing to remember is that all the enemies come one by one, and their order matters. Some of the possible ways which are valid would be:

- 1, 2 and 13 all on the 2^nd entrance. Final result:
1-2-13.

- Firstly, 13 on the 2^nd entrance, then 1 on the 1^st entrance.  And then, 2 on the 2^nd entrance.  Final result:

13-2
1.
