from collections import deque

class Solution:

	def minColour(self, N, M, mat):
		g = [[] for _ in range(N)]
		for i in mat:
			g[i[1] - 1].append(i[0] - 1)
		h = [-1] * N

		def dfs(x):
			if h[x] != -1:
				return h[x]
			c = 0
			for y in g[x]:
				c = max(c, dfs(y))
			h[x] = c + 1
			return h[x]
		for i in range(N):
			dfs(i)
		return max(h)
