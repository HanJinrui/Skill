Roy has taken a liking to the Binary Search Trees(BST). He is interested in knowing the number of ways an array $\mbox{A}$ of $N$ integers can be arranged to form a BST. Thus, he tries a few combinations, and notes down the numbers at the odd levels and the numbers at the even levels. 

You're given two values, alpha and beta. Can you calculate the sum of Liking of all possible BST's that can be formed from an array of $N$ integers? Liking of each BST is defined as follows 

(sum of numbers on even levels * alpha) - (sum of numbers on odd levels * beta)

Note 

The root element is at level $0$ ( Even )
The elements smaller or equal to the parent element are present in the left subtree, elements greater than or equal to the parent element are present in the right subtree.  Explained here

If the answer is no less than $10^{9}+9$, output the answer % $10^{9}+9$. 

(If the answer is less than $0$, keep adding $10^{9}+9$ until the value turns non negative.)

Input Format 

The first line of input file contains an integer, $\mathbf{T}$, denoting the number of test cases to follow. 

Each testcase comprises of $3$ lines. 

The first line contains $N$, the number of integers. 

The second line contains two space separated integers, alpha and beta. 

The third line contains space separated $N$ integers_, denoting the $i^{\mbox{th}}$ integer in array $A[i]$.  

Output Format 

Output $\mathbf{T}$ lines. Each line contains the answer to its respective test case. 

Constraints  

$1\leq T\leq10$ 

$1\leq N\leq150$ 

$1\leq A[i]\leq10^9$ 

$1\leq alpha,beta\leq10^9$  

Sample Input

4
1
1 1
1
2
1 1
1 2
3
1 1
1 2 3
5
1 1
1 2 3 4 5

Sample Output

1
0
6
54

Explanation

There are $\begin{array}{c}4\end{array}$ test cases in total. 

For the first test case, only $1$ BST can be formed with 1 as the root node. Hence the Liking / sum is $1$. 

For the second test case, we get 2 BSTs of the form, the Liking of the first tree is $1*1-2*1=-1$ and $2*1-1*1=1$, this sums to $0$, hence the answer. 

1                  2 
 \                /
  2              1

For the third test case, we get $5$ BSTs. The Liking of each of the BST from left  to right are $2,-2,4,2,0$ which sums to $\boldsymbol{6}$ and hence the answer.  

1            2                 3          3      1
 \          / \               /          /        \
  2        1   3             1          2          3
   \                          \        /          /
    3                          2      1          2

Similarly, for the fourth test case, the answer is $54$.
