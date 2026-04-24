from typing import List
from collections import defaultdict
import heapq
import sys

class Solution:

	def countPaths(self, n: int, roads: List[List[int]]) -> int:
		mod = 10 ** 9 + 7
		adj = defaultdict(list)
		for (u, v, w) in roads:
			adj[u].append([v, w])
			adj[v].append([u, w])
		distance = [float('inf')] * n
		ways = [0] * n
		distance[0] = 0
		ways[0] = 1
		q = []
		heapq.heappush(q, [0, 0])
		while len(q) != 0:
			(dist, node) = heapq.heappop(q)
			for i in adj[node]:
				(v, w) = i
				d = dist + w
				if distance[v] > d:
					distance[v] = d
					heapq.heappush(q, [distance[v], v])
					ways[v] = ways[node]
				elif distance[v] == d:
					ways[v] += ways[node] % mod
		return ways[n - 1]
