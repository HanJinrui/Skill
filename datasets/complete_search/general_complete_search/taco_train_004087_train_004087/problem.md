King Richard is leading a troop of $N^2$ knights into battle! Being very organized, he labels his knights $K_0,K_1,\ldots,K_{N^2-1}$ and arranges them in an $N\times N$ square formation, demonstrated below:

Before the battle begins, he wants to test how well his knights follow instructions. He issues $\mbox{S}$ drill commands, where each command follows the format $a_{i}$ $b_{i}$ $d_{i}$ and is executed like so:

All knights in the square having the top-left corner at location $(a_i,b_i)$ and the bottom-right corner at location $(a_i+d_i,b_i+d_i)$ rotate $90^{\circ}$ in the clockwise direction. Recall that some location $(r,c)$ denotes the cell located at the intersection of row $\textbf{r}$ and column $\textbf{c}$. For example:

You must follow the commands sequentially. The square for each command is completely contained within the square for the previous command. Assume all knights follow the commands perfectly.

After performing all $\mbox{S}$ drill commands, it's time for battle! King Richard chooses knights $K_{w_1},K_{w_2},...,K_{w_L}$ for his first wave of attack; however, because the knights were reordered by the drill commands, he's not sure where his chosen knights are!

As his second-in-command, you must find the locations of the knights. For each knight $K_{w_1}$, $K_{w_{2}},\ldots,K_{w_{L}}$, print the knight's row and column locations as two space-separated values on a new line.  

Input Format

This is broken down into three parts:

The first line contains a single integer, $N$.       
The second line contains a single integer, $\mbox{S}$. 

Each line $\boldsymbol{i}$ of the $\mbox{S}$ subsequent lines describes a command in the form of three space-separated integers corresponding to $a_i$, $b_i$, and $d_i$, respectively.  
The next line contains a single integer, $\boldsymbol{\mbox{L}}$. 
Each line $j$ of the $\boldsymbol{\mbox{L}}$ subsequent lines describes a knight the King wants to find in the form of a single integer corresponding to $w_j$.  

Constraints

$1\leq S\leq2\cdot10^5$  
$7\leq N\leq3\cdot10^7$
$1\leq a_i,b_i\leq N$  
$0\leq d_i<N$  
$a_{i-1}\leq a_i$ and $a_{i}+d_{i}\leq a_{i-1}+d_{i-1}$  
$b_{i-1}\leq b_{i}$ and $b_i+d_i\leq b_{i-1}+d_{i-1}$  
$1\leq L\leq2\cdot10^5$  
$0\leq w_j<N^2$  

Subtask     

$7\leq N\leq3000$ for $25\%$ of the maximum score.  

Output Format

Print $\boldsymbol{\mbox{L}}$ lines of output, where each line $j$ contains two space-separated integers describing the respective row and column values where knight $K_{w_j}$ is located.  

Sample Input
7
4
1 2 4
2 3 3
3 4 1
3 4 0
7
0
6
9
11
24
25
48

Sample Output
1 1
1 7
4 6
3 4
2 5
2 4
7 7

Explanation

The following diagram demonstrates the sequence of commands:

Click here to download a larger image.

In the final configuration:

Knight $\mathbf{K_0}$ is at location $(1,1)$
Knight $\mathbf{K_6}$ is at location $(1,7)$
Knight $\mathbf{K}_{9}$ is at location $(4,6)$
Knight $K_{11}$ is at location $(3,4)$
Knight $K_{24}$ is at location $(2,5)$
Knight $K_{25}$ is at location $(2,4)$
Knight $K_{48}$ is at location $(7,7)$
