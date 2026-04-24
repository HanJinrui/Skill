class Solution:

	def printGraph(self, v, adj):
		for i in range(v):
			adj[i].insert(0, i)
		return adj
