import heapq

class Solution:

	def dijkstra(self, V, adj, S):
		dis = [float('inf') for _ in range(V)]
		pq = [(0, S)]
		dis[S] = 0
		while pq:
			(d, u) = heapq.heappop(pq)
			for (v, e) in adj[u]:
				if d + e < dis[v]:
					dis[v] = d + e
					heapq.heappush(pq, (dis[v], v))
		return dis
