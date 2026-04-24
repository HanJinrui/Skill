from collections import defaultdict
(n, m, b) = map(int, input().split())
d = defaultdict(list)
for i in range(n):
	(a, p, v) = map(int, input().split())
	d[a].append((p, v))
alb = list(map(int, input().split()))
dp = [[0 for x in range(b + 1)] for y in range(n + 1)]
s = 1
i = 1
while i <= m:
	j = 0
	sg = 0
	while j < len(d[i]):
		k = b
		ps = d[i][j][0]
		gs = d[i][j][1]
		sg += gs
		while k >= ps:
			dp[s][k] = max(dp[s - 1][k], dp[s - 1][k - ps] + gs)
			k -= 1
		k = 0
		while k < ps:
			dp[s][k] = dp[s - 1][k]
			k += 1
		j += 1
		s += 1
	k = b
	while k >= alb[i - 1]:
		dp[s - 1][k] = max(dp[s - 1 - j][k - alb[i - 1]] + sg, dp[s - 1][k])
		k -= 1
	i += 1
print(dp[n][b])
