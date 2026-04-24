for _ in range(int(input())):
	N = int(input())
	A = [*map(int, input().split())]
	(op, dp) = ([pow(10, 9)] * (N + 1), [pow(10, 9)] * (N + 1))
	op[A[0]] = dp[0] = 0
	for i in range(1, N):
		if A[i - 1] <= A[i]:
			dp[i] = dp[i - 1]
		dp[i] = min(dp[i], op[A[i]] + 1)
		op[A[i]] = min(op[A[i]], dp[i])
	print(dp[N - 1] if dp[N - 1] <= N else -1)
