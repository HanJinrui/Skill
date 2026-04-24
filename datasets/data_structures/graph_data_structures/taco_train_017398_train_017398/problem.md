Read problems statements in Mandarin Chinese and Russian as well. 

	Mike is given an undirected graph G of N vertices and M edges. A non-negative integer X_{i} is assigned to the i'th vertex of G, for 1 ≤ i ≤ N.

	Mike was asked to assign labels to each edge of the graph so that the following condition is satisfied:

	Let's suppose that the j'th edge of G connects vertices U_{j} and V_{j}. Then, a non-negative integer Y_{j} equals to XU_{j} xor XV_{j}.

	This challenge was too easy for Mike and he solved it quickly.

	The next day, Mike started to worry that he had solved the problem too quickly and had made a lot of mistakes, so he decided to double-check his answers. To his horror, Mike discovered that all the values of X_{i} had been lost!

	Mike is a very meticulous person and he doesn't like making mistakes, so he decided to create his own values of X_{i} that still produce the same values of Y_{j}.

	Your task is to determine whether it is possible to do so. If it is, you should output the K'th lexicographically valid sequence (X_{1}, X_{2}, ..., X_{N}) that satisfies the above conditions, knowing the structure of G and all the values Y_{j}.

------ Note ------ 

	Maybe some of you aren't familiar with some terms in the statement. Here are some articles that could help you understand the problem correctly:

XOR operation: http://en.wikipedia.org/wiki/Exclusive_{or}

	Also, the stack memory size is quite limited on CodeChef, so a deep recursion may lead to the Runtime Error verdict.

------ Input ------ 

	The first line of the input contains the integers N, M and K.

	The next M lines describe the edges of G; the j'th line contains three integers U_{j}, V_{j} and Y_{j}.

	It's guaranteed that G doesn't contain multiple edges and loops.

------ Output ------ 

	If there is no valid labelling, or less than K valid labellings, the only line of the output should contain -1. Otherwise, the only line of the output should contain N non-negative integers, denoting the K'th lexicographically valid sequence (X_{1}, X_{2}, ..., X_{N}).

	It's guaranteed that in the correct sequence all of the values of X_{i} won't exceed the 32-bit signed integer limit.

------ Constraints ------ 

1 ≤ N ≤ 200,000(2 × 10^{5});
0 ≤ M ≤ 300,000(3 × 10^{5});
1 ≤ K ≤ 1,000,000,000(10^{9});
1 ≤ U_{j} ≠ V_{j} ≤ N;
0 ≤ Y_{j} < 2^{31}.

------ Example ------ 

Input:
5 4 2
1 2 5
1 3 9
2 4 0
2 5 1

Output:
1 4 8 4 5 

------ Explanation ------ 

	The first lexicographically valid sequence is equal to (0, 5, 9, 5, 4);

	The second lexicographically valid sequence is equal to (1, 4, 8, 4, 5) - that's the one that should be printed out as the answer.
