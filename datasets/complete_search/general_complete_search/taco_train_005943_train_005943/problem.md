Victor is building a Japanese rock garden in his $24\times24$ square courtyard. He overlaid the courtyard with a Cartesian coordinate system so that any point $(x,y)$ in the courtyard has coordinates $x\in[-12,12]$ and $y\in[-12,12]$. Victor wants to place $12$ stones in the garden according to the following rules:

The center of each stone is located at some point $(x,y)$, where $\boldsymbol{x}$ and $y$ are integers $\in[-12,12]$. 
The coordinates of all twelve stones are pairwise distinct. 
The Euclidean distance from the center of any stone to the origin is not an integer. 
The sum of Euclidean distances between all twelve points and the origin is an almost integer, meaning the absolute difference between this sum and an integer must be $\leq10^{-12}$.

Given the values of $\boldsymbol{x}$ and $y$ for the first stone Victor placed in the garden, place the remaining $\mbox{11}$ stones according to the requirements above. For each stone you place, print two space-separated integers on a new line describing the respective $\boldsymbol{x}$ and $y$ coordinates of the stone's location.

Input Format

Two space-separated integers describing the respective values of $\boldsymbol{x}$ and $y$ for the first stone's location.

Constraints

$-12\leq x,y\leq12$

Output Format

Print $\mbox{11}$ lines, where each line contains two space-separated integers describing the respective values of $\boldsymbol{x}$ and $y$ for a stone's location.

Sample Input 0
7 11

Sample Output 0
11 1
-2 12
5 4
12 -3
10 3
9 6
-12 -7
1 11
-6 -6
12 -4
4 12

Explanation 0

The diagram below depicts the placement of each stone and maps its distance to the origin (note that red denotes the first stone placed by Victor and blue denotes the eleven remaining stones we placed):

Now, let's determine if the sum of these distances is an almost integer. First, we find the distance from the origin to the stone Victor placed at $(7,11)$, which is $\sqrt{7^2+11^2}\approx13.038404810405297429165943114858$. Next, we calculate the distances for the remaining stones we placed in the graph above:

$\sqrt{11^2+1^2}\approx11.045361017187260774210913843344$
$\sqrt{(-2)^2+12^2}\approx12.165525060596439377999368490404\text{}$
$\sqrt{5^2+4^2}\approx6.4031242374328486864882176746218$
$\sqrt{12^2+(-3)^2}\approx12.36931687652981649464229567922$
$\sqrt{10^2+3^2}\approx10.44060650891055017975754022548\text{}$
$\sqrt{9^2+6^2}\approx10.816653826391967879357663802411$
$\sqrt{(-12)^2+(-7)^2}\approx13.89243989449804508432547041029\text{}$
$\sqrt{1^2+11^2}\approx11.045361017187260774210913843344$
$\sqrt{(-6)^2+(-6)^2}\approx8.4852813742385702928101323452582$
$\sqrt{12^2+(-4)^2}\approx12.649110640673517327995574177731$
$\sqrt{4^2+12^2}\approx12.64911064067351737995574177731$

When we sum these eleven distances with the distance for the stone Victor placed, we get $\approx135.000000000000016207888321012$. The nearest integer to this number is $135$, and the distance between this sum and the nearest integer is $\approx1.6\times10^{-14}\leq10^{-12}$ (meaning it's an almost integer). Because this configuration satisfies all of Victor's rules for his rock garden, we print eleven lines of x y coordinates describing the locations of the stones we placed.
