Victoria is splurging on expensive accessories at her favorite stores. Each store stocks $\mbox{A}$ types of accessories, where the $i^{\mbox{th}}$ accessory costs $\boldsymbol{i}$ dollars ($1\leq i\leq A$). Assume that an item's type identifier is the same as its cost, and the store has an unlimited supply of each accessory.

Victoria wants to purchase a total of $L$ accessories according to the following rule:

Any $N$-element subset of the purchased items must contain at least $\mbox{D}$ different types of accessories. 

For example, if $L=6$, $N=3$, and $D=2$, then she must choose $\boldsymbol{6}$ accessories such that any subset of $3$ of the $\boldsymbol{6}$ accessories will contain at least $2$ distinct types of items. 

Given $L$, $\mbox{A}$, $N$, and $\mbox{D}$ values for $\mathbf{T}$ shopping trips, find and print the maximum amount of money that Victoria can spend during each trip; if it's not possible for Victoria to make a purchase during a certain trip, print SAD instead. You must print your answer for each trip on a new line.

Input Format

The first line contains an integer, $\mathbf{T}$, denoting the number of shopping trips. 

Each of the $\mathbf{T}$ subsequent lines describes a single shopping trip as four space-separated integers corresponding to $L$, $\mbox{A}$, $N$, and $\mbox{D}$, respectively.

Constraints

$1\leq T\leq10^6$  
$1\leq D\leq N\leq L\leq10^5$  
$1\leq A\leq10^9$  
The sum of the $L$'s for all $\mathbf{T}$ shopping trips $\leq8\cdot10^{6}$.  

Output Format

For each shopping trip, print a single line containing either the maximum amount of money Victoria can spend; if there is no collection of items satisfying her shopping rule for the trip's $L$, $\mbox{A}$, $N$, and $\mbox{D}$ values, print SAD instead.

Sample Input
2
6 5 3 2
2 1 2 2

Sample Output
24
SAD

Explanation

Shopping Trip 1: 

We know that:

Victoria wants to buy $L=6$ accessories. 
The store stocks the following $A=5$ types of accessories: $\{1,2,3,4,5\}$. 
For any grouping of $N=3$ of her $L$ accessories, there must be at least $D=2$ distinct types of accessories.  

Victoria can satisfy her shopping rule and spend the maximum amount of money by purchasing the following set of accessories: $\{3,4,5,5,4,3\}$. The total cost is $3+4+5+5+4+3=24$, so we print $24$ on a new line.

Shopping Trip 2: 

We know that:

Victoria wants to buy $L=2$ accessories.
The store stocks $A=1$ type of accessory: $\{1\}$. 
For any grouping of $N=2$ of her $L$ accessories, there must be at least $D=2$ distinct types of accessories. 

Because the store only carries $1$ type of accessory, Victoria cannot make a purchase satisfying the constraint that there be at least $D=2$ distinct types of accessories. Because Victoria will not purchase anything, we print that she is SAD on a new line.
