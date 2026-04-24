def DIFF_solu():
	max_ans = 0
	(n, m) = map(int, input().split())
	sum_i = []
	A = []
	for i in range(n):
		A.append(list(map(int, input().split())))
		sum_i.append(sum(A[-1]))
	for j in range(m):
		max_diff_1 = 0
		max_diff_2 = 0
		for i in range(n):
			diff = sum_i[i] - A[i][j] - A[i][j] * (m - 1)
			max_diff_1 += max(0, diff)
			max_diff_2 += max(0, -diff)
		max_ans = max(max_ans, max_diff_1, max_diff_2)
	return max_ans
t = int(input())
for _ in range(t):
	print(DIFF_solu())
