import collections
import sys
sys.setrecursionlimit(10 ** 9)

def dfs(u, ii):
	vis[u] = ii
	for (v, wt) in g[u]:
		if v not in vis:
			x_vals[v] = x_vals[u] ^ wt
			dfs(v, ii)
		elif x_vals[v] != x_vals[u] ^ wt:
			print(-1)
			exit(0)
(n, m, k) = map(int, input().split())
k -= 1
g = collections.defaultdict(list)
for i in range(m):
	(x, y, z) = map(int, input().split())
	g[x].append((y, z))
	g[y].append((x, z))
vis = {}
x_vals = [0 for i in range(n + 1)]
last = ii = 0
for i in range(1, n + 1):
	if i not in vis:
		dfs(i, ii)
		last = i
		ii += 1
for i in range(1, n + 1):
	if vis[i] == vis[last]:
		x_vals[i] ^= k
print(*x_vals[1:])
