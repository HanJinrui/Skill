from collections import Counter
(n, m, c) = map(int, input().split())
up = Counter(list(map(int, input().split())))
down = Counter(list(map(int, input().split())))
dp = [[0 for _ in range(c + 1)] for _ in range(c + 1)]
for i in range(1, c + 1):
	dp[0][i] = (dp[0][i - 1] + up.get(i, 0) * down.get(i, 0)) % (10 ** 9 + 7)
for i in range(1, c + 1):
	for j in range(1, c + 1):
		dp[i][j] = (dp[i][j - 1] + up.get(j, 0) * down.get(j, 0) * dp[i - 1][j - 1]) % (10 ** 9 + 7)
for i in range(1, c + 1):
	print(dp[i][c], end=' ', sep='')
print()
