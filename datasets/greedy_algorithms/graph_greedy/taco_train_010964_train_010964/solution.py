n = int(input())
g = [[] for _ in range(n)]
s = 0
for _ in range(n - 1):
	(u, v, w) = map(int, input().split())
	u -= 1
	v -= 1
	g[u].append((v, w))
	g[v].append((u, w))
	s += w

def dfs(u, f, x):
	ret = x
	for (v, w) in g[u]:
		if f != v:
			ret = max(ret, dfs(v, u, w + x))
	return ret
print(2 * s - dfs(0, -1, 0))
