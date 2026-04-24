Chef has an array of N numbers and a magic function which can swap two array values if their distance is strictly greater than K units. Since his friend Pishty is obsessed with sorted array, Chef wants to make the lexicographically minimum array possible by using this magic function. He can use this magic function any number of times. Help him find the solution.

Distance: absolute difference of indices
Lexicographically minimum: Given two arrays P_{1},P_{2}….P_{r} and Q_{1},Q_{2}….Q_{r} of same length the first one is smaller than the second one for the lexicographical order, if P_{i}  < Q_{i} for the first i where P_{i} and Q_{i} differ. 

------ Input ------ 

First line of input contains two space separated integers N and K
Next line contains N space separated integers A_{1}, A_{2}, ..., A_{N} denoting chef's array.

------ Output ------ 

The only line of output contains N space separated integers denoting the lexicographically minimum array possible after all such possible swap operations.

------ Constraints ------ 

$1 ≤ N,K ≤ 10^{5}$
$1 ≤ A_{i} ≤ 10^{9}$
 
----- Sample Input 1 ------ 
6 2
4 6 3 2 5 1
----- Sample Output 1 ------ 
1 2 3 4 5 6
----- explanation 1 ------ 
In the first operation, Chef can use his magic function to swap 2 and 4 since their distance = 3 (greater than 2). New array formed: 2 6 3 4 5 1Similarly, he can now swap 2 and 1 to obtain: 1 6 3 4 5 2Finally he can swap 2 and 6 to obain: 1 2 3 4 5 6.This is the lexicographically minimum array possible.
