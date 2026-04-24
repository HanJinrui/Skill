Chloe is fascinated by prime numbers. She came across the number $283002$ on a sign and, though the number is not prime, found some primes hiding in it by using the following rules:  

Every three consecutive digits sum to a prime:
$\underbrace{283}002\quad\underbrace{2830}02\quad28\underbrace{300}2\quad283\underbrace{002}$
Every four consecutive digits sum to a prime:
$\underbrace{28300}2\quad\underbrace{28300}2\quad28\underbrace{3002}$
Every five consecutive digits sum to a prime:
$\underbrace{283002}\quad2\underbrace{83002}$

You must answer $\textit{q}$ queries, where each query consists of an integer, $n$. For each $n$, find and print the number of positive $n$-digit numbers, modulo $10^9+7$, that satisfy all three of Chloe's rules (i.e., every three, four, and five consecutive digits sum to a prime).

Input Format

The first line contains an integer, $\textit{q}$, denoting the number of queries. 

Each of the $\textit{q}$ subsequent lines contains an integer denoting the value of $n$ for a query.  

Constraints

$1\leq q\leq2\times10^4$  
$1\leq n\leq4\times10^5$  

Output Format

For each query, print the number of $n$-digit numbers satisfying Chloe's rules, modulo $10^9+7$, on a new line.   

Sample Input 0
1
6

Sample Output 0
95

Explanation 0

There are $95$ six-digit numbers satisfying the property above, where the respective first and last ones are $\textbf{101101}$ and $\boldsymbol{902005}$.
