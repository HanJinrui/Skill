class Solution:

	def findMaxFlow(self, N, M, Edges):
		g = [[0] * N for i in range(N)]
		for (i, j, k) in Edges:
			g[i - 1][j - 1] += k
			g[j - 1][i - 1] += k

		def bfs(s, t, parent):
			queue = [(s, float('inf'))]
			while queue:
				(curr, flow) = queue.pop(0)
				for (k, v) in enumerate(g[curr]):
					if parent[k] is None and v > 0:
						parent[k] = curr
						val = min(flow, v)
						if k == t:
							return val
						queue.append((k, val))
			return 0

		def helper(s, t):
			path = 0
			while True:
				parent = [None] * N
				parent[s] = -1
				val = bfs(s, t, parent)
				if val == 0:
					break
				path += val
				curr = t
				while curr != s:
					prev = parent[curr]
					g[prev][curr] -= val
					g[curr][prev] -= val
					curr = prev
			return path
		return helper(0, N - 1)
