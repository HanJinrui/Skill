Capeta is working part-time for an animal shipping company. He needs to pick up animals from various zoos and drop them to other zoos. The company ships four kinds of animals: elephants, dogs, cats, and mice.

There are $m$ zoos, numbered $1$ to $m$. Also, there are $n$ animals. For each animal $\boldsymbol{i}$, Capeta knows its type $t_i$ (E for elephant, D for dog, C for cat and M for mouse), source zoo $s_i$ where Capeta has to pick it up from, and destination zoo $d_i$ where Capeta needs to deliver it to. 

Capeta is given a truck with a huge capacity where $n$ animals can easily fit. He is also given additional instructions:

He must visit the zoos in increasing order. He also cannot skip zoos. 

Dogs are scared of elephants, so he is not allowed to bring them together at the same time. 

Cats are scared of dogs, so he is not allowed to bring them together at the same time. 
Mice are scared of cats, so he is not allowed to bring them together at the same time. 
Elephants are scared of mice, so he is not allowed to bring them together at the same time. 

Also, loading and unloading animals are complicated, so once an animal is loaded onto the truck, that animal will only be unloaded at its destination. 

Because of these reasons, Capeta might not be able to transport all animals. He will need to ignore some animals. Which ones? The company decided to leave that decision for Capeta. He is asked to prepare a report and present it at a board meeting of the company.

Capeta needs to report the minimum number of zoos that must be reached so that she is able to transport $\boldsymbol{x}$ animals, for each $\boldsymbol{x}$ from $1$ to $n$. 

Complete the function minimumZooNumbers and return an integer array where the $x^{\text{th}}$ integer is the minimum number of zoos that Capeta needs to reach so that she is able to transport $\boldsymbol{x}$ animals, or $-1$ if it is impossible to transport $\boldsymbol{x}$ animals. 

He is good at driving, but not so much at planning. Hence, he needs your help.

Input Format

The first line contains a single integer $\boldsymbol{\boldsymbol{t}}$, the number of test cases.

Each test case consists of four lines. The first line contains two space-separated integers $m$ and $n$. The second line contains $n$ space-separated characters $t_1,t_2,\ldots,t_n$. The third line contains $n$ space-separated integers $s_1,s_2,\ldots,s_n$. The fourth line contains $n$ space-separated integers $d_1,d_2,\ldots,d_n$.  

$t_i$, $s_i$ and $d_i$ are the details for the $\boldsymbol{i}$th animal, as described in the problem statement.

Constraints

$1\leq t\leq10$  
$1\leq m,n\leq5\cdot10^4$  
$1\leq s_i,d_i\leq m$  
$s_i\neq d_i$
$t_i$ is either E, D, C or M

Subtasks  

For $30\%$ of the total score, $m,n\leq10^3$  

Output Format

For each case, print a single line containing $n$ space-separated integers, where the $x^{\text{th}}$ integer is the minimum number of zoos that Capeta needs to reach so that she is able to transport $\boldsymbol{x}$ animals. If it is not possible to transport $\boldsymbol{x}$ animals at all, then put $-1$ instead.

Sample Input 0
2
10 3
E D C
4 1 4
7 5 8
10 6
E D C M E D
1 1 1 2 9 7
2 2 2 4 10 10

Sample Output 0
5 8 -1
2 2 4 10 -1 -1

Explanation 0

First Test Case

Capeta can transport one animal by traveling up to zoo number $5$. Just drop the dog there. Next, in order to transport $2$ animals (elephant and cat), Capeta has to go up to zoo number $8$.

Second Test Case

 Animal: Drop the elephant to zoo $2$.
Animal: Drop the elephant and cat to zoo $2$.
Animal: Drop the elephant and cat to zoo $2$. Then drop the mouse to zoo $4$.
Animal: Drop the elephant and cat to zoo $2$. Then drop the mouse to zoo $4$. Finally, drop either the elephant or the dog to $10$.
It is impossible to transport $5$ or $6$ animals.
