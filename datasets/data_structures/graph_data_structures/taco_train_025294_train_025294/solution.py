from collections import defaultdict
from typing import List
import heapq

class Solution:

	def minimumCost(self, flights: List[List[int]], n: int, k: int) -> int:
		q = [(0, k)]
		adj = defaultdict(list)
		dist = {}
		for (u, v, w) in flights:
			adj[u].append((v, w))
		while q:
			(dis, node) = heapq.heappop(q)
			if node not in dist:
				dist[node] = dis
				for (nei, weight) in adj[node]:
					heapq.heappush(q, (dis + weight, nei))
		return max(dist.values()) if len(dist) == n else -1
