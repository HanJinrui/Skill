This question is designed to help you get a better understanding of basic heap operations.  

There are $3$ types of query:

"$1$ $\boldsymbol{\nu}$"  - Add an element $\boldsymbol{\nu}$ to the heap.  
"$2$ $\boldsymbol{\nu}$"  - Delete the element $\boldsymbol{\nu}$ from the heap.  
"$3$" - Print the minimum of all the elements in the heap.

NOTE: It is guaranteed that the element to be deleted will be there in the heap. Also, at any instant, only distinct elements will be in the heap.

Input Format

The first line contains the number of queries, $Q$. 

Each of the next $Q$ lines contains one of the $3$ types of query.   

Constraints 

$1\leq Q\leq10^5$ 

$-10^9\leq v\leq10^9$

Output Format

For each query of type $3$, print the minimum value on a single line.  

Sample Input
STDIN       Function
-----       --------
5           Q = 5
1 4         insert 4
1 9         insert 9
3           print minimum
2 4         delete 4
3           print minimum

Sample Output
4  
9 

Explanation

After the first $2$ queries, the heap contains {$4,9$}. Printing the minimum gives $\begin{array}{c}4\end{array}$ as the output. Then, the $4^{th}$ query deletes $\begin{array}{c}4\end{array}$ from the heap, and the $5^{th}$ query gives $\mbox{9}$ as the output.
