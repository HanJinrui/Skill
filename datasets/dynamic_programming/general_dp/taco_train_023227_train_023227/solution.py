t = int(input())
for _ in range(t):
	(N, M, k) = map(int, input().split())
	a = []
	for _ in range(N):
		a.append(input())
	dp = [0] * N
	for i in range(N):
		dp[i] = [0] * M
	dp[0][0] = k - 1
	for i in range(1, N):
		if a[i - 1][0] == '1':
			dp[i][0] = (dp[i - 1][0] + 1) // 2
		else:
			dp[i][0] = dp[i - 1][0] // 2
	for j in range(1, M):
		if a[0][j - 1] == '1':
			dp[0][j] = dp[0][j - 1] // 2
		else:
			dp[0][j] = (dp[0][j - 1] + 1) // 2
	for i in range(1, N - 1):
		for j in range(1, M - 1):
			if a[i - 1][j] == '1':
				dp[i][j] = (dp[i - 1][j] + 1) // 2
			else:
				dp[i][j] = dp[i - 1][j] // 2
			if a[i][j - 1] == '1':
				dp[i][j] += dp[i][j - 1] // 2
			else:
				dp[i][j] += (dp[i][j - 1] + 1) // 2
	j = M - 1
	for i in range(1, N):
		if a[i - 1][j] == '1':
			dp[i - 1][j] = min(dp[i - 1][j], 1)
			dp[i][j] = dp[i - 1][j]
		else:
			dp[i - 1][j] = 0
			dp[i][j] = 0
		if a[i][j - 1] == '1':
			dp[i][j] += dp[i][j - 1] // 2
		else:
			dp[i][j] += (dp[i][j - 1] + 1) // 2
	i = N - 1
	for j in range(1, M):
		if a[i - 1][j] == '1':
			dp[i][j] = (dp[i - 1][j] + 1) // 2
		else:
			dp[i][j] = dp[i - 1][j] // 2
		if a[i][j - 1] == '1':
			dp[i][j - 1] = 0
		else:
			dp[i][j - 1] = min(dp[i][j - 1], 1)
			dp[i][j] += dp[i][j - 1]
	for i in range(N):
		for j in range(M):
			if dp[i][j] & 1:
				dp[i][j] = 1 - int(a[i][j])
			else:
				dp[i][j] = int(a[i][j])
	i = 0
	j = 0
	while i < N and j < M:
		if i == N - 1 and j == M - 1:
			break
		if dp[i][j] == 0:
			if j == M - 1:
				break
			j += 1
		else:
			if i == N - 1:
				break
			i += 1
	print(i + 1, end=' ')
	print(j + 1)
