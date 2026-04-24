(N, M) = map(int, input().split())
S1 = input()
S2 = input()
ans = 0
dp = [[0 for i in range(M + 1)] for j in range(N + 1)]
for i in range(N):
	for j in range(M):
		v = max(0, max(dp[i + 1][j] - 1, dp[i][j + 1] - 1))
		if S1[i] == S2[j]:
			v = max(v, dp[i][j] + 2)
		ans = max(ans, v)
		dp[i + 1][j + 1] = v
print(ans)
