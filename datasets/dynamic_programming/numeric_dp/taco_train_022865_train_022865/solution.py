import sys
(n, K) = map(int, input().split())
a = list(map(int, input().split()))
(m2, m5) = ([0] * n, [0] * n)
for (i, x) in enumerate(a):
	while x % 2 == 0:
		x //= 2
		m2[i] += 1
	while x % 5 == 0:
		x //= 5
		m5[i] += 1
dp = [[-10 ** 9] * 5100 for _ in range(K)]
dp[0][0] = 0
for i in range(n):
	(x, y) = (m5[i], m2[i])
	for j in range(min(K - 1, i) - 1, -1, -1):
		for k in range(5000, -1, -1):
			dp[j + 1][k + x] = max(dp[j + 1][k + x], dp[j][k] + y)
	dp[0][x] = max(dp[0][x], y)
ans = 0
for i in range(5001):
	ans = max(ans, min(i, dp[-1][i]))
print(ans)
