s = input()
t = input()
(n, m) = (len(s), len(t))
dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
for i in range(n + 1):
	for j in range(n + 1):
		if i == j:
			dp[i][j] = 1
for i in range(n - 1, -1, -1):
	for j in range(i + 1, n + 1):
		if i >= m or t[i] == s[j - i - 1]:
			dp[i][j] += dp[i + 1][j] % 998244353
		if j - 1 >= m or t[j - 1] == s[j - i - 1]:
			dp[i][j] += dp[i][j - 1] % 998244353
total = 0
for i in range(m, n + 1):
	total += dp[0][i] % 998244353
print(total % 998244353)
