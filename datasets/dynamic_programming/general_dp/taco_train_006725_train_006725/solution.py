n = int(input())
A = list(map(int, input().split()))
dp = [[0] * n for i in range(n)]
for i in range(n):
	dp[0][i] = A[i]
for i in range(1, n):
	for j in range(n - i):
		dp[i][j] = dp[i - 1][j] ^ dp[i - 1][j + 1]
for i in range(1, n):
	for j in range(n - i):
		dp[i][j] = max(dp[i][j], dp[i - 1][j], dp[i - 1][j + 1])
q = int(input())
for i in range(q):
	(l, r) = map(int, input().split())
	(l, r) = (l - 1, r - 1)
	print(dp[r - l][l])
