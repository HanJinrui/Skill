def max_sum(A, N):
	NS = -sum(A)
	V = ans = sum([i * v for (i, v) in enumerate(A)])
	for i in range(1, N):
		V += NS + N * A[i - 1]
		ans = max(ans, V)
	return ans
