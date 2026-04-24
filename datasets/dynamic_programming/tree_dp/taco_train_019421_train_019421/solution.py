import sys
input = sys.stdin.readline
n = int(input())
A = list(map(int, input().split()))
A = [-1 if a == 0 else 1 for a in A]
g = [[] for i in range(n)]
for i in range(n - 1):
	(u, v) = map(int, input().split())
	(u, v) = (u - 1, v - 1)
	g[u].append(v)
	g[v].append(u)
s = []
s.append(0)
parent = [-1] * n
order = []
while s:
	v = s.pop()
	order.append(v)
	for u in g[v]:
		if parent[v] == u:
			continue
		parent[u] = v
		s.append(u)
order.reverse()
dp = [0] * n
for v in order:
	dp[v] += A[v]
	u = parent[v]
	if u == -1:
		continue
	dp[u] += max(0, dp[v])
ans = [0] * n
order.reverse()
for v in order:
	ans[v] = dp[v]
	for u in g[v]:
		if parent[v] == u:
			continue
		dp[u] += max(0, ans[v] - max(0, dp[u]))
print(*ans)
