Chef is taking a tough examination. The question paper consists of N objective problems and each problem has 4 options A, B, C, and D, out of which, exactly one option is correct.

Since Chef did not study for the exam, he does not know the answer to any of the problems. Chef was looking nearby for help when his friend somehow communicated the following information:

Exactly N_{A} problems have option A as the answer.
Exactly N_{B} problems have option B as the answer.
Exactly N_{C} problems have option C as the answer.
Exactly N_{D} problems have option D as the answer.

Note that:
N_{A} + N_{B} + N_{C} + N_{D} = N.
Each problem is worth exactly 1 mark and there is no negative marking.
Even though Chef knows the number of correct options of each type, he does not know the correct answer to any problem. 

Based on the given information, find the maximum marks Chef can guarantee if he marks the answers optimally.

------ Input Format ------ 

- First line will contain T, number of test cases. Then the test cases follow.
- First line of each test case contains an integer N denoting the number of problems.
- Second line of each test case contains 4 integers N_{A}, N_{B}, N_{C}, and N_{D} - as mentioned in the problem statement.

------ Output Format ------ 

For each test case, output the maximum marks Chef can guarantee if he marks the answers optimally.

------ Constraints ------ 

$1 ≤ T ≤ 1000$
$1 ≤ N ≤ 10^{5}$
$0 ≤ N_{A}, N_{B}, N_{C}, N_{D} ≤ N$
$N_{A} + N_{B} + N_{C} + N_{D} = N$

----- Sample Input 1 ------ 
2
5
0 0 5 0
10
7 1 1 1

----- Sample Output 1 ------ 
5
7

----- explanation 1 ------ 
Test Case $1$: Chef knows that all the problems have answer as option $C$ and thus he will mark all the answers as $C$ and get $5$ marks.

Test Case $2$: It will be optimal for Chef to mark all the options as $A$ which will yield him $7$ marks. Thus, irrespective of the answer key, Chef can guarantee $7$ marks by marking all answers as option $A$.
