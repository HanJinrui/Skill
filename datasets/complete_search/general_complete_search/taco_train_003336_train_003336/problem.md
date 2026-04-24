In a class of N students, a class test was held. The i^{th} student scored A_{i} marks. It is also known that the scores of all students were distinct.

A student passes the test if their score is strictly greater than the passing mark. 
Given that exactly X students pass in the test, find the maximum value of the passing mark of the test.

------ Input Format ------ 

- The first line of input will contain a single integer T, denoting the number of test cases.
- Each test case consists of multiple lines of input.
- The first line of each test case contains two space-separated integers N and X — the number of students in the class and the number of students that passed in the test.
- The next line contains N space-separated integers A_{1}, A_{2}, \ldots, A_{N}, where the i^{th} integer denotes the marks of the i^{th} student.

------ Output Format ------ 

For each test case, output on a new line, the maximum value of the passing mark of the test.

------ Constraints ------ 

$1 ≤ T ≤ 100$
$1 ≤ N ≤ 100$
$1 ≤ X ≤ N$
$1 ≤ A_{i} ≤ 100$
- All elements of array $A$ are distinct.

----- Sample Input 1 ------ 
3
2 2
5 1
4 1
5 1 7 4
4 3
15 70 100 31

----- Sample Output 1 ------ 
0
6
30

----- explanation 1 ------ 
Test case $1$: Since both students pass the test, both students scored greater than passing marks. The maximum value of passing marks can be $0$, as both students have marks greater than $0$.

Test case $2$: Only one student passes the test. Thus, the third student has passed the test by scoring $7$ marks. The passing marks of the test is $6$.

Test case $3$: Since three students pass the test, students $2, 3,$ and $4$ scored greater than passing marks. The maximum value of passing marks can be $30$, three students have marks greater than $30$.
