You are a waiter at a party.  There is a pile of numbered plates.  Create an empty $\textit{answers}$ array.  At each iteration, $\boldsymbol{i}$, remove each plate from the top of the stack in order.  Determine if the number on the plate is evenly divisible by the $i^t h$ prime number.  If it is, stack it in pile $B_i$.  Otherwise, stack it in stack $A_i$.  Store the values in $B_i$ from top to bottom in $\textit{answers}$.  In the next iteration, do the same with the values in stack $A_i$.  Once the required number of iterations is complete, store the remaining values in $A_i$ in $\textit{answers}$, again from top to bottom.  Return the $\textit{answers}$ array.  

Example   

$A=[2,3,4,5,6,7]$ 

$q=3$  

An abbreviated list of primes is $[2,3,5,7,11,13]$.  Stack the plates in reverse order. 

$A_0=[2,3,4,5,6,7]$ 

$\textit{answers}=[]$  

Begin iterations.  On the first iteration, check if items are divisible by $2$. 

$A_1=[7,5,3]$ 

$B_1=[6,4,2]$

Move $\begin{array}{c}B_1\end{array}$ elements to $\textit{answers}$.

$answers=[2,4,6]$  

On the second iteration, test if $\boldsymbol{A_1}$ elements are divisible by $3$. 

$A_2=[7,5]$ 

$B_2=[3]$  

Move $B_2$ elmements to $\textit{answers}$.  

$answers=[2,4,6,3]$  

And on the third iteration, test if $\boldsymbol{A_{2}}$ elements are divisible by $5$. 

$A_{3}=[7]$ 

$B_3=[5]$ 

Move $B_2$ elmements to $\textit{answers}$.  

$answers=[2,4,6,3,5]$  

All iterations are complete, so move the remaining elements in $A_3$, from top to bottom, to $\textit{answers}$.  

$answers=[2,4,6,3,5,7]$.  Return this list.  

Function Description   

Complete the waiter function in the editor below.  

waiter has the following parameters:  

int number[n]: the numbers on the plates  
int q: the number of iterations  

Returns  

int[n]: the numbers on the plates after processing  

Input Format

The first line contains two space separated integers, $n$ and $\textit{q}$. 

The next line contains $n$ space separated integers representing the initial pile of plates, i.e., $\mbox{A}$.  

Constraints  

$1\leq n\leq5\times10^4$ 

$2\leq{number[i]}\leq{10^4}$ 

$1\leq q\leq1200$  

Sample Input 0
5 1
3 4 7 6 5

Sample Output 0
4
6
3
7
5

Explanation 0

Initially:

$\mbox{A}$ = [3, 4, 7, 6, 5]<-TOP

After 1 iteration (divide by 2, the 1st prime number):

$\boldsymbol{A_1}$ = [5, 7, 3]<-TOP

$\begin{array}{c}B_1\end{array}$ = [6, 4]<-TOP

Move $\begin{array}{c}B_1\end{array}$ elements to $\textit{answers}$.  

$answers=[4,6]$  

All iterations are complete, so move $\boldsymbol{A_1}$ elements to $\textit{answers}$.  

$answers=[4,6,3,7,5]$. 

Sample Input 1
5 2
3 3 4 4 9

Sample Output 1
4
4
9
3
3

Explanation 1

Initially:

$\mbox{A}$ = [3, 3, 4, 4, 9]<-TOP

After $1^{st}$ iteration (divide by 2):

$\boldsymbol{A_1}$ = [9, 3, 3]<-TOP  

$\begin{array}{c}B_1\end{array}$ = [4, 4]<-TOP

Move $\begin{array}{c}B_1\end{array}$ to $\textit{answers}$.

$a n s wers=[4,4]$  

After $2^{nd}$ iteration (divide by 3):

$\boldsymbol{A_{2}}$ = []<- TOP

$B_2$ = [3, 3, 9]<-TOP 

Move $B_2$ elements to $\textit{answers}$.  

$answers=[4,4,9,3,3]$  

There are no values remaining in $\boldsymbol{A_{2}}$.
