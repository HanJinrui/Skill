Read problems statements in [Hindi], [Mandarin Chinese], [Russian], [Vietnamese], and [Bengali] as well.

Chef has a memory machine. It has one layer for data storage and another layer for cache. Chef has stored an array with length $N$ in the first layer; let's denote its elements by $A_{0}, A_{1}, \ldots, A_{N-1}$. Now he wants to load some elements of this array into the cache.

The machine loads the array in blocks with size $B$: $A_{0}, A_{1}, \ldots, A_{B-1}$ form a block, $A_{B}, A_{B+1}, \ldots, A_{2B-1}$ form another block, and so on. The last block may contain less than $B$ elements of Chef's array. The cache may only contain at most one block at a time. Whenever Chef tries to access an element $A_{i}$, the machine checks if the block where $A_{i}$ is located is already in the cache, and if it is not, loads this block into the cache layer, so that it can quickly access any data in it. However, as soon as Chef tries to access any element that is outside the block currently loaded in the cache, the block that was previously loaded into the cache is removed from the cache, since the machine loads a new block containing the element that is being accessed.

Chef has a sequence of elements $A_{x_{1}}, A_{x_{2}}, \ldots, A_{x_{M}}$ which he wants to access, in this order. Initially, the cache is empty. Chef is wondering how many times the machine will need to load a block into the cache layer. Can you help him calculate this number?

------  Input ------
The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
The first line of each test case contains three space-separated integers $N$, $B$ and $M$.
The second line contains $M$ space-separated integers $x_{1}, x_{2}, \ldots, x_{M}$.

------  Output ------
For each test case, print a single line containing one integer ― the number of times the machine loads a block into the cache.

------  Constraints ------
$1 ≤ T ≤ 100$
$1 ≤ N, B, M ≤ 5,000$
$0 ≤ x_{i} < N$ for each valid $i$

----- Sample Input 1 ------ 
1

5 3 3

0 3 4
----- Sample Output 1 ------ 
2
----- explanation 1 ------ 
Example case 1: The machine stores elements $[A_{0}, A_{1}, A_{2}]$ in one block and $[A_{3}, A_{4}]$ in another block. When accessing $A_{0}$, the block $[A_{0}, A_{1}, A_{2}]$ is loaded. Then, accessing $A_{3}$ removes the previous block from the cache and loads the block $[A_{3}, A_{4}]$. Finally, when Chef accesses $A_{4}$, a new block is not loaded, since the block containing $A_{4}$ is currently loaded in the cache.
