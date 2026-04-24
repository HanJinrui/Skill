class Solution:

	def findMotherVertex(self, V, adj):
		visited = set()

		def dfs(node):
			if node in visited:
				return
			visited.add(node)
			for child in adj[node]:
				dfs(child)
		dfs(0)
		return 0 if len(visited) == V else -1
