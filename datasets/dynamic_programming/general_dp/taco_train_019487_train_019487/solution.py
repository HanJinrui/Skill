for t in range(int(input())):
	(n, c) = list(map(int, input().split()))
	g = list(map(int, input().split()))
	dp = [0] * (n + 1)
	dp[0] = 0
	dp[1] = c
	for i in range(2, len(dp)):
		d = {}
		arg = 0
		dp[i] = c + dp[i - 1]
		for j in range(i, 0, -1):
			d[g[j - 1]] = d.get(g[j - 1], 0) + 1
			if d[g[j - 1]] == 2:
				arg += 2
			elif d[g[j - 1]] > 2:
				arg += 1
			dp[i] = min(dp[i], c + arg + dp[j - 1])
	print(dp[n])
