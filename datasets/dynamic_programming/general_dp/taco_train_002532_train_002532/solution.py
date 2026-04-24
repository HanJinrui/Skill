def solve(s, n):
	dp = [[0] * n for _ in range(n)]
	for i in range(n - 1, -1, -1):
		dp[i][i] = 1
		for j in range(i + 1, n):
			if s[i] == s[j]:
				dp[i][j] = dp[i + 1][j - 1] + 2
			else:
				dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
	return dp[0][n - 1] // 2
t = int(input())
for _ in range(t):
	n = int(input())
	s = input()
	result = solve(s, n)
	print(result)
