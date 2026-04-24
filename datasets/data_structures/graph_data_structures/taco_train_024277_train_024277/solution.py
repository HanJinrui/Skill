class Solution:

	def kosaraju(self, V, adj):

		def dfs1(i):
			if i in v:
				return i
			else:
				v.add(i)
				for j in adj[i]:
					dfs1(j)
			stk.append(i)

		def dfs2(i):
			if i in v:
				return
			else:
				v.add(i)
				for j in adj1[i]:
					dfs2(j)
		adj1 = [[] for i in range(V)]
		for i in range(len(adj)):
			for j in adj[i]:
				adj1[j].append(i)
		stk = []
		v = set()
		for i in range(V):
			if i not in v:
				dfs1(i)
		v = set()
		c = 0
		for i in stk[::-1]:
			if i not in v:
				dfs2(i)
				c += 1
		return c
