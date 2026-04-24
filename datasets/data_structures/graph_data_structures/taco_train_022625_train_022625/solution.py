import sys
sys.setrecursionlimit(10 ** 6)

class Solution:

	def dfs(self, i, p, vis, graph, dis, low, l, ap):
		vis[i] = 1
		dis[i] = low[i] = l[0]
		l[0] += 1
		c = 0
		for j in graph[i]:
			if j == p:
				continue
			if vis[j] == 0:
				self.dfs(j, i, vis, graph, dis, low, l, ap)
				low[i] = min(low[i], low[j])
				if low[j] >= dis[i] and p != -1:
					ap.add(i)
				c += 1
			else:
				low[i] = min(low[i], dis[j])
		if c > 1 and p == -1:
			ap.add(i)

	def doctorStrange(self, n, k, g):
		adj = []
		for i in range(n):
			adj.append([])
		for i in g:
			adj[i[0] - 1].append(i[1] - 1)
			adj[i[1] - 1].append(i[0] - 1)
		l = [0]
		low = [-1] * n
		dis = [-1] * n
		vis = [0] * n
		ap = set()
		self.dfs(0, -1, vis, adj, dis, low, l, ap)
		ap = list(ap)
		ap.sort()
		return len(ap)
