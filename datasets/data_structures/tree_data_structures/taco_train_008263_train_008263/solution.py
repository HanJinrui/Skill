from collections import defaultdict
for _ in range(int(input())):
	n = int(input())
	g = defaultdict(list)
	for _ in range(n - 1):
		(u, v, w) = map(int, input().split())
		g[u].append((v, w))
		g[v].append((u, w))
	d = [0] * (n + 1)

	def dfs(x, p):
		for (y, k) in g[x]:
			if y != p:
				d[y] = k ^ d[x]
				dfs(y, x)
	dfs(1, 0)
	fa = False
	grp = defaultdict(list)
	for i in range(1, n + 1):
		for j in range(i + 1, n + 1):
			x = d[i] ^ d[j]
			grp[x].append((i, j))
			if len(grp[x]) > 1:
				fa = True
				res = [grp[x][0], grp[x][1]]
				break
		if fa:
			break
	if fa:
		print(*res[0], *res[1])
	else:
		print(-1)
