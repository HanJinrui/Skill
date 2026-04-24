from typing import List

class Solution:

	def eventualSafeNodes(self, V: int, adj: List[List[int]]) -> List[int]:
		adjrev = [[] for i in range(V)]
		indeg = [0 for i in range(V)]
		for i in range(V):
			for j in adj[i]:
				adjrev[j].append(i)
				indeg[i] += 1
		safe = []
		q = []
		for i in range(V):
			if indeg[i] == 0:
				q.append(i)
		while q:
			x = q.pop(0)
			safe.append(x)
			for i in adjrev[x]:
				indeg[i] -= 1
				if indeg[i] == 0:
					q.append(i)
		safe.sort()
		return safe
