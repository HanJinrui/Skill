There is an integer array $\boldsymbol{d}$ which does not contain more than two elements of the same value. How many distinct ascending triples ($d[i]<d[j]<d[k],i<j<k$) are present? 

Input format 

The first line contains an integer, $N$, denoting the number of elements in the array. This is followed by a single line, containing $N$ space-separated integers. Please note that there are no leading spaces before the first number, and there are no trailing spaces after the last number.

Output format: 

A single integer that denotes the number of distinct ascending triplets present in the array.

Constraints: 

$N\leq10^5$ 

Every element of the array is present at most twice. 

Every element of the array is a 32-bit non-negative integer.

Sample input:  

6  
1 1 2 2 3 4  

Sample output:  

4

Explanation 

The distinct triplets are 

(1,2,3) 

(1,2,4) 

(1,3,4) 

(2,3,4)

The elements of the array might not be sorted. Make no assumptions of the same.
