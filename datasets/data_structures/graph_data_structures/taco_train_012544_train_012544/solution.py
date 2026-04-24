from collections import defaultdict
import sys
sys.setrecursionlimit(10 ** 9)

class Solution:

	def dfs(self, visited, adj, u, st):
		visited[u] = True
		st.add(u)
		for v in adj[u]:
			if not visited[v]:
				self.dfs(visited, adj, v, st)
		visited[u] = False

	def captainAmerica(self, N, M, V):
		(set1, set2) = (set(), set())
		visited = [False for i in range(N + 1)]
		adj = defaultdict(list)
		for i in range(M):
			adj[V[i][0]].append(V[i][1])
		self.dfs(visited, adj, 1, set1)
		self.dfs(visited, adj, N, set2)
		return len(set1.intersection(set2))
