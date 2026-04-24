from collections import deque

class Solution:

	def isBipartite(self, V, adj):
		color = [-1] * V

		def dfs(starNode, colorNow):
			color[starNode] = colorNow
			for nei in adj[starNode]:
				if color[nei] == -1:
					color[nei] = not colorNow
					if not dfs(nei, not colorNow):
						return False
				elif color[nei] == colorNow:
					return False
			return True
		for i in range(V):
			if color[i] == -1:
				if not dfs(i, 0):
					return False
		return True
