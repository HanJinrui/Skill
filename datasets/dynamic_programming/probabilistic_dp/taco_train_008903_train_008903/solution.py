for _ in range(int(input())):
	(N, C, K) = [int(c) for c in input().split()]
	dp = [[[0 for i in range(C)] for ii in range(N)] for ii in range(K + 1)]
	for i in range(N):
		dp[0][i][1] = 1
	for i in range(1, K + 1):
		(l, r) = [int(c) - 1 for c in input().split()]
		for j in range(N):
			for k in range(C):
				if j >= l and j <= r:
					for m in range(C):
						dp[i][j][m * k % C] += dp[i - 1][j][k] / (2 * C)
					dp[i][j][k] += dp[i - 1][j][k] * 0.5
				else:
					dp[i][j][k] += dp[i - 1][j][k]
	ans = 0
	for i in range(N):
		for j in range(C):
			ans += j * dp[K][i][j]
	print(ans)
