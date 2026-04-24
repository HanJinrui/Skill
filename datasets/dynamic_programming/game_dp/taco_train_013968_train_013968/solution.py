t = int(input())
for _ in range(t):
	(n, m, k) = map(int, input().split())
	mod = int(1000000000.0 + 7)
	dp = [[0] * (n + 1) for i in range(n + 1)]
	for i in range(n + 1):
		dp[i][i] = i * k % mod
	for i in range(1, n + 1):
		for j in range(1, i):
			dp[i][j] = (dp[i - 1][j - 1] + dp[i - 1][j]) * (mod + 1) // 2 % mod
	print(dp[n][m])
