(n, k) = map(int, input().split())
dp = [1] * (n + 1)
mod = 10 ** 9 + 7
for i in range(k - 1):
	for j in range(1, n + 1):
		for t in range(2 * j, n + 1, j):
			dp[j] += dp[t]
print(sum(dp[1:]) % mod)
