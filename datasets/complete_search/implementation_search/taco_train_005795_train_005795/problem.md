The weather report of Chefland is *Good* if the number of sunny days in a week is strictly greater than the number of rainy days. 

Given 7 integers A_{1}, A_{2}, A_{3}, A_{4}, A_{5}, A_{6}, A_{7} where A_{i} = 1 denotes that the i^{th} day of week in Chefland is a sunny day, A_{i} = 0 denotes that the i^{th} day in Chefland is a rainy day. Determine if the weather report of Chefland is *Good* or not.

------ Input Format ------ 

- First line will contain T, number of testcases. Then the testcases follow.
- Each testcase contains of a single line of input, 7 space separated integers A_{1}, A_{2}, A_{3}, A_{4}, A_{5}, A_{6}, A_{7}.

------ Output Format ------ 

For each testcase, print "YES" if the weather report of Chefland is Good, otherwise print "NO". Print the output without quotes.

You may print each character of the string in uppercase or lowercase (for example, the strings "yEs", "yes", "Yes" and "YES" will all be treated as identical).

------ Constraints ------ 

$1 ≤ T ≤ 20$
$0 ≤ A_{i} ≤ 1$

----- Sample Input 1 ------ 
4
1 0 1 0 1 1 1
0 1 0 0 0 0 1
1 1 1 1 1 1 1
0 0 0 1 0 0 0

----- Sample Output 1 ------ 
YES
NO
YES
NO
----- explanation 1 ------ 
Test case $1$: The number of sunny days is $5$ and the number of rainy days is $2$. Hence the weather report of Chefland is Good.

Test case $2$: The number of sunny days is $1$ and the number of rainy days is $6$. Hence the weather report of Chefland is not Good.
