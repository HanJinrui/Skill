for _ in range(int(input())):
	(n, m) = map(int, input().split())
	arr = []
	for i in range(n):
		arr.append(list(map(int, input().split())))
	dp = [[arr[i][j] for j in range(m)] for i in range(n)]
	for i in range(n - 2, -1, -1):
		dp[i][-1] = max(dp[i][-1], dp[i + 1][-1])
	for i in range(m - 2, -1, -1):
		dp[-1][i] = max(dp[-1][i], dp[-1][i + 1])
	for i in range(n - 2, -1, -1):
		for j in range(m - 2, -1, -1):
			if (i + j) % 2:
				if arr[i + 1][j] > arr[i][j + 1]:
					dp[i][j] = max(dp[i + 1][j], dp[i][j])
				else:
					dp[i][j] = max(dp[i][j + 1], dp[i][j])
			else:
				dp[i][j] = max(min(dp[i + 1][j], dp[i][j + 1]), dp[i][j])
	print(dp[0][0])
