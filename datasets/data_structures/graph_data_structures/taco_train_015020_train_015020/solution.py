from collections import defaultdict, deque

class Solution:

	def isPossible(self, n, edges):
		g = defaultdict(lambda : [])
		deg = [0] * n
		for (u, v) in edges:
			g[u].append(v)
			deg[v] += 1
		q = deque([i for i in range(n) if deg[i] == 0])
		c = 0
		while q:
			u = q.popleft()
			c += 1
			for v in g[u]:
				deg[v] -= 1
				if deg[v] == 0:
					q.append(v)
		return c == n
