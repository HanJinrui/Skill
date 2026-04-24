class Solution:

	def isCyclic(self, V, adj):
		visited = {}

		def dfs(node):
			if node in visited:
				return visited[node]
			visited[node] = True
			for nei in adj[node]:
				if dfs(nei):
					return True
			visited[node] = False
			return False
		for i in range(V):
			if dfs(i):
				return True
		return False
