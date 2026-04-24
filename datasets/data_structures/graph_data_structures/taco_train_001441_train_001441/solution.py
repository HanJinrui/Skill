class Solution:

	def numProvinces(self, adj, V):

		def dfs(adj, i):
			adj[i][i] = 0
			for j in range(len(adj)):
				if adj[i][j] == 1:
					adj[i][j] = 0
					if adj[j][j] == 1:
						dfs(adj, j)
		ans = 0
		for i in range(V):
			if adj[i][i] == 0:
				continue
			ans += 1
			dfs(adj, i)
		return ans
