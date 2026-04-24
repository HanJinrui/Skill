dp = [0] * 5010
dp[0] = 1
(n, m, k) = map(int, input().split())
t = 998244353
for i in range(k):
	for j in range(len(dp) - 1, -1, -1):
		if j == 0:
			dp[j] = 0
		else:
			dp[j] = (dp[j - 1] * (n - j + 1) + dp[j] * j) % t
c = 0
for i in range(k + 1):
	c += pow(m, max(n - i, 0), t) * dp[i]
	c %= t
den = pow(m, n, t)
den = pow(den, t - 2, t)
print(den * c % t)
