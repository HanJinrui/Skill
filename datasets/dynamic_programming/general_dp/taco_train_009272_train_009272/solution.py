T = int(input())
MOD = 1000000007
C = [[0] * 400 for _ in range(400)]
C[0][0] = 1
for i in range(400):
	(C[i][0], C[i][i]) = (1, 1)
	for j in range(1, i):
		C[i][j] = (C[i - 1][j - 1] + C[i - 1][j]) % MOD
for t in range(T):
	(N, M) = [int(c) for c in input().split()]
	X = [int(c) for c in input().split()]
	D = [int(c) for c in input().split()]
	dp = [[[0] * (M + 1) for j in range(D[i])] for i in range(N)]
	for i in range(N):
		for j in range(D[i]):
			dp[i][j][0] = 1
			if j > 0:
				dp[i][j][1] += 1
			if j < D[i] - 1:
				dp[i][j][1] += 1
		for m in range(2, M + 1):
			for j in range(D[i]):
				if j > 0:
					dp[i][j][m] += dp[i][j - 1][m - 1]
				if j < D[i] - 1:
					dp[i][j][m] += dp[i][j + 1][m - 1]
	total = [dp[0][X[0] - 1][m] for m in range(M + 1)]
	for i in range(1, N):
		for j in reversed(range(1, M + 1)):
			total[j] = sum((total[k] * C[j][k] * dp[i][X[i] - 1][j - k] for k in range(j + 1)))
	print(total[M] % MOD)
