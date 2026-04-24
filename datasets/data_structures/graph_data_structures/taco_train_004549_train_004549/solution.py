class Solution:

	def dfsOfGraph(self, V, adj):
		lst = []

		def dfs(st):
			if st not in lst:
				lst.append(st)
				for i in adj[st]:
					dfs(i)
		dfs(0)
		return lst
