Given a string consisting of the letters $\textbf{a}$, $\textbf{b}$ and $\textbf{c}$, we can perform the following operation: 

Take any two adjacent distinct characters and replace them with the third character. 

Find the shortest string obtainable through applying this operation repeatedly.  

For example, given the string $\textbf{aba}$ we can reduce it to a $\mbox{1}$ character string by replacing $\textbf{ab}$ with $\textbf{c}$ and $\textbf{ca}$ with $\mbox{b}$: $\textbf{aba}\to\textbf{ca}\to\textbf{b}$.  

Function Description  

Complete the stringReduction function in the editor below.  It must return an integer that denotes the length of the shortest string obtainable.  

stringReduction has the following parameter: 

- s: a string  

Input Format

The first line contains the number of test cases $\boldsymbol{\boldsymbol{t}}$.  

Each of the next $\boldsymbol{\boldsymbol{t}}$ lines contains a string $\boldsymbol{\mathrm{~S~}}$ to process.

Constraints

$1\leq t\leq100$
$1<|s|\leq100$

Output Format

For each test case, print the length of the resultant minimal string on a new line.  

Sample Input
3  
cab  
bcab  
ccccc

Sample Output
2  
1  
5

Explanation

For the first case, there are two solutions:  $\textbf{cab}\to\textbf{cc}$ or $\textbf{cab}\to\textbf{bb}$. 

For the second case, one optimal solution is: $\textbf{bcab}\to\textbf{aab}\to\textbf{ac}\to\textbf{b}$. 

For the third case, no operations can be performed so the answer is $5$.
