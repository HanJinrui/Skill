You will be given a list of 32 bit unsigned integers. Flip all the bits ($1\rightarrow0$ and $\textbf{0}\rightarrow1$) and return the result as an unsigned integer.  

Example 

$n=9_{10}$   

$\textbf{9}_{10}=1\textbf{001}_{2}$.  We're working with 32 bits, so:  

$00000000000000000000000000001001_2=9_{10}$ 

$11111111111111111111111111110110_2=4294967286_{10}$  

Return $4294967286$.

Function Description

Complete the flippingBits function in the editor below.  

flippingBits has the following parameter(s):

int n: an integer   

Returns   

int: the unsigned decimal integer result

Input Format

The first line of the input contains $\textit{q}$, the number of queries. 

Each of the next $\textit{q}$ lines contain an integer, $n$, to process.  

Constraints

$1\leq q\leq100$ 

$0\leq n<2^{32}$

Sample Input 0
3
2147483647
1
0

Sample Output 0
2147483648
4294967294
4294967295

Explanation 0

$01111111111111111111111111111111_{2}=2147483647_{10}$ 

$10000000000000000000000000000000_2=2147483648_{10}$  

$00000000000000000000000000000001_2=1_{10}$ 

$11111111111111111111111111111110_2=4294967294_{10}$  

$00000000000000000000000000000000_{2}=0_{10}$ 

$11111111111111111111111111111111_2=4294967295_{10}$  

Sample Input 1
2
4
123456

Sample Output 1
4294967291
4294843839

Explanation 1

$00000000000000000000000000000100_{2}=4_{10}$ 

$11111111111111111111111111111011_2=4294967291_{10}$  

$000000000000000111001001000000_2=123456_{10}$ 

$11111111111111100001110110111111_{2}=4294843839_{10}$  

Sample Input 2
3
0
802743475
35601423

Sample Output 2
4294967295
3492223820
4259365872

Explanation 2

$00000000000000000000000000000000_{2}=0_{10}$ 

$11111111111111111111111111111111_2=4294967295_{10}$  

$00101111110110001110010010110011_2=802743475_{10}$ 

$11010000001001110001101101001100_2=3492223820_{10}$  

$00000010000111110011110000001111_2=35601423_{10}$ 

$11111101111000001100001111110000_2=425965872_{10}$
