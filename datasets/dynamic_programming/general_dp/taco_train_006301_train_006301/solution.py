n = int(input())
(*a,) = map(int, input().split())
a.append(-1)
b = [a[i] for i in range(n) if a[i] != a[i - 1]]
dp = [[0 for j in range(n + 2)] for i in range(n + 2)]
for l in range(len(b)):
	for i in range(len(b) - l):
		j = i + l
		dp[i][j] = max(dp[i][j - 1], dp[i + 1][j])
		if b[i] == b[j]:
			dp[i][j] = dp[i + 1][j - 1] + 2
print(len(b) - (dp[0][len(b) - 1] + 1) // 2)
