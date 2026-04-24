(n, t) = map(int, input().split())
dp = [[[[0, 0] for i in range(t + 1)] for j in range(5)] for k in range(n + 1)]
dp[2][2][1][0] = 1
dp[2][3][1][0] = 2
dp[2][4][1][0] = 3
ans = 0
for i in range(3, n + 1):
	for j in range(1, 5):
		for k in range(1, t + 1):
			for l in range(1, j):
				dp[i][j][k][0] += dp[i - 1][l][k][0] + dp[i - 1][l][k - 1][1]
			for l in range(4, j, -1):
				dp[i][j][k][1] += dp[i - 1][l][k][1] + dp[i - 1][l][k][0]
for i in range(1, 5):
	ans += dp[n][i][t][1]
print(ans)
