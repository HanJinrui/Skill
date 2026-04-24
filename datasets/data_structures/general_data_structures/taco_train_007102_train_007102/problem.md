Implement a simple text editor. The editor initially contains an empty string, $\mbox{S}$. Perform $Q$ operations of the following $\begin{array}{c}4\end{array}$ types:  

append$\left(\mbox{W}\right)$  - Append string $\mbox{w}$ to the end of $\mbox{S}$.
delete$\left(k\right)$   - Delete the last $\boldsymbol{\mbox{k}}$ characters of $\mbox{S}$.
print$\left(k\right)$     - Print the $k^{th}$ character of $\mbox{S}$.
undo$\left(\right)$     - Undo the last (not previously undone) operation of type $1$ or $2$, reverting $\mbox{S}$ to the state it was in prior to that operation.  

Example   

$S=\textbf{'abcde'}$ 

$ops=[\text{''1}\:\:\textsf{fg'},\:\:\text{'3}\:\text{6'},\:\:\text{'2}\:\text{5'},\:\:\text{'4'},\:\:\text{''3}\:\text{7'},\:\:\text{'4'},\:\:\text{'3}\:\text{4'}]$   

operation
index   S       ops[index]  explanation
-----   ------  ----------  -----------
0       abcde   1 fg        append fg
1       abcdefg 3 6         print the 6th letter - f
2       abcdefg 2 5         delete the last 5 letters
3       ab      4           undo the last operation, index 2
4       abcdefg 3 7         print the 7th characgter - g
5       abcdefg 4           undo the last operation, index 0
6       abcde   3 4         print the 4th character - d

The results should be printed as:  

f
g
d

Input Format

The first line contains an integer, $Q$, denoting the number of operations. 

Each line $\boldsymbol{i}$ of the $Q$ subsequent lines (where $0\leq i<Q$) defines an operation to be performed. Each operation starts with a single integer, $\boldsymbol{\boldsymbol{t}}$ (where $t\in\{1,2,3,4\}$), denoting a type of operation as defined in the Problem Statement above. If the operation requires an argument, $\boldsymbol{\boldsymbol{t}}$ is followed by its space-separated argument. For example, if $t=1$ and $W=\text{"abcd"}$, line $\boldsymbol{i}$ will be 1 abcd. 

Constraints

$1\leq Q\leq10^6$  
$1\leq k\leq|S|$  
The sum of the lengths of all $\mbox{w}$ in the input $\leq10^{6}$.  
The sum of $\boldsymbol{\mbox{k}}$ over all delete operations $\leq2\cdot10^{6}$.  
All input characters are lowercase English letters.  
It is guaranteed that the sequence of operations given as input is possible to perform.

Output Format

Each operation of type $3$ must print the $k^{th}$ character on a new line.

Sample Input
STDIN   Function
-----   --------
8       Q = 8
1 abc   ops[0] = '1 abc'
3 3     ops[1] = '3 3'
2 3     ...
1 xy
3 2
4 
4 
3 1

Sample Output
c
y
a

Explanation

Initially, $\mbox{S}$ is empty. The following sequence of $8$ operations are described below:

$S=\text{"}$. We append $\boldsymbol{abc}$ to $\mbox{S}$, so $S=\text{"}abc"$. 
Print the $3^{rd}$ character on a new line. Currently, the $3^{rd}$ character is c.
Delete the last $3$ characters in $\mbox{S}$ ($\boldsymbol{abc}$), so $S=\text{"}$. 
Append $x_y$ to $\mbox{S}$, so $S=\text{"}xy\text{"}$. 
Print the $2^{nd}$ character on a new line. Currently, the $2^{nd}$ character is y.
Undo the last update to $\mbox{S}$, making $\mbox{S}$ empty again (i.e., $S=\text{"}$).
Undo the next to last update to $\mbox{S}$ (the deletion of the last $3$ characters), making $S=\text{"abc"}$.
Print the $1^{st}$ character on a new line. Currently, the $1^{st}$ character is a.
