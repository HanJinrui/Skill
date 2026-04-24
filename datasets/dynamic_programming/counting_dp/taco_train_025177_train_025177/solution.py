(n, k) = map(int, input().split())
dp = []
for i in range(k + 1):
	dp.append([])
	for j in range(n + 1):
		dp[-1].append(0)
for i in range(1, n + 1):
	dp[1][i] = 1
for m in range(1, k):
	for i in range(1, n + 1):
		for j in range(i, n + 1, i):
			dp[m + 1][j] += dp[m][i]
			dp[m + 1][j] %= 1000000007
print(sum(dp[k]) % 1000000007)
