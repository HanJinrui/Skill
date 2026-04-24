class Solution:

	def topoSort(self, V, adj):
		ans = []
		v = set()

		def dfs(node):
			v.add(node)
			for x in adj[node]:
				if x not in v:
					dfs(x)
			ans.append(node)
		for x in range(V):
			if x not in v:
				dfs(x)
		return ans[::-1]
