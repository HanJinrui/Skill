(n, m, c0, d0) = map(int, input().split())
dp = []
for i in range(n + 1):
	dp.append(i // c0 * d0)
for i in range(m):
	(a, b, c, d) = map(int, input().split())
	for j in range(1, a // b + 1):
		for k in range(n, c - 1, -1):
			dp[k] = max(dp[k], dp[k - c] + d)
print(dp[n])
