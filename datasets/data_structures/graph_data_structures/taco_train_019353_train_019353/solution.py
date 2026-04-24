from sys import setrecursionlimit
setrecursionlimit(10 ** 9)

def dfs(u):
	if vis[u]:
		return
	vis[u] = True
	p.append(u + 1)
	for v in g[u]:
		dfs(v)
for _ in range(int(input())):
	(n, m) = map(int, input().split())
	a = list(map(int, input().split()))
	b = list(map(int, input().split()))
	c = [a[i] // b[i] for i in range(n)]
	g = [[] for _ in range(n)]
	for _ in range(m):
		(u, v) = map(int, input().split())
		u -= 1
		v -= 1
		g[u].append(v)
		g[v].append(u)
	p = []
	maxi = max(c)
	vis = [False] * n
	for i in range(n):
		if c[i] != maxi:
			vis[i] = True
	ans = []
	for u in range(n):
		if not vis[u]:
			dfs(u)
			if len(p) > len(ans):
				ans = p
			p = []
	print(len(ans))
	print(*ans)
