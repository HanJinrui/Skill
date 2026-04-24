def p2(a):
	n = len(a)
	last = [[0] * 26 for _ in range(n)]
	last[0][ord(a[0]) - 97] = 0
	for i in range(1, n):
		for j in range(26):
			last[i][j] = last[i - 1][j]
		last[i][ord(a[i]) - 97] = i
	dp = [''] * n
	for i in range(n - 1, -1, -1):
		for j in range(n - 1, i, -1):
			k = last[j][ord(a[i]) - 97]
			if k > i:
				if k - i == 1 and len(dp[j]) < 2:
					dp[j] = a[i] + a[i]
				elif len(dp[j]) < len(dp[k - 1]) + 2:
					dp[j] = a[i] + dp[k - 1] + a[i]
					if len(dp[j]) >= 100:
						if len(dp[j]) == 101:
							return dp[j][:50] + dp[j][51:]
						else:
							return dp[j]
		dp[i] = a[i]
	return dp[n - 1]
print(p2(input()))
