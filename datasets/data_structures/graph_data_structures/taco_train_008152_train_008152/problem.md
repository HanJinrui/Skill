This is the easy version of the problem. The only difference between the easy and hard versions is that, in the easy one, additionally, there exists a solution with at least 2 employees in every department.

ChefCorp has N employees. Each employee belongs to exactly one of the M departments. Each department is headed by exactly one of the employees belonging to that department.

The management structure of ChefCorp is as follows:
Each employee of a department (including its head) is *in contact* with every other employee of that department.
The head of each department is *in contact* with the heads of all the other departments.

For example, let N = 7, M = 3 and employees 1, \textbf{2}, 3 belong to the first department, employees \textbf{4}, 5 belong to the second department and employees \textbf{6}, 7 belong to the third department (employees in bold represent the heads of the departments). The following pairs of employees are in contact with each other: (1, 2), (1, 3), (2, 3), (4, 5), (6, 7), (2, 4), (4, 6), (2, 6).

However, due to some inexplicable reasons, ChefCorp loses all its data on the departments. Given the total number of employees N and every pair of employees who are *in contact* with each other, can you help recover the number of departments and the employees belonging to each of the departments?

------ Input Format ------ 

- The first line contains a single integer T — the number of test cases. Then the test cases follow.
- The first line of each test case contains a single integer N — the total number of employees in ChefCorp.
- The second line of each test case contains a single integer K — the number of pairs of employees *in contact* with each other.
- K lines follow. The i^{th} of these K lines contain two space-separated integers u_{i} and v_{i}, denoting that employee u_{i} is *in contact* with v_{i}.

------ Output Format ------ 

- For each test case, output the following:
- In the first line output M — the number of departments.
- In the second line, output N space-separated integers D_{1}, D_{2}, \ldots, D_{N} (1 ≤ D_{i} ≤ M) — denoting that the i^{th} employee belongs to the D_{i}^{th} department.
- In the third line, output M space-separated integers H_{1}, H_{2}, \ldots, H_{M} (1 ≤ H_{i} ≤ N, H_{i} \neq H_{j} when i \neq j) — denoting that the H_{i}^{th} employee is the head of the i^{th} department.

If there are multiple answers, output any. It is guaranteed that at least one solution always exists.

------ Constraints ------ 

$1 ≤ T ≤ 1000$
$2 ≤ N ≤ 1000$
$1 ≤ K ≤ \frac{N\cdot(N-1)}{2}$
$1 ≤ u_{i}, v_{i} ≤ N$
$u_{i} \neq v_{i}$ for each $1 ≤ i ≤ K$.
- It is guaranteed that there exists a solution in which there are at least two employees in every department.
- The sum of $N$ over all test cases does not exceed $3000$.

----- Sample Input 1 ------ 
3
7
8
1 2
1 3
2 3
4 5
6 7
2 4
4 6
2 6
2
1
1 2
6
8
6 2
5 4
3 1
5 2
3 6
2 1
6 1
2 3

----- Sample Output 1 ------ 
3
1 1 1 2 2 3 3
2 4 6
1
1 1
1
2
1 1 1 2 2 1
2 5

----- explanation 1 ------ 
Test Case $1$: Explained in the problem statement.
