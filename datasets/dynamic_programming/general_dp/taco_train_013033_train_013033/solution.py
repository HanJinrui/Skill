dp = [[0 for it in range(1003)] for it in range(1003)]
dp[0][0] = 1
mod = 10 ** 9 + 7
for i in range(1, 1003):
	dp[i][0] = dp[i - 1][i - 1]
	for j in range(1, i + 1):
		dp[i][j] = (dp[i - 1][j - 1] % mod + dp[i][j - 1] % mod) % mod
for it in range(int(input())):
	n = int(input())
	print(dp[n][0])
