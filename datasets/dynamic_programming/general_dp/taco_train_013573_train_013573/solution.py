n = int(input())
a = list(map(int, input().split()))
dp = [[0, 0] for i in range(201)]
for i in range(201):
	dp[i][1] = 1
mod = 998244353
for i in range(1, n + 1):
	dp1 = [[0, 0] for _ in range(201)]
	for j in range(1, 201):
		if a[i - 1] == -1 or a[i - 1] == j:
			dp1[j][0] = (dp1[j][0] + dp[j - 1][1] + dp[j - 1][0]) % mod
			dp1[j][1] = (dp1[j][1] + dp[200][1] - dp[j - 1][1] + dp[j][0] - dp[j - 1][0]) % mod
		dp1[j][0] = (dp1[j][0] + dp1[j - 1][0]) % mod
		dp1[j][1] = (dp1[j][1] + dp1[j - 1][1]) % mod
	dp = dp1
print(dp[200][1])
