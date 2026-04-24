Meereen is famous for its fighting pits where fighters fight each other to the death.

Initially, there are $n$ fighters and each fighter has a strength value. The $n$ fighters are divided into $\boldsymbol{\mbox{k}}$ teams, and each fighter belongs exactly one team. For each fight, the Great Masters of Meereen choose two teams, $\boldsymbol{x}$ and $y$, that must fight each other to the death. The teams attack each other in alternating turns, with team $\boldsymbol{x}$ always launching the first attack. The fight ends when all the fighters on one of the teams are dead.

Assume each team always attacks optimally. Each attack is performed as follows:

The attacking team chooses a fighter from their team with strength $\boldsymbol{\mathrm{~S~}}$.
The chosen fighter chooses at most $\boldsymbol{\mathrm{~S~}}$ fighters from other team and kills all of them. 

The Great Masters don't want to see their favorite fighters fall in battle, so they want to build their teams carefully and know who will win different team matchups. They want you to perform two type of queries:

1 p x Add a new fighter with strength $\boldsymbol{p}$ to team $\boldsymbol{x}$. It is guaranteed that this new fighter's strength value will not be less than any current member of team $\boldsymbol{x}$.
2 x y Print the name of the team that would win a matchup between teams $\boldsymbol{x}$ and $y$ in their current state (recall that team $\boldsymbol{x}$ always starts first). It is guaranteed that $x\neq y$. 

Given the initial configuration of the teams and $\textit{q}$ queries, perform each query so the Great Masters can plan the next fight.

Note: You are determining the team that would be the winner if the two teams fought. No fighters are actually dying in these matchups so, once added to a team, a fighter is available for all future potential matchups.

Input Format

The first line contains three space-separated integers describing the respective values of $n$ (the number of fighters), $\boldsymbol{\mbox{k}}$ (the number of teams), and $\textit{q}$ (the number of queries). 

Each line $\boldsymbol{i}$ of the $n$ subsequent lines contains two space-separated integers describing the respective values of fighter $\boldsymbol{i}$'s strength, $s_i$, and team number, $t_i$. 

Each of the $\textit{q}$ subsequent lines contains a space-separated query in one of the two formats defined in the Problem Statement above (i.e., 1 p x or 2 x y).

Constraints

$1\leq n,q\leq2\times10^5$
$2\leq k\leq2\times10^5$
$1\leq x,y,t_i\leq k$
$1\leq s_i,p\leq2\times10^5$
It is guaranteed that both teams in a query matchup will always have at least one fighter.

Scoring 

This challange has binary scoring. This means you will get a full score if your solution passes all test cases; otherwise, you will get $0$ points.

Output Format

After each type $2$ query, print the name of the winning team on a new line. For example, if $x=1$ and $y=2$ are matched up and $\boldsymbol{x}$ wins, you would print $1$.

Sample Input
7 2 6
1 1
2 1
1 1
1 2
1 2
1 2
2 2
2 1 2
2 2 1
1 2 1
1 2 1
2 1 2
2 2 1

Sample Output
1
2
1
1

Explanation

Team $1$ has three fighters with the following strength levels: $S_1=\{1,1,2\}$. 

Team $2$ has four fighters with the following strength levels: $S_2=\{1,1,1,2\}$.      

The first query matching up team $x=1$ and $y=2$ would play out as follows:

Team $x=1$ attacks $\rightarrow$ The fighter with strength $2$ can kill one fighter with strength $2$ and one fighter with strength $1$. Now, $S_1=\{1,1,2\}$, and $S_2=\{1,1\}$.
Team $x=2$ attacks $\rightarrow$ The fighter with strength $1$ can kill the fighter with strength $2$. Now, $S_1=\{1,1\}$, and $S_2=\{1,1\}$.
Team $x=1$ attacks $\rightarrow$ The fighter with strength $1$ can kill one fighter with strength $1$. Now, $S_1=\{1,1\}$, and $S_2=\{1\}$.
Team $x=2$ attacks $\rightarrow$ The fighter with strength $1$ can kill one fighter with strength $1$. Now, $S_1=\{1\}$, and $S_2=\{1\}$.
Team $x=1$ attacks $\rightarrow$ The fighter with strength $1$ can kill the last fighter with strength $1$. Now, $S_1=\{1\}$, and $S_2=\{\}$.

After this last attack, all of Team $2$'s fighters would be dead. Thus, we print $1$ as team $1$ would win that fight.
