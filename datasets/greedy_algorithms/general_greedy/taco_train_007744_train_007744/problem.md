Priyanka works for an international toy company that ships by container.  Her task is to the determine the lowest cost way to combine her orders for shipping.  She has a list of item weights.  The shipping company has a requirement that all items loaded in a container must weigh less than or equal to 4 units plus the weight of the minimum weight item.  All items meeting that requirement will be shipped in one container.

What is the smallest number of containers that can be contracted to ship the items based on the given list of weights?

For example, there are items with weights $w=[1,2,3,4,5,10,11,12,13]$.  This can be broken into two containers: $[1,2,3,4,5]$ and $[10,11,12,13]$.  Each container will contain items weighing within $\begin{array}{c}4\end{array}$ units of the minimum weight item.  

Function Description  

Complete the toys function in the editor below.  It should return the minimum number of containers required to ship.  

toys has the following parameter(s):  

w: an array of integers that represent the weights of each order to ship  

Input Format

The first line contains an integer $n$, the number of orders to ship. 

The next line contains $n$ space-separated integers, $w[1],w[2],\ldots,w[n]$,  representing the orders in a weight array.

Constraints

$1\leq n\leq10^5$ 

$0\leq w[i]\leq10^4,where\ i\in[1,n]$   

Output Format

Return the integer value of the number of containers Priyanka must contract to ship all of the toys. 

Sample Input
8
1 2 3 21 7 12 14 21

Sample Output
4

Explanation

The first container holds items weighing $\mbox{I}$, $2$ and $3$. (weights in range $1\ldots5$) 

The second container holds the items weighing $21$ units. ($21\ldots25$) 

The third container holds the item weighing $7$ units.  ($7...11$) 

The fourth container holds the items weighing $12$ and $\mathbf{14}$ units. ($12...14$)  

$\begin{array}{c}4\end{array}$ containers are required.
