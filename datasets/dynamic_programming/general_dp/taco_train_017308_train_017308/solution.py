n = int(input())
w = [[] for i in range(n + 1)]
sz = [0] * (n + 1)
f = [[0] * (n + 1) for i in range(n + 1)]

def dfs(u, p):
	f[u][1] = sz[u] = 1
	for v in w[u]:
		if v != p:
			dfs(v, u)
			for j in range(sz[u], -1, -1):
				for k in range(sz[v], -1, -1):
					f[u][j + k] = max(f[u][j + k], f[u][j] * f[v][k])
			sz[u] += sz[v]
	for i in range(1, sz[u] + 1):
		f[u][0] = max(f[u][0], f[u][i] * i)
for i in range(n - 1):
	(x, y) = map(int, input().split())
	w[x] += [y]
	w[y] += [x]
dfs(1, 0)
print(f[1][0])
