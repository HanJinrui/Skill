Read problems statements in Mandarin Chinese, Russian and Vietnamese as well. 

Chef invited N of his friends in his birthday party. All the friends are numbered from 1 to N. Some of the friends might know each other. You are given this information by M pairs each of form (a_{i}, b_{i}), denoting that the persons a_{i} and b_{i} know each other.

Chef wants all of his guests to seat at the two tables set up for dinner. He wants that all the people  sitting at a table must know each other, otherwise they will feel awkward with mutual eating habits. Chef is okay if a table is not occupied by any person. Chef is worried whether all the guests can seat at the dinner tables in the desired way.

Please help Chef fast to identify whether his worry is real or not!! The delicacies at the table are getting cold.

------ Input ------ 

The first line of the input contains an integer T denoting the number of test cases. The description of T test cases follows.
The first line of each test case contains two space-separated integers N and M, denoting the number of Chef's friends and the number of pairs representing information whether two person know each other or not.
The next M lines contain two space-separated integers a_{i} and b_{i}, denoting that persons a_{i} and b_{i} know each other.

------ Output ------ 

For each test case, output a single line containing word "YES" (without quotes) if Chef can divide all of his friends into two groups that in each group all the people know each other and "NO" (without quotes) otherwise.

------ Constraints ------ 

$1 ≤ T ≤ 10^{3}$
$1 ≤ N ≤ 10^{3}$
$0 ≤ M ≤ 10^{6}$
$1 ≤ a_{i}, b_{i} ≤ N$
$The sum of N over all test cases in a single test file does not exceed 10^{4}$
$The sum of M over all test cases in a single test file does not exceed 10^{6}$

------ Subtasks ------ 

Subtask #1 (30 pts)
$1 ≤ N ≤ 10$
Subtask #2 (70 pts)
$Original constraints$

----- Sample Input 1 ------ 
3
3 2
1 2
2 3
4 3
1 2
2 3
2 4
6 7
1 2
1 3
2 3
2 4
4 5
4 6
5 6
----- Sample Output 1 ------ 
YES
NO
YES
----- explanation 1 ------ 
Example case 1.
Table 1: Person 1. Table 2: Persons 2 and 3.
Example case 2.
All guests can't have a seat according to the rule.
Example case 3.
Table 1: Persons 1, 2, 3. Table 2: Persons 4, 5, 6.
