Bitoholic is an inhabitant of the planet Neo in a galaxy far far away. Their civilization is studies an advanced form of mathematics. However, rules of calculus are a bit different there. On his planet, integration and differentiation techniques are called alpha and beta operations respectively and are defined as:

alpha: after applying this operation on an polynomial, the degree is incremented by some integral value R and this operation can only be allowed if the degree of the polynomial does not exceed an upper limit U. 

beta: after applying this operation on the polynomial, the degree is decremented by some integral value S and this operation can only be allowed if the degree of the polynomial does not go below the lower limit 0.

You are given  the degree P of an arbitrary polynomial in input, but not the polynomial itself. You have to perform some sequence of alpha and beta operations on it subject to following conditions:
If the degree of the polynomial after applying the alpha operation is exceeding the limit "U", then you will not be able to apply this operation.   
Similarly, if the degree of the polynomial after applying the beta operation is going below 0, then you will not be able to apply this operation.   
If at any stage only one operation (alpha or beta) is possible, it has to be applied.   
You will stop if none of the operations are possible to perform.

You need  to perform a total of  N such operations on the polynomial, although the alpha and beta operations can be performed in any order such that the degree of the polynomial is maximized after N such operations. You will halt the operations only in one of these two cases: 
If you are not able to perform any of the two operations alpha or beta
If you have completed  a total of N operations.

In output you have to find out the maximum degree of the polynomial after applying the N operations.
Input Format :
The first line of the input gives the number of test cases, T.  T test cases follow. Each test case consists of one line with five integers, N, P, U, R and S, where the N is the total number of operations allowed, P is the degree of the polynomial,  U is the upper limit on the degree of the polynomial, R is the increment steps after applying alpha operation and S is the decrement steps after applying beta operations.
Output Format:
For each test case, output one line containing "Case #x:", where x is the test case number (starting from 1). Then, for every test case, in order, output the maximum degree possible when the process halts.
Constraints:
0 < T ≤ 10

0 < N <10^8

0 < P, U, R, S <10^9

SAMPLE INPUT
2 
1 6 10 11 5 
2 2 4 2 1

SAMPLE OUTPUT
Case #1: 1
Case #2: 3

Explanation

For the first test-case:

N=1, P=6, U=10 , R=11 , S=5

degree of the initial polynomial is 6 and Upper limit on the  polynomial  is U=10. A total of N=1 operation needs to be performed such that the degree is maximized.
one possible solution is : 

operation 1: we cannot apply alpha operation as the new degree will be 17 that will exceed the upper limit, so we apply the beta operation and the new  degree of polynomial will be 6-5=1, which is the required answer.

For the second test-case:

N=2, P=2, U=4 , R=2 , S=1

degree of the initial polynomial is 2 and Upper limit on the  polynomial is U=4. A total of N=2 operations need to be performed such that the degree is maximized.
one possible order is : 

operation 1: apply alpha operation, degree of polynomial increased by 2, so  it becomes 4 , 
operation 2: now degree is 4 and we cannot apply alpha operation so we have to apply beta operation which gives degree of 4-1=3.

hence after the two operations the degree is 3.
