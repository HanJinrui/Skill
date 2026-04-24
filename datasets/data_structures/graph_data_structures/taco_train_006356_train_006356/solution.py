class Solution:

	def isBridge(self, V, adj, c, d):

		def dfs(src):
			vis[src] = 0
			for i in adj[src]:
				if vis[i]:
					dfs(i)
		if c in adj[d]:
			adj[d].remove(c)
		if d in adj[c]:
			adj[c].remove(d)
		else:
			return 0
		vis = [1] * V
		dfs(c)
		return vis[d]
