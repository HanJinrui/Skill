(n, m) = map(int, input().split())
g = {x: [] for x in range(1, n + 1)}
dp = [1] * (n + 1)
ans = 0
for _ in range(m):
	(a, b) = map(int, input().split())
	g[a].append(b)
	g[b].append(a)
for v in range(1, n + 1):
	for u in g[v]:
		if u < v:
			dp[v] = max(dp[v], dp[u] + 1)
	ans = max(ans, dp[v] * len(g[v]))
print(ans)
