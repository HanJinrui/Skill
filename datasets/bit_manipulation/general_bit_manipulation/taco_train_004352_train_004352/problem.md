An array, $\mbox{A}$, is defined as follows: 

$A_0=0$
$A_x=A_{x-1}\oplus x$ for $x>0$, where $\oplus$ is the symbol for XOR

You will be given a left and right index $\mbox{l r}$.  You must determine the XOR sum of the segment of $\mbox{A}$ as $A[l]\oplus A[l+1]\oplus ...\oplus A[r-1]\oplus A[r]$. 

For example, $A=[0,1,3,0,4,1,7,0,8]$.  The segment from $l=1$ to $r=4$ sums to $1\oplus3\oplus0\oplus4=6$. 

Print the answer to each question.

Function Description  

Complete the xorSequence function in the editor below.  It should return the integer value calculated.  

xorSequence has the following parameter(s):  

l: the lower index of the range to sum  
r: the higher index of the range to sum  

Input Format

The first line contains an integer $\textit{q}$, the number of questions. 

Each of the next $\textit{q}$ lines contains two space-separated integers, $l\left[i\right]$ and $r[i]$, the inclusive left and right indexes of the segment to query.

Constraints

$1\leq q\leq10^5$ 

 $1\leq l[i]\leq r[i]\leq10^{15}$  

Output Format

On a new line for each test case, print the XOR-Sum of $\mbox{A}$'s elements in the inclusive range between indices $l\left[i\right]$ and $r[i]$.

Sample Input 0
3
2 4
2 8
5 9

Sample Output 0
7
9
15

Explanation 0

The beginning of our array looks like this:
 $A=[0,1,3,0,4,1,7,0,8,1,11,...]$

Test Case 0: 

$3\oplus0\oplus4=7$

Test Case 1: 

$3\oplus0\oplus4\oplus1\oplus7\oplus0\oplus8=9$

Test Case 2: 

$1\oplus7\oplus0\oplus8\oplus1=15$

Sample Input 1
3
3 5
4 6
15 20

Sample Output 1
5
2
22

Explanation 1

$A=[0,1,3,0,4,1,7,0,8,1,11,0,12,1,15,0,16,1,19,0,20,1,23,0,24,1,...]$.  Perform the xor sum on each interval: 

$3-5:0\oplus4\oplus1=5$ 

$4-6:4\oplus1\oplus7=2$ 

$15-20:0\oplus16\oplus1\oplus19\oplus0\oplus20=22$
