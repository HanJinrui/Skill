INF = 2 ** 29
BUL = 1000
T = int(input())
for t in range(T):
	(n, m) = (int(x) for x in input().split())
	dp = [[INF for x in range(BUL + 1)] for x in range(n)]
	dp1 = [[INF for x in range(BUL + 1)] for x in range(n)]
	dp2 = [[INF for x in range(BUL + 1)] for x in range(n)]
	s = [[int(x) for x in input().split()] for x in range(n)]
	g = [[int(x) for x in input().split()] for x in range(n)]
	for i in range(n):
		if i == 0:
			for j in range(m):
				dp[i][g[i][j]] = min(dp[i][g[i][j]], s[i][j])
		else:
			for j in range(m):
				dp[i][g[i][j]] = min(dp[i][g[i][j]], dp1[i - 1][s[i][j]] + s[i][j], dp2[i - 1][s[i][j]])
		dp1[i][1] = dp[i][1] - 1
		for j in range(2, BUL + 1):
			dp1[i][j] = min(dp1[i][j - 1], dp[i][j] - j)
		dp2[i][BUL] = dp[i][BUL]
		for j in reversed(range(1, BUL)):
			dp2[i][j] = min(dp2[i][j + 1], dp[i][j])
	print(dp2[n - 1][1])
