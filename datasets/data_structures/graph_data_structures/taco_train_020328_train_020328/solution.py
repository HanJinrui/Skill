from typing import List

class Solution:

	def shortestPath(self, n: int, m: int, edges: List[List[int]]) -> List[int]:
		distance = [100000] * n
		distance[0] = 0
		for i in range(n - 1):
			for edge in edges:
				u = edge[0]
				v = edge[1]
				w = edge[2]
				if distance[u] + w < distance[v]:
					distance[v] = distance[u] + w
		for i in range(len(distance)):
			if distance[i] == 100000:
				distance[i] = -1
		return distance
