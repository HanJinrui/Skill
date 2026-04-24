class Solution:

	def minimumCut(self, A, S, T, N):
		ans = []
		breaker = 0
		start = S
		end = T
		adj = [[] for i in range(N)]
		scores = {}
		for u in range(N):
			for v in range(N):
				adj[u].append(v)
				scores[u, v] = A[u][v]
		while breaker == 0:
			visited = [False for x in range(N)]
			(tflow, tnodes) = self.BFS(start, end, adj, visited, scores)
			if tflow > 0:
				for i in range(len(tnodes) - 1):
					u = tnodes[i]
					v = tnodes[i + 1]
					scores[u, v] -= tflow
					scores[v, u] += tflow
			else:
				breaker = 1
		visited = [False for x in range(N)]
		visited = self.findReachable(start, scores, adj, visited)
		for i in range(N):
			for j in range(N):
				if A[i][j] > 0:
					if visited[i] and (not visited[j]):
						ans.append(i)
						ans.append(j)
		if len(ans) == 0:
			return [-1]
		return ans

	def findReachable(self, start, scores, adj, visited):
		visited[start] = True
		for nei in adj[start]:
			weight = scores[start, nei]
			if visited[nei] or weight == 0:
				continue
			visited = self.findReachable(nei, scores, adj, visited)
		return visited

	def BFS(self, start, end, adj, visited, scores):
		tnodes = [start]
		tflow = 0
		visited[start] = True
		for nei in adj[start]:
			weight = scores[start, nei]
			if visited[nei] or weight == 0:
				continue
			if nei == end:
				tnodes.append(end)
				tflow = weight
				return (tflow, tnodes)
			(tflow2, tnodes2) = self.BFS(nei, end, adj, visited, scores)
			if tflow2 > 0:
				tflow = min(weight, tflow2)
				tnodes = tnodes + tnodes2
				return (tflow, tnodes)
		return (tflow, tnodes)
